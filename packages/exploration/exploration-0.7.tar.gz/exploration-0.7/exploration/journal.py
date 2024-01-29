"""
- Authors: Peter Mawhorter
- Consulted:
- Date: 2022-9-4
- Purpose: Parsing for journal-format exploration records.

A journal fundamentally consists of a number of lines detailing
decisions reached, options observed, and options chosen. Other
information like enemies fought, items acquired, or general comments may
also be present.

The start of each line is a single letter that determines the entry
type, and remaining parts of that line separated by whitespace determine
the specifics of that entry. Indentation is allowed and ignored; its
suggested use is to indicate which entries apply to previous entries
(e.g., tags, annotations, effects, and requirements).

The `convertJournal` function converts a journal string into a
`core.DiscreteExploration` object, or adds to an existing exploration
object if one is specified.

To support slightly different journal formats, a `Format` dictionary is
used to define the exact notation used for various things.
"""

from __future__ import annotations

from typing import (
    Optional, List, Tuple, Dict, Union, Collection, get_args, cast,
    Sequence, Literal, Set, TypedDict
)

import re
import warnings
import textwrap

from . import core, base, parsing


#----------------------#
# Parse format details #
#----------------------#

JournalEntryType = Literal[
    'preference',
    'alias',
    'custom',
    'DEBUG',

    'START',
    'explore',
    'return',
    'action',
    'retrace',
    'warp',
    'wait',
    'observe',
    'END',

    'requirement',
    'challenge',
    'effect',
    'apply',

    'tag',
    'annotate',

    'context',
    'domain',
    'focus',
    'zone',

    'unify',
    'obviate',
    'extinguish',
    'complicate',

    'fulfills',

    'relative'
]
"""
One of the types of entries that can be present in a journal. These can
be written out long form, or abbreviated using a single letter (see
`DEFAULT_FORMAT`). Each journal line is either an entry or a continuation
of a previous entry. The available types are:

- 'P' / 'preference': Followed by a setting name and value, controls
    global preferences for journal processing.

- '=' / 'alias': Followed by zero or more words and then a block of
    commands, this establishes an alias that can be used as a custom
    command. Within the command block, curly braces surrounding a word
    will be replaced by the argument in the same position that that word
    appears following the alias (for example, an alias defined using:

        = redDoor name [
          o {name}
            qb red
        ]

    could be referenced using:

        > redDoor door

    and that reference would be equivalent to:

        o door
          qb red

    To help aliases be more flexible, if '_' is referenced between curly
    braces (or '_' followed by an integer), it will be substituted with
    an underscore followed by a unique number (these numbers will count
    up with each such reference used by a specific `JournalObserver`
    object). References within each alias substitution which are
    suffixed with the same digit (or which are unsuffixed) will get the
    same value. So for example, an alias:

        = savePoint [
          o {_}
          x {_} {_1} {_2}
              g savePoint
          a save
          t {_2}
        ]

    when deployed twice like this:

        > savePoint
        > savePoint

    might translate to:

        o _17
        x _17 _18 _19
            g savePoint
        a save
        t _19
        o _20
        x _20 _21 _22
            g savePoint
        a save
        t _22

- '>' / 'custom': Re-uses the code from a previously-defined alias. This
    command type is followed by an alias name and then one argument for
    each parameter of the named alias (see above for examples).

- '?' / 'DEBUG': Prints out debugging information when executed. See
    `DebugAction` for the possible argument values and `doDebug` for
    more information on what they mean.

- 'S" / 'START': Names the starting decision (or zone::decision pair).
    Must appear first except in journal fragments.

- 'x' / 'explore': Names a transition taken and the decision (or
    new-zone::decision) reached as a result, possibly with a name for
    the reciprocal transition which is created. Use 'zone' afterwards to
    swap around zones above level 0.

- 'r' / 'return': Names a transition taken and decision returned to,
    connecting a transition which previously connected to an unexplored
    area back to a known decision instead. May also include a reciprocal
    name.

- 'a' / 'action': Names an action taken at the current decision and may
    include effects and/or requirements.

- 't' / 'retrace': Names a transition taken, where the destination is
    already explored.

- 'w' / 'wait': indicates a step of exploration where no transition is
    taken. You can use 'A' afterwards to apply effects in order to
    represent events that happen outside of player control. Use 'action'
    instead for player-initiated effects.

- 'p' / 'warp': Names a new decision (or zone::decision) to be at, but
    without adding a transition there from the previous decision. If no
    zone name is provided but the destination is a novel decision, it
    will be placed into the same zones as the origin.

- 'o' / 'observe': Names a transition observed from the current
    decision, or a transition plus destination if the destination is
    known, or a transition plus destination plus reciprocal if
    reciprocal information is also available. Observations don't create
    exploration steps.

- 'E' / 'END': Names an ending which is reached from the current
    decision via a new automatically-named transition.

- 'q' / 'requirement': Specifies a requirement to apply to the
    most-recently-defined transition or its reciprocal.

- 'e' / 'effect': Specifies a `base.Consequence` that *replaces* the
    consequence for the currently-relevant transition (or its reciprocal
    or both if `reciprocalPart` or `bothPart` is used). The remainder of
    the line (and/or the next few lines) should be parsable using
    `ParseFormat.parseConsequence`, or if not, using
    `ParseFormat.parseEffect` for a single effect.

- 'A' / 'apply': Specifies an effect to be immediately applied to the
    current state, relative to the most-recently-taken or -defined
    transition. If a 'transitionPart' or 'reciprocalPart' target
    specifier is included, the effect will also be recorded as an effect
    in the current active `core.Consequence` context for the most recent
    transition or reciprocal, but otherwise it will just be applied
    without being stored in the graph. Note that effects which are
    hidden until activated should have their 'hidden' property set to
    `True`, regardless of whether they're added to the graph before or
    after the transition they are associated with. Also, certain effects
    like 'bounce' cannot be applied retroactively.

- 'g' / 'tag': Applies one or more tags to the current decision, or to
    either the most-recently-taken transition or its reciprocal if
    'transitionPart' or 'reciprocalPart' is specified.

- 'n' / 'annotate': Like 'tag' but applies an annotation.

- 'c' / 'context': Specifies either 'commonContext' or the name of a
    specific focal context to activate. Focal contexts represent things
    like multiple characters or teams, and by default capabilities,
    tokens, and skills are all tied to a specific focal context. If the
    name given is anything other than the 'commonContext' value then
    that context will be swapped to active (and created as a blank
    context if necessary). TODO: THIS

- 'd' / 'domain': Specifies a domain name, swapping to that domain as
    the current domain, and setting it as an active domain in the
    current `core.FocalContext`. This does not de-activate other
    domains, but the journal has a notion of a single 'current' domain
    that entries will be applied to. If no focal point has been
    specified and we swap into a plural-focalized domain, the
    alphabetically-first focal point within that domain will be
    selected, but focal points for each domain are remembered when
    swapping back. Use the 'notApplicable' value after a domain name to
    deactivate that domain. Any other value after a domain name must be
    one of the 'focalizeSingular', 'focalizePlural', or
    'focalizeSpreading' values to indicate that the domain uses that
    type of focalization. These should only be used when a domain is
    created, you cannot change the focalization type of a domain after
    creation. If no focalization type is given along with a new domain
    name, singular focalization will be used for that domain. If no
    domain is specified before performing the first action of an
    exploration, the `core.DEFAULT_DOMAIN` with singular focalization
    will be set up. TODO: THIS

- 'f' / 'focus': Specifies a `core.FocalPointName` for the specific
    focal point that should be acted on by subsequent journal entries in
    a plural-focalized domain. Focal points represent things like
    individual units in a game where you have multiple units to control.

    May also specify a domain followed by a focal point name to change
    the focal point in a domain other than the current domain.

- 'z' / 'zone': Specifies a zone name and a level (via extra `zonePart`
    characters) that will replace the current zone at the given
    hierarchy level for the current decision. This is done using the
    `core.DiscreteExploration.reZone` method.

- 'u' / 'unify': Specifies a decision with which the current decision
    will be unified (or two decisions that will be unified with each
    other), merging their transitions. The name of the merged decision
    is the name of the second decision specified (or the only decision
    specified when merging the current decision). Can instead target a
    transition or reciprocal to merge (which must be at the current
    decision), although the transition to merge with must either lead to
    the same destination or lead to an unknown destination (which will
    then be merged with the transition's destination). Any transitions
    between the two merged decisions will remain as actions at the new
    decision.

- 'v' / 'obviate': Specifies a transition at the current decision and a
    decision that it links to and updates that information, without
    actually crossing the transition. The reciprocal transition must
    also be specified, although one will be created if it didn't already
    exist. If the reciprocal does already exist, it must lead to an
    unknown decision.

- 'X' / 'extinguish': Deletes an transition at the current decision. If it
    leads to an unknown decision which is not otherwise connected to
    anything, this will also delete that decision (even if it already
    has tags or annotations or the like). Can also be used (with a
    decision target) to delete a decision, which will delete all
    transitions touching that decision. Note that usually, 'unify' is
    easier to manage than extinguish for manipulating decisions.
    - 'complicate': Takes a transition between two known decisions and
    adds a new known decision in the middle of it. The old ends of the
    transition both connect to the new decision, and new names are given
    to their new reciprocals. Does not change the player's position.

- 'F' / 'fulfills': Specifies a requirement and a capability, and adds
    an equivalence to the current graph such that if that requirement is
    fulfilled, the specified capability is considered to be active. This
    allows for later discovery of one or more powers which allow
    traversal of previously-marked transitions whose true requirements
    were unknown when they were discovered.

- '@' / 'relative': Specifies a decision to be treated as the 'current
    decision' without actually setting the position there. Use the
    marker twice (default '@ @') to enter relative mode at the current
    decision. Until used to reverse this effect, all position-changing
    entries change this relative position value instead of the actual
    position in the graph, and updates are applied to the current graph
    without creating new exploration steps or applying any effects.
    Useful for doing things like noting information about far-away
    locations disclosed in a cutscene. Can target a transition at the
    current node, in which case that is counted as the
    'most-recent-transition' for entry purposes and the same relative
    mode is entered.
"""

JournalTargetType = Literal[
    'decisionPart',
    'transitionPart',
    'reciprocalPart',
    'bothPart',
    'zonePart',
    'actionPart',
]
"""
The different parts that an entry can target. The signifiers for these
target types will be concatenated with a journal entry signifier in some
cases. For example, by default 'g' as an entry type means 'tag', and 't'
as a target type means 'transition'. So 'gt' as an entry type means 'tag
transition' and applies the relevant tag to the most-recently-created
transition instead of the most-recently-created decision. The
`targetSeparator` character (default '@') is used to combine an entry
type with a target type when the entry type is written without
abbreviation. In that case, the target specifier may drop the suffix
'Part' (e.g., tag@transition in place of `gt`). The available target
parts are each valid only for specific entry types. The target parts are:

- 'decisionPart' - Use to specify that the entry applies to a decision
    when it would normally apply to something else.
- 'transitionPart' - Use to specify that the entry applies to a
    transition instead of a decision.
- 'reciprocalPart' - Use to specify that the entry applies to a
    reciprocal transition instead of a decision or the normal
    transition.
- 'bothPart' - Use to specify that the entry applies to both of two
    possibilities, such as to a transition and its reciprocal.
- 'zonePart' - Use only for re-zoning to indicate the hierarchy level. May
    be repeated; each instance increases the hierarchy level by 1
    starting from 0.
- 'actionPart' - Use only for the 'observe' entry to specify that the
    observed transition is an action (i.e., its destination is the same
    as its source) rather than a real transition (whose destination would
    be a new, unknown node).

The entry types where a target specifier can be applied are:

- 'requirement': By default these are applied to transitions, but the
    'reciprocalPart' target can be used to apply to a reciprocal
    instead. Use `bothPart` to apply the same requirement to both the
    transition and its reciprocal.
- 'effect': Same as 'requirement'.
- 'apply': Same as 'effect' (and see above).
- 'tag': Applies the tag to the specified target instead of the
    most-recently-created decision, which is the default.
- 'annotation': Same as 'tag', but can also use a decision-part target
    to annotate the current decision (default is to annotate the
    exploration step).
- 'unify': By default applies to a decision, but can be applied to a
    transition or reciprocal instead.
- 'extinguish': By default applies to a transition and its reciprocal,
    but can be applied to just one or the other, or to a decision.
- 'relative': Only 'transition' applies here and changes the
    most-recent-transition value when entering relative mode instead of
    just changing the current-decision value. Can be used within
    relative mode to pick out an existing transition as well.
- 'zone': This is the only place where the 'zonePart' target type
    applies, and it can actually be applied as many times as you want.
    Each application makes the zone specified apply to a higher level in
    the hierarchy of zones, so that instead of swapping the level-0 zone
    using 'z', the level-1 zone can be changed using 'zz' or the level 2
    zone using 'zzz', etc. In lieu of using 'z's, you can also just write
    as an integer the level you want to use (e.g., z0 for a level-0 zone,
    or z1 for a level-1 zone). When using a long-form entry type, the
    target may be given as the string 'zone' in which case the level-1
    zone is used. To use a different zone level with a long-form entry
    type, use multiple 'z's, or an integer.
- 'observe': The only place where the 'actionPart' target type applies,
    and that is the only applicable target type. Applying `actionPart`
    turns the observed transition into an action.
"""

JournalInfoType = Literal[
    'on',
    'off',
    'domainFocalizationSingular',
    'domainFocalizationPlural',
    'domainFocalizationSpreading',
    'commonContext',
    'comment',
    'unknownItem',
    'notApplicable',
    'exclusiveDomain',
    'targetSeparator',
    'reciprocalSeparator',
    'transitionAtDecision',
    'blockDelimiters',
]
"""
Represents a part of the journal syntax which isn't an entry type but is
used to mark something else. For example, the character denoting an
unknown item. The available values are:

- 'on' / 'off': Used to indicate on/off status for preferences.
- 'domainFocalizationSingular' / 'domainFocalizationPlural'
  / 'domainFocalizationSpreading': Used as markers after a domain for
  the `core.DomainFocalization` values.
- 'commonContext': Used with 'context' in place of a
    `core.FocalContextName` to indicate that we are targeting the common
    focal context.
- 'comment': Indicates extraneous text that should be ignored by the
    journal parser. Note that tags and/or annotations should usually be
    used to apply comments that will be accessible when viewing the
    exploration object.
- 'unknownItem': Used in place of an item name to indicate that
    although an item is known to exist, it's not yet know what that item
    is. Note that when journaling, you should make up names for items
    you pick up, even if you don't know what they do yet. This notation
    should only be used for items that you haven't picked up because
    they're inaccessible, and despite being apparent, you don't know
    what they are because they come in a container (e.g., you see a
    sealed chest, but you don't know what's in it).
- 'notApplicable': Used in certain positions to indicate that something
    is missing entirely or otherwise that a piece of information
    normally supplied is unnecessary. For example, when used as the
    reciprocal name for a transition, this will cause the reciprocal
    transition to be deleted entirely, or when used before a domain name
    with the 'domain' entry type it deactivates that domain. TODO
- 'exclusiveDomain': Used to indicate that a domain being activated
    should deactivate other domains, instead of being activated along
    with them.
- 'targetSeparator': Used in long-form entry types to separate the entry
    type from a target specifier when a target is specified. Default is
    '@'. For example, a 'gt' entry (tag transition) would be expressed
    as 'tag@transition' in the long form.
- 'reciprocalSeparator': Used to indicate, within a requirement or a
    tag set, a separation between requirements/tags to be applied to the
    forward direction and requirements/tags to be applied to the reverse
    direction. Not always applicable (e.g., actions have no reverse
    direction).
- 'transitionAtDecision' Used to separate a decision name from a
    transition name when identifying a specific transition.
- 'blockDelimiters' Two characters used to delimit the start and end of
    a block of entries. Used for things like edit effects.
"""

JournalMarkerType = Union[
    JournalEntryType,
    JournalTargetType,
    JournalInfoType
]
"Any journal marker type."


JournalFormat = Dict[JournalMarkerType, str]
"""
A journal format is specified using a dictionary with keys that denote
journal marker types and values which are one-to-several-character
strings indicating the markup used for that entry/info type.
"""

DEFAULT_FORMAT: JournalFormat = {
    # Toggles
    'preference': 'P',

    # Alias handling
    'alias': '=',
    'custom': '>',

    # Debugging
    'DEBUG': '?',

    # Core entry types
    'START': 'S',
    'explore': 'x',
    'return': 'r',
    'action': 'a',
    'retrace': 't',
    'wait': 'w',
    'warp': 'p',
    'observe': 'o',
    'END': 'E',

    # Transition properties
    'requirement': 'q',
    'challenge': 'h',
    'effect': 'e',
    'apply': 'A',

    # Tags & annotations
    'tag': 'g',
    'annotate': 'n',

    # Context management
    'context': 'c',
    'domain': 'd',
    'focus': 'f',
    'zone': 'z',

    # Revisions
    'unify': 'u',
    'obviate': 'v',
    'extinguish': 'X',
    'complicate': 'C',

    # Capability discovery
    'fulfills': 'F',

    # Relative mode
    'relative': '@',

    # Target specifiers
    'decisionPart': 'd',
    'transitionPart': 't',
    'reciprocalPart': 'r',
    'bothPart': 'b',
    'zonePart': 'z',
    'actionPart': 'a',

    # Info markers
    'on': 'on',
    'off': 'off',
    'domainFocalizationSingular': 'singular',
    'domainFocalizationPlural': 'plural',
    'domainFocalizationSpreading': 'spreading',
    'commonContext': '*',
    'comment': '#',
    'unknownItem': '?',
    'notApplicable': '-',
    'exclusiveDomain': '>',
    'reciprocalSeparator': '/',
    'targetSeparator': '@',
    'transitionAtDecision': '%',
    'blockDelimiters': '[]',
}
"""
The default `JournalFormat` dictionary.
"""


DebugAction = Literal[
    'here',
    'transition',
    'destinations',
    'steps',
    'decisions'
]
"""
The different kinds of debugging commands.
"""


class JournalParseFormat(parsing.ParseFormat):
    """
    A ParseFormat manages the mapping from markers to entry types and
    vice versa.
    """
    def __init__(
        self,
        formatDict: parsing.Format = parsing.DEFAULT_FORMAT,
        journalMarkers: JournalFormat = DEFAULT_FORMAT
    ):
        """
        Sets up the parsing format. Accepts base and/or journal format
        dictionaries, but they both have defaults (see `DEFAULT_FORMAT`
        and `parsing.DEFAULT_FORMAT`). Raises a `ValueError` unless the
        keys of the format dictionaries exactly match the required
        values (the `parsing.Lexeme` values for the base format and the
        `JournalMarkerType` values for the journal format).
        """
        super().__init__(formatDict)
        self.journalMarkers: JournalFormat = journalMarkers

        # Build comment regular expression
        self.commentRE = re.compile(
            self.journalMarkers.get('comment', '#') + '.*$',
            flags=re.MULTILINE
        )

        # Get block delimiters
        blockDelimiters = journalMarkers.get('blockDelimiters', '[]')
        if len(blockDelimiters) != 2:
            raise ValueError(
                f"Block delimiters must be a length-2 string containing"
                f" the start and end markers. Got: {blockDelimiters!r}."
            )
        blockStart = blockDelimiters[0]
        blockEnd = blockDelimiters[1]
        self.blockStart = blockStart
        self.blockEnd = blockEnd

        # Add backslash for literal if it's an RE special char
        if blockStart in '[]()*.?^$&+\\':
            blockStart = '\\' + blockStart
        if blockEnd in '[]()*.?^$&+\\':
            blockEnd = '\\' + blockEnd

        # Build block start and end regular expressions
        self.blockStartRE = re.compile(
            blockStart + r'\s*$',
            flags=re.MULTILINE
        )
        self.blockEndRE = re.compile(
            r'^\s*' + blockEnd,
            flags=re.MULTILINE
        )

        # Check that journalMarkers doesn't have any extra keys
        markerTypes = (
            get_args(JournalEntryType)
          + get_args(JournalTargetType)
          + get_args(JournalInfoType)
        )
        for key in journalMarkers:
            if key not in markerTypes:
                raise ValueError(
                    f"Format dict has key '{key}' which is not a"
                    f" recognized entry or info type."
                )

        # Check completeness of formatDict
        for mtype in markerTypes:
            if mtype not in journalMarkers:
                raise ValueError(
                    f"Journal markers dict is missing an entry for"
                    f" marker type '{mtype}'."
                )

        # Build reverse dictionaries from markers to entry types and
        # from markers to target types (no reverse needed for info
        # types).
        self.entryMap: Dict[str, JournalEntryType] = {}
        self.targetMap: Dict[str, JournalTargetType] = {}
        entryTypes = set(get_args(JournalEntryType))
        targetTypes = set(get_args(JournalTargetType))

        # Check for duplicates and create reverse maps
        for name, marker in journalMarkers.items():
            if name in entryTypes:
                # Duplicates not allowed among entry types
                if marker in self.entryMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.entryMap[marker]}'."
                    )

                # Map markers to entry types
                self.entryMap[marker] = cast(JournalEntryType, name)
            elif name in targetTypes:
                # Duplicates not allowed among entry types
                if marker in self.targetMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.targetMap[marker]}'."
                    )

                # Map markers to entry types
                self.targetMap[marker] = cast(JournalTargetType, name)

            # else ignore it since it's an info type

    def markers(self) -> List[str]:
        """
        Returns the list of all entry-type markers (but not other kinds
        of markers), sorted from longest to shortest to help avoid
        ambiguities when matching.
        """
        entryTypes = get_args(JournalEntryType)
        return sorted(
            (
                m
                for (et, m) in self.journalMarkers.items()
                if et in entryTypes
            ),
            key=lambda m: -len(m)
        )

    def markerFor(self, markerType: JournalMarkerType) -> str:
        """
        Returns the marker for the specified entry/info/effect/etc.
        type.
        """
        return self.journalMarkers[markerType]

    def determineEntryType(self, entryBits: List[str]) -> Tuple[
        JournalEntryType,
        Union[None, JournalTargetType, int],
        List[str]
    ]:
        """
        Given a sequence of strings that specify a command, returns a
        tuple containing the entry type, target part, and list of
        arguments for that command. If no target type was included, the
        second entry of the return value will be `None`, and in the
        special case of zones, it will be an integer indicating the
        hierarchy level according to how many times the 'zonePart'
        target specifier was present, default 0.
        """
        # Get entry specifier
        entrySpecifier = entryBits[0]
        entryArgs = entryBits[1:]

        entryType: Optional[JournalEntryType] = None
        entryTarget: Union[None, JournalTargetType, int] = None
        validEntryTypes: Set[JournalEntryType] = set(
            get_args(JournalEntryType)
        )
        validEntryTargets: Set[JournalTargetType] = set(
            get_args(JournalTargetType)
        )

        # Look for a long-form entry specifier with an @ sign separating
        # the entry type from the entry target
        targetMarker = self.markerFor('targetSeparator')
        if (
            targetMarker in entrySpecifier
        and not entrySpecifier.startswith(targetMarker)
            # Because the targetMarker is also a valid entry type!
        ):
            specifierBits = entrySpecifier.split(targetMarker)
            if len(specifierBits) != 2:
                raise JournalParseError(
                    f"When a long-form entry specifier contains a"
                    f" colon, it must contain exactly one (to split the"
                    f" entry type from the entry target). We got"
                    f" '{entrySpecifier}'."
                )
            entryTypeGuess: str
            entryTargetGuess: Optional[str]
            entryTypeGuess, entryTargetGuess = specifierBits
            if entryTypeGuess not in validEntryTypes:
                raise JournalParseError(
                    f"Invalid long-form entry type: {entryType!r}"
                )
            else:
                entryType = cast(JournalEntryType, entryTypeGuess)

            if entryType == 'zone':
                if entryTargetGuess.isdigit():
                    entryTarget = int(entryTargetGuess)
                elif entryTargetGuess == 'zone':
                    entryTarget = 1
                elif (
                    len(entryTargetGuess) > 0
                and set(entryTargetGuess) != {'z'}
                ):
                    raise JournalParseError(
                        f"Invalid target specifier for"
                        f" zone:\n{entryTargetGuess}"
                    )
                else:
                    entryTarget = len(entryTargetGuess)

            elif entryTargetGuess in validEntryTargets:
                entryTarget = cast(JournalTargetType, entryTargetGuess)

            else:
                if entryTargetGuess + 'Part' in validEntryTargets:
                    entryTarget = cast(
                        JournalTargetType,
                        entryTargetGuess + 'Part'
                    )
                else:
                    origGuess = entryTargetGuess
                    entryTargetGuess = self.targetMap.get(
                        entryTargetGuess
                    )
                    if entryTargetGuess not in validEntryTargets:
                        raise JournalParseError(
                            f"Invalid long-form entry target:"
                            f" {origGuess!r}"
                        )
                    else:
                        entryTarget = cast(
                            JournalTargetType,
                            entryTargetGuess
                        )

        elif entrySpecifier in validEntryTypes:
            # Might be a long-form specifier without a colon
            entryType = cast(JournalEntryType, entrySpecifier)
            entryTarget = None
            if entryType == 'zone':
                entryTarget = 0

        else:  # parse a short-form entry specifier
            typeSpecifier = entrySpecifier[0]
            if typeSpecifier not in self.entryMap:
                raise JournalParseError(
                    f"Entry does not begin with a recognized entry"
                    f" marker:\n{entryBits}"
                )
            entryType = self.entryMap[typeSpecifier]

            # Figure out the entry target from second+ character(s)
            targetSpecifiers = entrySpecifier[1:]
            if entryType == 'zone':
                specifiers = set(targetSpecifiers)
                if targetSpecifiers.isdigit():
                    entryTarget = int(targetSpecifiers)
                elif len(specifiers) > 0 and specifiers != {'z'}:
                    raise JournalParseError(
                        f"Invalid target specifier for zone:\n{entryBits}"
                    )
                else:
                    entryTarget = len(targetSpecifiers)
            elif len(targetSpecifiers) > 0:
                if len(targetSpecifiers) > 1:
                    raise JournalParseError(
                        f"Entry has too many target specifiers:\n{entryBits}"
                    )
                elif targetSpecifiers not in self.targetMap:
                    raise JournalParseError(
                        f"Unrecognized target specifier:\n{entryBits}"
                    )
                entryTarget = self.targetMap[targetSpecifiers]
        # else entryTarget remains None

        return (entryType, entryTarget, entryArgs)

    def argsString(self, pieces: List[str]) -> str:
        """
        Recombines pieces of a journal argument (such as those produced
        by `unparseEffect`) into a single string. When there are
        multi-line or space-containing pieces, this adds block start/end
        delimiters and indents the piece if it's multi-line.
        """
        result = ''
        for piece in pieces:
            if '\n' in piece:
                result += (
                    f" {self.blockStart}\n"
                    f"{textwrap.indent(piece, '  ')}"
                    f"{self.blockEnd}"
                )
            elif ' ' in piece:
                result += f" {self.blockStart}{piece}{self.blockEnd}"
            else:
                result += ' ' + piece

        return result[1:]  # chop off extra initial space

    def removeComments(self, text: str) -> str:
        """
        Given one or more lines from a journal, removes all comments from
        it/them. Any '#' and any following characters through the end of
        a line counts as a comment.

        Returns the text without comments.

        Example:

        >>> pf = JournalParseFormat()
        >>> pf.removeComments('abc # 123')
        'abc '
        >>> pf.removeComments('''\\
        ... line one # comment
        ... line two # comment
        ... line three
        ... line four # comment
        ... ''')
        'line one \\nline two \\nline three\\nline four \\n'
        """
        return self.commentRE.sub('', text)

    def findBlockEnd(self, string: str, startIndex: int) -> int:
        """
        Given a string and a start index where a block open delimiter
        is, returns the index within the string of the matching block
        closing delimiter.

        There are two possibilities: either both the opening and closing
        delimiter appear on the same line, or the block start appears at
        the end of a line (modulo whitespce) and the block end appears
        at the beginning of a line (modulo whitespace). Any other
        configuration is invalid and may lead to a `JournalParseError`.

        Note that blocks may be nested within each other, including
        nesting single-line blocks in a multi-line block. It's also
        possible for several single-line blocks to appear on the same
        line.

        Examples:

        >>> pf = JournalParseFormat()
        >>> pf.findBlockEnd('[ A ]', 0)
        4
        >>> pf.findBlockEnd('[ A ] [ B ]', 0)
        4
        >>> pf.findBlockEnd('[ A ] [ B ]', 6)
        10
        >>> pf.findBlockEnd('[ A [ B ] ]', 0)
        10
        >>> pf.findBlockEnd('[ A [ B ] ]', 4)
        8
        >>> pf.findBlockEnd('[ [ B ]', 0)
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        >>> pf.findBlockEnd('[\\nABC\\n]', 0)
        6
        >>> pf.findBlockEnd('[\\nABC]', 0)  # End marker must start line
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        >>> pf.findBlockEnd('[\\nABC\\nDEF[\\nGHI\\n]\\n  ]', 0)
        19
        >>> pf.findBlockEnd('[\\nABC\\nDEF[\\nGHI\\n]\\n  ]', 9)
        15
        >>> pf.findBlockEnd('[\\nABC\\nDEF[ GHI ]\\n  ]', 0)
        19
        >>> pf.findBlockEnd('[\\nABC\\nDEF[ GHI ]\\n  ]', 9)
        15
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n  ]\\n]', 0)
        24
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n  ]\\n]', 11)
        22
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n  ]\\n]', 16)
        18
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H \\n  ]\\n]', 16)
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n\\n]', 0)
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        """
        # Find end of the line that the block opens on
        try:
            endOfLine = string.index('\n', startIndex)
        except ValueError:
            endOfLine = len(string)

        # Determine if this is a single-line or multi-line block based
        # on the presence of *anything* after the opening delimiter
        restOfLine = string[startIndex + 1:endOfLine]
        if restOfLine.strip() != '':  # A single-line block
            level = 1
            for restIndex, char in enumerate(restOfLine):
                if char == self.blockEnd:
                    level -= 1
                    if level <= 0:
                        break
                elif char == self.blockStart:
                    level += 1

            if level == 0:
                return startIndex + 1 + restIndex
            else:
                raise JournalParseError(
                    f"Got to end of line in single-line block without"
                    f" finding the matching end-of-block marker."
                    f" Remainder of line is:\n  {restOfLine!r}"
                )

        else:  # It's a multi-line block
            level = 1
            index = startIndex + 1
            while level > 0 and index < len(string):
                nextStart = self.blockStartRE.search(string, index)
                nextEnd = self.blockEndRE.search(string, index)
                if nextEnd is None:
                    break  # no end in sight; level won't be 0
                elif (
                    nextStart is None
                 or nextStart.start() > nextEnd.start()
                ):
                    index = nextEnd.end()
                    level -= 1
                    if level <= 0:
                        break
                else:  # They cannot be equal
                    index = nextStart.end()
                    level += 1

            if level == 0:
                if nextEnd is None:
                    raise RuntimeError(
                        "Parsing got to level 0 with no valid end"
                        " match."
                    )
                return nextEnd.end() - 1
            else:
                raise JournalParseError(
                    f"Got to the end of the entire string and didn't"
                    f" find a matching end-of-block marker. Started at"
                    f" index {startIndex}."
                )


#-------------------#
# Errors & Warnings #
#-------------------#

class JournalParseError(ValueError):
    """
    Represents a error encountered when parsing a journal.
    """
    pass


class LocatedJournalParseError(JournalParseError):
    """
    An error during journal parsing that includes additional location
    information.
    """
    def __init__(
        self,
        src: str,
        index: int,
        cause: Exception
    ) -> None:
        """
        In addition to the underlying error, the journal source text and
        the index within that text where the error occurred are
        required.
        """
        super().__init__("localized error")
        self.src = src
        self.index = index
        self.cause = cause

    def __str__(self):
        """
        Includes information about the location of the error and the
        line it appeared on.
        """
        context, line, pos = errorContext(self.src, self.index)
        context = context.rstrip('\n')
        return (
            f"\n  In journal on line {line} near character {pos}:"
            f"\n    {context}"
            f"\n  Error is:"
            f"\n{type(self.cause).__name__}: {self.cause}"
        )


def errorContext(string: str, index: int) -> Optional[Tuple[str, int, int]]:
    """
    Returns the line of text, the line number, and the character within
    that line for the given absolute index into the given string.
    Newline characters count as the last character on their line. Lines
    and characters are numbered starting from 1.

    Returns `None` for out-of-range indices.

    Examples:

    >>> errorContext('a\\nb\\nc', 0)
    ('a\\n', 1, 1)
    >>> errorContext('a\\nb\\nc', 1)
    ('a\\n', 1, 2)
    >>> errorContext('a\\nbcd\\ne', 2)
    ('bcd\\n', 2, 1)
    >>> errorContext('a\\nbcd\\ne', 3)
    ('bcd\\n', 2, 2)
    >>> errorContext('a\\nbcd\\ne', 4)
    ('bcd\\n', 2, 3)
    >>> errorContext('a\\nbcd\\ne', 5)
    ('bcd\\n', 2, 4)
    >>> errorContext('a\\nbcd\\ne', 6)
    ('e', 3, 1)
    >>> errorContext('a\\nbcd\\ne', -1)
    ('e', 3, 1)
    >>> errorContext('a\\nbcd\\ne', -2)
    ('bcd\\n', 2, 4)
    >>> errorContext('a\\nbcd\\ne', 7) is None
    True
    >>> errorContext('a\\nbcd\\ne', 8) is None
    True
    """
    # Convert negative to positive indices
    if index < 0:
        index = len(string) + index

    # Return None for out-of-range indices
    if not 0 <= index < len(string):
        return None

    # Count lines + look for start-of-line
    line = 1
    lineStart = 0
    for where, char in enumerate(string):
        if where >= index:
            break
        if char == '\n':
            line += 1
            lineStart = where + 1

    try:
        endOfLine = string.index('\n', where)
    except ValueError:
        endOfLine = len(string)

    return (string[lineStart:endOfLine + 1], line, index - lineStart + 1)


class JournalParseWarning(Warning):
    """
    Represents a warning encountered when parsing a journal.
    """
    pass


class PathEllipsis:
    """
    Represents part of a path which has been omitted from a journal and
    which should therefore be inferred.
    """
    pass


#-----------------#
# Parsing manager #
#-----------------#

class ObservationContext(TypedDict):
    """
    The context for an observation, including which context (common or
    active) is being used, which domain we're focused on, which focal
    point is being modified for plural-focalized domains, and which
    decision and transition within the current domain are most relevant
    right now.
    """
    context: base.ContextSpecifier
    domain: base.Domain
    # TODO: Per-domain focus/decision/transitions?
    focus: Optional[base.FocalPointName]
    decision: Optional[base.DecisionID]
    transition: Optional[Tuple[base.DecisionID, base.Transition]]


def observationContext(
    context: base.ContextSpecifier = "active",
    domain: base.Domain = base.DEFAULT_DOMAIN,
    focus: Optional[base.FocalPointName] = None,
    decision: Optional[base.DecisionID] = None,
    transition: Optional[Tuple[base.DecisionID, base.Transition]] = None
) -> ObservationContext:
    """
    Creates a default/empty `ObservationContext`.
    """
    return {
        'context': context,
        'domain': domain,
        'focus': focus,
        'decision': decision,
        'transition': transition
    }


class ObservationPreferences(TypedDict):
    """
    Specifies global preferences for exploration observation. Values are
    either strings or booleans. The keys are:

    - 'reciprocals': A boolean specifying whether transitions should
        come with reciprocals by default. Normally this is `True`, but
        it can be set to `False` instead.
        TODO: implement this.
    """
    reciprocals: bool


def observationPreferences(
    reciprocals=True
) -> ObservationPreferences:
    """
    Creates an observation preferences dictionary, using default values
    for any preferences not specified as arguments.
    """
    return {
        'reciprocals': reciprocals
    }


class JournalObserver:
    """
    Keeps track of extra state needed when parsing a journal in order to
    produce a `core.DiscreteExploration` object. The methods of this
    class act as an API for constructing explorations that have several
    special properties. The API is designed to allow journal entries
    (which represent specific observations/events during an exploration)
    to be directly accumulated into an exploration object, including
    entries which apply to things like the most-recent-decision or
    -transition.

    You can use the `convertJournal` function to handle things instead,
    since that function creates and manages a `JournalObserver` object
    for you.

    The basic usage is as follows:

    1. Create a `JournalObserver`, optionally specifying a custom
        `ParseFormat`.
    2. Repeatedly either:
        * Call `record*` API methods corresponding to specific entries
            observed or...
        * Call `JournalObserver.observe` to parse one or more
            journal blocks from a string and call the appropriate
            methods automatically.
    3. Call `JournalObserver.getExploration` to retrieve the
        `core.DiscreteExploration` object that's been created.

    You can just call `convertJournal` to do all of these things at
    once.

    Notes:

    - `JournalObserver.getExploration` may be called at any time to get
        the exploration object constructed so far, and that that object
        (unless it's `None`) will always be the same object (which gets
        modified as entries are recorded). Modifying this object
        directly is possible for making changes not available via the
        API, but must be done carefully, as there are important
        conventions around things like decision names that must be
        respected if the API functions need to keep working.
    - To get the latest graph or state, simply use the
        `core.DiscreteExploration.getSituation()` method of the
        `JournalObserver.getExploration` result.

    ## Examples

    >>> obs = JournalObserver()
    >>> e = obs.getExploration()
    >>> len(e) # blank starting state
    1
    >>> e.getActiveDecisions(0) # no active decisions before starting
    set()
    >>> obs.definiteDecisionTarget()
    Traceback (most recent call last):
    ...
    exploration.core.MissingDecisionError...
    >>> obs.currentDecisionTarget() is None
    True
    >>> # We start by using the record* methods...
    >>> obs.recordStart("Start")
    >>> obs.definiteDecisionTarget()
    0
    >>> obs.recordObserve("bottom")
    >>> obs.definiteDecisionTarget()
    0
    >>> len(e) # blank + started states
    2
    >>> e.getActiveDecisions(1)
    {0}
    >>> obs.recordExplore("left", "West", "right")
    >>> obs.definiteDecisionTarget()
    2
    >>> len(e) # starting states + one step
    3
    >>> e.getActiveDecisions(1)
    {0}
    >>> e.movementAtStep(1)
    (0, 'left', 2)
    >>> e.getActiveDecisions(2)
    {2}
    >>> e.getActiveDecisions()
    {2}
    >>> e.getSituation().graph.nameFor(list(e.getActiveDecisions())[0])
    'West'
    >>> obs.recordRetrace("right")
    >>> obs.definiteDecisionTarget()
    0
    >>> len(e) # starting states + two steps
    4
    >>> e.getActiveDecisions(1)
    {0}
    >>> e.movementAtStep(1)
    (0, 'left', 2)
    >>> e.getActiveDecisions(2)
    {2}
    >>> e.movementAtStep(2)
    (2, 'right', 0)
    >>> e.getActiveDecisions(3)
    {0}
    >>> obs.recordRetrace("bad") # transition doesn't exist
    Traceback (most recent call last):
    ...
    exploration.core.MissingTransitionError...
    >>> obs.definiteDecisionTarget()
    0
    >>> obs.recordObserve('right', 'East', 'left')
    >>> e.getSituation().graph.getTransitionRequirement('Start', 'right')
    ReqNothing()
    >>> obs.recordRequirement('crawl|small')
    >>> e.getSituation().graph.getTransitionRequirement('Start', 'right')
    ReqAny([ReqCapability('crawl'), ReqCapability('small')])
    >>> obs.definiteDecisionTarget()
    0
    >>> obs.currentTransitionTarget()
    (0, 'right')
    >>> obs.currentReciprocalTarget()
    (3, 'left')
    >>> # The use of relative mode to add remote observations
    >>> obs.relative('East')
    >>> obs.definiteDecisionTarget()
    3
    >>> obs.recordObserve('top_vent')
    >>> obs.recordRequirement('crawl')
    >>> obs.recordReciprocalRequirement('crawl')
    >>> obs.recordExplore('right_door', 'Outside', 'left_door')
    >>> obs.definiteDecisionTarget()
    5
    >>> obs.recordRequirement('X')
    >>> obs.recordReciprocalRequirement('X')
    >>> obs.recordAction('lever') # no info on what it does yet...
    >>> # TODO door-toggling lever example
    >>> obs.definiteDecisionTarget()
    5
    >>> obs.relative() # leave relative mode
    >>> len(e) # starting states + two steps, no steps happen in relative mode
    4
    >>> obs.definiteDecisionTarget()
    0
    >>> g = e.getSituation().graph
    >>> g.getTransitionRequirement(
    ...     g.getDestination('East', 'top_vent'),
    ...     'return'
    ... )
    ReqCapability('crawl')
    >>> g.getTransitionRequirement('East', 'top_vent')
    ReqCapability('crawl')
    >>> g.getTransitionRequirement('East', 'right_door')
    ReqImpossible()
    >>> g.getTransitionRequirement('Outside', 'left_door')
    ReqImpossible()
    >>> # Now we demonstrate the use of "observe"
    >>> e.getActiveDecisions()
    {0}
    >>> g.destinationsFrom(0)
    {'bottom': 1, 'left': 2, 'right': 3}
    >>> g.getDecision('Attic') is None
    True
    >>> obs.definiteDecisionTarget()
    0
    >>> obs.observe("\
o up Attic down\\n\
x up\\n\
o vent\\n\
q crawl")
    >>> g = e.getSituation().graph
    >>> g.destinationsFrom(0)
    {'bottom': 1, 'left': 2, 'right': 3, 'up': 6}
    >>> g.nameFor(list(e.getActiveDecisions())[0])
    'Attic'
    >>> g.getTransitionRequirement('Attic', 'vent')
    ReqCapability('crawl')
    >>> sorted(list(g.destinationsFrom('Attic').items()))
    [('down', 0), ('vent', 7)]
    >>> obs.observe("a getCrawl\\nAt gain crawl\\nr vent East top_vent")
    >>> g = e.getSituation().graph
    >>> g.getTransitionRequirement('East', 'top_vent')
    ReqCapability('crawl')
    >>> g.nameFor(g.getDestination('Attic', 'vent'))
    'East'
    >>> g.nameFor(g.getDestination('East', 'top_vent'))
    'Attic'
    >>> len(e) # exploration, action, and return are each 1
    7
    >>> e.getActiveDecisions(3)
    {0}
    >>> e.movementAtStep(3)
    (0, 'up', 6)
    >>> e.getActiveDecisions(4)
    {6}
    >>> g.nameFor(list(e.getActiveDecisions(4))[0])
    'Attic'
    >>> e.movementAtStep(4)
    (6, 'getCrawl', 6)
    >>> g.nameFor(list(e.getActiveDecisions(5))[0])
    'Attic'
    >>> e.movementAtStep(5)
    (6, 'vent', 3)
    >>> g.nameFor(list(e.getActiveDecisions(6))[0])
    'East'
    >>> # TODO: Extend example to: pull lever and observe it opens the door

    An example of the use of `recordUnify` and `recordObviate`.

    >>> obs = JournalObserver()
    >>> obs.observe('''
    ... S start
    ... x right hall left
    ... x right room left
    ... x vent vents right_vent
    ... ''')
    >>> obs.recordObviate('middle_vent', 'hall', 'vent')
    >>> obs.recordExplore('left_vent', 'new_room', 'vent')
    >>> obs.recordUnify('start')
    >>> e = obs.getExploration()
    >>> len(e)
    6
    >>> e.getActiveDecisions(0)
    set()
    >>> [
    ...     e.getSituation(n).graph.nameFor(list(e.getActiveDecisions(n))[0])
    ...     for n in range(1, 6)
    ... ]
    ['start', 'hall', 'room', 'vents', 'start']
    >>> g = e.getSituation().graph
    >>> g.getDestination('start', 'vent')
    3
    >>> g.getDestination('vents', 'left_vent')
    0
    >>> g.getReciprocal('start', 'vent')
    'left_vent'
    >>> g.getReciprocal('vents', 'left_vent')
    'vent'
    >>> 'new_room' in g
    False
    """

    parseFormat: JournalParseFormat
    """
    The parse format used to parse entries supplied as text. This also
    ends up controlling some of the decision and transition naming
    conventions that are followed, so it is not safe to change it
    mid-journal; it should be set once before observation begins, and
    may be accessed but should not be changed.
    """

    exploration: core.DiscreteExploration
    """
    This is the exploration object being built via journal observations.
    Note that the exploration object may be empty (i.e., have length 0)
    even after the first few entries have been recorded because in some
    cases entries are ambiguous and are not translated into exploration
    steps until a further entry resolves that ambiguity.
    """

    preferences: ObservationPreferences
    """
    Preferences for the observation mechanisms. See
    `ObservationPreferences`.
    """

    uniqueNumber: int
    """
    A unique number to be substituted (prefixed with '_') into
    underscore-substitutions within aliases. Will be incremented for each
    such substitution.
    """

    aliases: Dict[str, Tuple[List[str], str]]
    """
    The defined aliases for this observer. Each alias has a name, and
    stored under that name is a list of parameters followed by a
    commands string.
    """

    def __init__(self, parseFormat: Optional[JournalParseFormat] = None):
        """
        Sets up the observer. If a parse format is supplied, that will
        be used instead of the default parse format, which is just the
        result of creating a `ParseFormat` with default arguments.

        A simple example:

        >>> o = JournalObserver()
        >>> o.recordStart('hi')
        >>> e = o.getExploration()
        >>> len(e)
        2
        >>> g = e.getSituation().graph
        >>> len(g)
        1
        >>> e.getActiveContext()
        {\
'capabilities': {'capabilities': set(), 'tokens': {}, 'skills': {}},\
 'focalization': {'main': 'singular'},\
 'activeDomains': {'main'},\
 'activeDecisions': {'main': 0}\
}
        >>> list(g.nodes)[0]
        0
        >>> o.recordObserve('option')
        >>> list(g.nodes)
        [0, 1]
        >>> [g.nameFor(d) for d in g.nodes]
        ['hi', '_u.0']
        >>> o.recordZone(0, 'Lower')
        >>> [g.nameFor(d) for d in g.nodes]
        ['hi', '_u.0']
        >>> e.getActiveDecisions()
        {0}
        >>> o.recordZone(1, 'Upper')
        >>> o.recordExplore('option', 'bye', 'back')
        >>> g = e.getSituation().graph
        >>> [g.nameFor(d) for d in g.nodes]
        ['hi', 'bye']
        >>> o.recordObserve('option2')
        >>> import pytest
        >>> oldWarn = core.WARN_OF_NAME_COLLISIONS
        >>> core.WARN_OF_NAME_COLLISIONS = True
        >>> try:
        ...     with pytest.warns(core.DecisionCollisionWarning):
        ...         o.recordExplore('option2', 'Lower2::hi', 'back')
        ... finally:
        ...     core.WARN_OF_NAME_COLLISIONS = oldWarn
        >>> g = e.getSituation().graph
        >>> [g.nameFor(d) for d in g.nodes]
        ['hi', 'bye', 'hi']
        >>> # Prefix must be specified because it's ambiguous
        >>> o.recordWarp('Lower::hi')
        >>> g = e.getSituation().graph
        >>> [(d, g.nameFor(d)) for d in g.nodes]
        [(0, 'hi'), (1, 'bye'), (2, 'hi')]
        >>> e.getActiveDecisions()
        {0}
        >>> o.recordWarp('bye')
        >>> g = e.getSituation().graph
        >>> [(d, g.nameFor(d)) for d in g.nodes]
        [(0, 'hi'), (1, 'bye'), (2, 'hi')]
        >>> e.getActiveDecisions()
        {1}
        """
        if parseFormat is None:
            self.parseFormat = JournalParseFormat()
        else:
            self.parseFormat = parseFormat

        self.uniqueNumber = 0
        self.aliases = {}

        # Set up default observation preferences
        self.preferences = observationPreferences()

        # Create a blank exploration
        self.exploration = core.DiscreteExploration()

        # Debugging support
        self.prevSteps: Optional[int] = None
        self.prevDecisions: Optional[int] = None

        # Current context tracking focal context, domain, focus point,
        # decision, and/or transition that's currently most relevant:
        self.context = observationContext()

        # TODO: Stack of contexts?
        # Stored observation context can be restored as the current
        # state later. This is used to support relative mode.
        self.storedContext: Optional[
            ObservationContext
        ] = None

        # Whether or not we're in relative mode.
        self.inRelativeMode = False

    def getExploration(self) -> core.DiscreteExploration:
        """
        Returns the exploration that this observer edits.
        """
        return self.exploration

    def nextUniqueName(self) -> str:
        """
        Returns the next unique name for this observer, which is just an
        underscore followed by an integer. This increments
        `uniqueNumber`.
        """
        result = '_' + str(self.uniqueNumber)
        self.uniqueNumber += 1
        return result

    def currentDecisionTarget(self) -> Optional[base.DecisionID]:
        """
        Returns the decision which decision-based changes should be
        applied to. Changes depending on whether relative mode is
        active. Will be `None` when there is no current position (e.g.,
        before the exploration is started).
        """
        return self.context['decision']

    def definiteDecisionTarget(self) -> base.DecisionID:
        """
        Works like `currentDecisionTarget` but raises a
        `core.MissingDecisionError` instead of returning `None` if there
        is no current decision.
        """
        result = self.currentDecisionTarget()

        if result is None:
            raise core.MissingDecisionError("There is no current decision.")
        else:
            return result

    def currentTransitionTarget(
        self
    ) -> Optional[Tuple[base.DecisionID, base.Transition]]:
        """
        Returns the decision, transition pair that identifies the current
        transition which transition-based changes should apply to. Will
        be `None` when there is no current transition (e.g., just after a
        warp).
        """
        decision = self.context['decision']
        transition = self.context['transition']
        if decision is None or transition is None:
            return None
        else:
            return transition

    def currentReciprocalTarget(
        self
    ) -> Optional[Tuple[base.DecisionID, base.Transition]]:
        """
        Returns the decision, transition pair that identifies the
        reciprocal of the `currentTransitionTarget`. Will be `None` when
        there is no current transition, or when the current transition
        doesn't have a reciprocal (e.g., after an ending).
        """
        # relative mode is handled by `currentTransitionTarget`
        target = self.currentTransitionTarget()
        if target is None:
            return None
        return self.exploration.getSituation().graph.getReciprocalPair(
            *target
        )

    def checkFormat(
        self,
        entryType: str,
        target: Union[None, JournalTargetType, int],
        pieces: List[str],
        expectedTargets: Union[
            None,
            type[int],
            Collection[
                Union[None, JournalTargetType, int]
            ]
        ],
        expectedPieces: Union[None, int, Collection[int]]
    ) -> None:
        """
        Does format checking for a journal entry after
        `determineEntryType` is called. Checks that the target is one
        from an allowed list of targets (or is `None` if
        `expectedTargets` is set to `None`) and that the number of
        pieces of content is a specific number or within a specific
        collection of allowed numbers. If `expectedPieces` is set to
        None, there is no restriction on the number of pieces.

        Raises a `JournalParseError` if its expectations are violated.
        """
        if expectedTargets is None:
            if target is not None:
                raise JournalParseError(
                    f"{entryType} entry may not specify a target."
                )
        elif expectedTargets is int:
            if not isinstance(target, int):
                raise JournalParseError(
                    f"{entryType} entry must have an integer target."
                )
        elif target not in cast(
            Collection[
                Union[None, JournalTargetType, int]
            ],
            expectedTargets
        ):
            raise JournalParseError(
                f"{entryType} entry had invalid target '{target}'."
            )

        if expectedPieces is None:
            # No restriction
            pass
        elif isinstance(expectedPieces, int):
            if len(pieces) != expectedPieces:
                raise JournalParseError(
                    f"{entryType} entry had {len(pieces)} arguments but"
                    f" only {expectedPieces} argument(s) is/are allowed."
                )

        elif len(pieces) not in expectedPieces:
            allowed = ', '.join(str(x) for x in expectedPieces)
            raise JournalParseError(
                f"{entryType} entry had {len(pieces)} arguments but the"
                f" allowed argument counts are: {allowed}"
            )

    def parseOneCommand(
        self,
        journalText: str,
        startIndex: int
    ) -> Tuple[List[str], int]:
        """
        Parses a single command from the given journal text, starting at
        the specified start index. Each command occupies a single line,
        except when blocks are present in which case it may stretch
        across multiple lines. This function splits the command up into a
        list of strings (including multi-line strings and/or strings
        with spaces in them when blocks are used). It returns that list
        of strings, along with the index after the newline at the end of
        the command it parsed (which could be used as the start index
        for the next command). If the command has no newline after it
        (only possible when the string ends) the returned index will be
        the length of the string.

        If the line starting with the start character is empty (or just
        contains spaces), the result will be an empty list along with the
        index for the start of the next line.

        Examples:

        >>> o = JournalObserver()
        >>> commands = '''\\
        ... S start
        ... o option
        ...
        ... x option next back
        ... o lever
        ...   e edit [
        ...     o bridge
        ...       q speed
        ...   ] [
        ...     o bridge
        ...       q X
        ...   ]
        ... a lever
        ... '''
        >>> o.parseOneCommand(commands, 0)
        (['S', 'start'], 8)
        >>> o.parseOneCommand(commands, 8)
        (['o', 'option'], 17)
        >>> o.parseOneCommand(commands, 17)
        ([], 18)
        >>> o.parseOneCommand(commands, 18)
        (['x', 'option', 'next', 'back'], 37)
        >>> o.parseOneCommand(commands, 37)
        (['o', 'lever'], 45)
        >>> bits, end = o.parseOneCommand(commands, 45)
        >>> bits[:2]
        ['e', 'edit']
        >>> bits[2]
        'o bridge\\n      q speed'
        >>> bits[3]
        'o bridge\\n      q X'
        >>> len(bits)
        4
        >>> end
        116
        >>> o.parseOneCommand(commands, end)
        (['a', 'lever'], 124)

        >>> o = JournalObserver()
        >>> s = "o up Attic down\\nx up\\no vent\\nq crawl"
        >>> o.parseOneCommand(s, 0)
        (['o', 'up', 'Attic', 'down'], 16)
        >>> o.parseOneCommand(s, 16)
        (['x', 'up'], 21)
        >>> o.parseOneCommand(s, 21)
        (['o', 'vent'], 28)
        >>> o.parseOneCommand(s, 28)
        (['q', 'crawl'], 35)
        """

        index = startIndex
        unit: Optional[str] = None
        bits: List[str] = []
        pf = self.parseFormat  # shortcut variable
        while index < len(journalText):
            char = journalText[index]
            if char.isspace():
                # Space after non-spaces -> end of unit
                if unit is not None:
                    bits.append(unit)
                    unit = None
                # End of line -> end of command
                if char == '\n':
                    index += 1
                    break
            else:
                # Non-space -> check for block
                if char == pf.blockStart:
                    if unit is not None:
                        bits.append(unit)
                        unit = None
                    blockEnd = pf.findBlockEnd(journalText, index)
                    block = journalText[index + 1:blockEnd - 1].strip()
                    bits.append(block)
                    index = blockEnd  # +1 added below
                elif unit is None:  # Initial non-space -> start of unit
                    unit = char
                else:  # Continuing non-space -> accumulate
                    unit += char
            # Increment index
            index += 1

        # Grab final unit if there is one hanging
        if unit is not None:
            bits.append(unit)

        return (bits, index)

    def observe(self, journalText: str) -> None:
        """
        Ingests one or more journal blocks in text format (as a
        multi-line string) and updates the exploration being built by
        this observer, as well as updating internal state.

        This method can be called multiple times to process a longer
        journal incrementally including line-by-line.

        ## Example:

        >>> obs = JournalObserver()
        >>> oldWarn = core.WARN_OF_NAME_COLLISIONS
        >>> try:
        ...     obs.observe('''\\
        ... S Room1::start
        ... zz Region
        ... o nope
        ...   q power|tokens*3
        ... o unexplored
        ... o onwards
        ... x onwards sub_room backwards
        ... t backwards
        ... o down
        ...
        ... x down Room2::middle up
        ... a box
        ...   At deactivate
        ...   At gain tokens*1
        ... o left
        ... o right
        ...   gt blue
        ...
        ... x right Room3::middle left
        ... o right
        ... a miniboss
        ...   At deactivate
        ...   At gain power
        ... x right - left
        ... o ledge
        ...   q tall
        ... t left
        ... t left
        ... t up
        ...
        ... x nope secret back
        ... ''')
        ... finally:
        ...     core.WARN_OF_NAME_COLLISIONS = oldWarn
        >>> e = obs.getExploration()
        >>> len(e)
        13
        >>> g = e.getSituation().graph
        >>> len(g)
        9
        >>> def showDestinations(g, r):
        ...     if isinstance(r, str):
        ...         r = obs.parseFormat.parseDecisionSpecifier(r)
        ...     d = g.destinationsFrom(r)
        ...     for outgoing in sorted(d):
        ...         req = g.getTransitionRequirement(r, outgoing)
        ...         if req is None or req == base.ReqNothing():
        ...             req = ''
        ...         else:
        ...             req = ' ' + repr(req)
        ...         print(outgoing, g.identityOf(d[outgoing]) + req)
        ...
        >>> "start" in g
        False
        >>> showDestinations(g, "Room1::start")
        down 4 (Room2::middle)
        nope 1 (Room1::secret) ReqAny([ReqCapability('power'),\
 ReqTokens('tokens', 3)])
        onwards 3 (Room1::sub_room)
        unexplored 2 (_u.1)
        >>> showDestinations(g, "Room1::secret")
        back 0 (Room1::start)
        >>> showDestinations(g, "Room1::sub_room")
        backwards 0 (Room1::start)
        >>> showDestinations(g, "Room2::middle")
        box 4 (Room2::middle)
        left 5 (_u.4)
        right 6 (Room3::middle)
        up 0 (Room1::start)
        >>> g.transitionTags(4, "right")
        {'blue': 1}
        >>> showDestinations(g, "Room3::middle")
        left 4 (Room2::middle)
        miniboss 6 (Room3::middle)
        right 7 (Room3::-)
        >>> showDestinations(g, "Room3::-")
        ledge 8 (_u.7) ReqCapability('tall')
        left 6 (Room3::middle)
        >>> showDestinations(g, "_u.7")
        return 7 (Room3::-)
        >>> e.getActiveDecisions()
        {1}
        >>> g.identityOf(1)
        '1 (Room1::secret)'

        Note that there are plenty of other annotations not shown in
        this example; see `DEFAULT_FORMAT` for the default mapping from
        journal entry types to markers, and see `JournalEntryType` for
        the explanation for each entry type.

        Most entries start with a marker (which includes one character
        for the type and possibly one for the target) followed by a
        single space, and everything after that is the content of the
        entry.
        """
        # Normalize newlines
        journalText = journalText\
            .replace('\r\n', '\n')\
            .replace('\n\r', '\n')\
            .replace('\r', '\n')

        # Shortcut variable
        pf = self.parseFormat

        # Remove comments from entire text
        journalText = pf.removeComments(journalText)

        startAt = 0
        currentStartPos = 0
        try:
            while startAt < len(journalText):
                currentStartPos = startAt
                bits, startAt = self.parseOneCommand(journalText, startAt)

                if len(bits) == 0:
                    continue

                eType, eTarget, eParts = pf.determineEntryType(bits)
                if eType == 'preference':
                    self.checkFormat(
                        'preference',
                        eTarget,
                        eParts,
                        None,
                        2
                    )
                    pref = eParts[0]
                    opAnn = ObservationPreferences.__annotations__
                    if pref not in opAnn:
                        raise JournalParseError(
                            f"Invalid preference name '{pref}'."
                        )

                    prefVal: Union[None, str, bool]
                    if opAnn[pref] is bool:
                        prefVal = pf.onOff(eParts[1])
                        if prefVal is None:
                            warnings.warn(
                                (
                                    f"On/off value '{eParts[1]}' is"
                                    f" neither '{pf.markerFor('on')}'"
                                    f" nor '{pf.markerFor('off')}'."
                                    f" Assuming 'off'."
                                ),
                                JournalParseWarning
                            )
                    else:  # we assume it's a string
                        assert opAnn[pref] is str
                        prefVal = eParts[1]

                    # Set the preference value (type checked above)
                    self.preferences[pref] = prefVal  # type: ignore [literal-required] # noqa: E501

                elif eType == 'alias':
                    self.checkFormat(
                        "alias",
                        eTarget,
                        eParts,
                        None,
                        None
                    )

                    if len(eParts) < 2:
                        raise JournalParseError(
                            "Alias entry must include at least an alias"
                            " name and a commands list."
                        )
                    aliasName = eParts[0]
                    parameters = eParts[1:-1]
                    commands = eParts[-1]
                    self.defineAlias(aliasName, parameters, commands)

                elif eType == 'custom':
                    self.checkFormat(
                        "custom",
                        eTarget,
                        eParts,
                        None,
                        None
                    )
                    if len(eParts) == 0:
                        raise JournalParseError(
                            "Custom entry must include at least an alias"
                            " name."
                        )
                    self.deployAlias(eParts[0], eParts[1:])

                elif eType == 'DEBUG':
                    self.checkFormat(
                        "DEBUG",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.doDebug(*cast(List[DebugAction], eParts))

                elif eType == 'START':
                    self.checkFormat(
                        "START",
                        eTarget,
                        eParts,
                        None,
                        1
                    )

                    where = pf.parseDecisionSpecifier(eParts[0])
                    if isinstance(where, base.DecisionID):
                        raise JournalParseError(
                            f"Can't use {repr(where)} as a start"
                            f" because the start must be a decision"
                            f" name, not a decision ID."
                        )
                    self.recordStart(where)

                elif eType == 'explore':
                    self.checkFormat(
                        "explore",
                        eTarget,
                        eParts,
                        None,
                        {1, 2, 3}
                    )

                    if len(eParts) == 1:
                        self.recordExplore(eParts[0])
                    elif len(eParts) == 2:
                        destination = pf.parseDecisionSpecifier(eParts[1])
                        self.recordExplore(eParts[0], destination)
                    else:
                        destination = pf.parseDecisionSpecifier(eParts[1])
                        self.recordExplore(eParts[0], destination, eParts[2])

                elif eType == 'return':
                    self.checkFormat(
                        "return",
                        eTarget,
                        eParts,
                        None,
                        {2, 3}
                    )
                    destination = pf.parseDecisionSpecifier(eParts[1])
                    self.recordReturn(
                        eParts[0],
                        destination,
                        eParts[2] if len(eParts) > 2 else None
                    )

                elif eType == 'action':
                    self.checkFormat(
                        "action",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.recordAction(eParts[0])

                elif eType == 'retrace':
                    self.checkFormat(
                        "retrace",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.recordRetrace(eParts[0])

                elif eType == 'warp':
                    self.checkFormat(
                        "warp",
                        eTarget,
                        eParts,
                        None,
                        {1}
                    )

                    destination = pf.parseDecisionSpecifier(eParts[1])
                    self.recordWarp(destination)

                elif eType == 'wait':
                    self.checkFormat(
                        "wait",
                        eTarget,
                        eParts,
                        None,
                        0
                    )
                    self.recordWait()

                elif eType == 'observe':
                    self.checkFormat(
                        "observe",
                        eTarget,
                        eParts,
                        (None, 'actionPart'),
                        (1, 2, 3)
                    )
                    if eTarget is None:
                        self.recordObserve(*eParts)
                    else:
                        if len(eParts) > 1:
                            raise JournalParseError(
                                f"Observing action '{eParts[0]}' at"
                                f" '{self.definiteDecisionTarget()}':"
                                f" neither a destination nor a"
                                f" reciprocal may be specified when"
                                f" observing an action (did you mean to"
                                f" observe a transition?)."
                            )
                        self.recordObserveAction(*eParts)

                elif eType == 'END':
                    self.checkFormat(
                        "END",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.recordEnd(*eParts)

                elif eType == 'requirement':
                    self.checkFormat(
                        "requirement",
                        eTarget,
                        eParts,
                        (None, 'reciprocalPart', 'bothPart'),
                        None
                    )
                    req = pf.parseRequirement(' '.join(eParts))
                    if eTarget in (None, 'bothPart'):
                        self.recordRequirement(req)
                    if eTarget in ('reciprocalPart', 'bothPart'):
                        self.recordReciprocalRequirement(req)

                elif eType == 'effect':
                    self.checkFormat(
                        "effect",
                        eTarget,
                        eParts,
                        None,
                        None
                    )

                    consequence: base.Consequence
                    try:
                        consequence = pf.parseConsequence(' '.join(eParts))
                    except parsing.ParseError:
                        consequence = [pf.parseEffect(' '.join(eParts))]

                    self.recordTransitionConsequence(consequence)

                elif eType == 'apply':
                    self.checkFormat(
                        "apply",
                        eTarget,
                        eParts,
                        (None, 'transitionPart'),
                        None
                    )

                    toApply: base.Consequence
                    try:
                        toApply = pf.parseConsequence(' '.join(eParts))
                    except parsing.ParseError:
                        toApply = [pf.parseEffect(' '.join(eParts))]

                    # If we targeted a transition, that means we wanted
                    # to both apply the consequence now AND set it up as
                    # an consequence of the transition we just took.
                    if eTarget == 'transitionPart':
                        if self.context['transition'] is None:
                            raise JournalParseError(
                                "Can't apply a consequence to a"
                                " transition here because there is no"
                                " current relevant transition."
                            )
                        # We need to apply these consequences as part of
                        # the transition so their trigger count will be
                        # tracked properly, but we do not want to
                        # re-apply the other parts of the consequence.
                        self.recordAdditionalTransitionConsequence(
                            toApply
                        )
                    else:
                        # Otherwise just apply the consequence
                        self.exploration.applyExtraneousConsequence(
                            toApply,
                            self.context['transition']
                        )

                elif eType == 'tag':
                    self.checkFormat(
                        "tag",
                        eTarget,
                        eParts,
                        (
                            None,
                            'decisionPart',
                            'transitionPart',
                            'reciprocalPart',
                            'bothPart'
                        ),
                        None
                    )
                    tag: base.Tag
                    value: base.TagValue
                    if len(eParts) == 0:
                        raise JournalParseError(
                            "tag entry must include at least a tag name."
                        )
                    elif len(eParts) == 1:
                        tag = eParts[0]
                        value = 1
                    elif len(eParts) == 2:
                        tag, value = eParts
                        if value == 'True':
                            value = True
                        elif value == 'False':
                            value = False
                        elif value == 'None':
                            value = None
                        else:
                            try:
                                value = int(value)
                            except ValueError:
                                try:
                                    value = float(value)
                                except ValueError:
                                    pass
                    else:
                        raise JournalParseError(
                            f"tag entry has too many parts (only a tag"
                            f" name and a tag value are allowed). Got:"
                            f" {eParts}"
                        )

                    if eTarget in (None, "decisionPart"):
                        self.recordTagDecision(tag, value)
                    elif eTarget == "transitionPart":
                        self.recordTagTranstion(tag, value)
                    elif eTarget == "reciprocalPart":
                        self.recordTagReciprocal(tag, value)
                    elif eTarget == "bothPart":
                        self.recordTagTranstion(tag, value)
                        self.recordTagReciprocal(tag, value)
                    else:
                        raise JournalParseError(
                            f"Invalid tag target type '{eTarget}'."
                        )

                elif eType == 'annotate':
                    self.checkFormat(
                        "annotate",
                        eTarget,
                        eParts,
                        (
                            None,
                            'decisionPart',
                            'transitionPart',
                            'reciprocalPart',
                            'bothPart'
                        ),
                        None
                    )
                    if len(eParts) == 0:
                        raise JournalParseError(
                            "annotation may not be empty."
                        )
                    if eTarget is None:
                        self.recordAnnotateStep(' '.join(eParts))
                    elif eTarget == "decisionPart":
                        self.recordAnnotateDecision(' '.join(eParts))
                    elif eTarget == "transitionPart":
                        self.recordAnnotateTranstion(' '.join(eParts))
                    elif eTarget == "reciprocalPart":
                        self.recordAnnotateReciprocal(' '.join(eParts))
                    elif eTarget == "bothPart":
                        self.recordAnnotateTranstion(' '.join(eParts))
                        self.recordAnnotateReciprocal(' '.join(eParts))
                    else:
                        raise JournalParseError(
                            f"Invalid annotation target type '{eTarget}'."
                        )

                elif eType == 'context':
                    self.checkFormat(
                        "context",
                        eTarget,
                        eParts,
                        int,
                        1
                    )
                    if eParts[0] == pf.markerFor('commonContext'):
                        self.recordContextSwap(None)
                    else:
                        self.recordContextSwap(eParts[0])

                elif eType == 'domain':
                    self.checkFormat(
                        "domain",
                        eTarget,
                        eParts,
                        int,
                        {1, 2, 3}
                    )
                    inCommon = False
                    if eParts[-1] == pf.markerFor('commonContext'):
                        eParts = eParts[:-1]
                        inCommon = True
                    if len(eParts) == 3:
                        raise JournalParseError(
                            f"A domain entry may only have 1 or 2"
                            f" arguments unless the last argument is"
                            f" {repr(pf.markerFor('commonContext'))}"
                        )
                    elif len(eParts) == 2:
                        if eParts[0] == pf.markerFor('exclusiveDomain'):
                            self.recordDomainFocus(
                                eParts[1],
                                exclusive=True,
                                inCommon=inCommon
                            )
                        elif eParts[0] == pf.markerFor('notApplicable'):
                            # Deactivate the domain
                            self.recordDomainUnfocus(
                                eParts[1],
                                inCommon=inCommon
                            )
                        else:
                            # Set up new domain w/ given focalization
                            focalization = pf.parseFocalization(eParts[1])
                            self.recordNewDomain(
                                eParts[0],
                                focalization,
                                inCommon=inCommon
                            )
                    else:
                        # Focus the domain (or possibly create it)
                        self.recordDomainFocus(
                            eParts[0],
                            inCommon=inCommon
                        )

                elif eType == 'focus':
                    self.checkFormat(
                        "focus",
                        eTarget,
                        eParts,
                        int,
                        {1, 2}
                    )
                    if len(eParts) == 2:  # explicit domain
                        self.recordFocusOn(eParts[1], eParts[0])
                    else:  # implicit domain
                        self.recordFocusOn(eParts[0])

                elif eType == 'zone':
                    self.checkFormat(
                        "zone",
                        eTarget,
                        eParts,
                        int,
                        1
                    )
                    if eTarget is None:
                        eTarget = 0
                    self.recordZone(cast(int, eTarget), eParts[0])

                elif eType == 'unify':
                    self.checkFormat(
                        "unify",
                        eTarget,
                        eParts,
                        (None, 'transitionPart', 'reciprocalPart'),
                        (1, 2)
                    )
                    if eTarget is None:
                        decisions = [
                            pf.parseDecisionSpecifier(p)
                            for p in eParts
                        ]
                        self.recordUnify(*decisions)
                    elif eTarget == 'transitionPart':
                        if len(eParts) != 1:
                            raise JournalParseError(
                                "A transition unification entry may only"
                                f" have one argument, but we got"
                                f" {len(eParts)}."
                            )
                        self.recordUnifyTransition(eParts[0])
                    elif eTarget == 'reciprocalPart':
                        if len(eParts) != 1:
                            raise JournalParseError(
                                "A transition unification entry may only"
                                f" have one argument, but we got"
                                f" {len(eParts)}."
                            )
                        self.recordUnifyReciprocal(eParts[0])
                    else:
                        raise RuntimeError(
                            f"Invalid target type {eTarget} after check"
                            f" for unify entry!"
                        )

                elif eType == 'obviate':
                    self.checkFormat(
                        "obviate",
                        eTarget,
                        eParts,
                        None,
                        3
                    )
                    transition, targetDecision, targetTransition = eParts
                    self.recordObviate(
                        transition,
                        pf.parseDecisionSpecifier(targetDecision),
                        targetTransition
                    )

                elif eType == 'extinguish':
                    self.checkFormat(
                        "extinguish",
                        eTarget,
                        eParts,
                        (
                            None,
                            'decisionPart',
                            'transitionPart',
                            'reciprocalPart',
                            'bothPart'
                        ),
                        1
                    )
                    if eTarget is None:
                        eTarget = 'bothPart'
                    if eTarget == 'decisionPart':
                        self.recordExtinguishDecision(
                            pf.parseDecisionSpecifier(eParts[0])
                        )
                    elif eTarget == 'transitionPart':
                        transition = eParts[0]
                        here = self.definiteDecisionTarget()
                        self.recordExtinguishTransition(
                            here,
                            transition,
                            False
                        )
                    elif eTarget == 'bothPart':
                        transition = eParts[0]
                        here = self.definiteDecisionTarget()
                        self.recordExtinguishTransition(
                            here,
                            transition,
                            True
                        )
                    else:  # Must be reciprocalPart
                        transition = eParts[0]
                        here = self.definiteDecisionTarget()
                        now = self.exploration.getSituation()
                        rPair = now.graph.getReciprocalPair(here, transition)
                        if rPair is None:
                            raise JournalParseError(
                                f"Attempted to extinguish the"
                                f" reciprocal of transition"
                                f" '{transition}' which "
                                f" has no reciprocal (or which"
                                f" doesn't exist from decision"
                                f" '{here}')."
                            )

                        self.recordExtinguishTransition(
                            rPair[0],
                            rPair[1],
                            deleteReciprocal=False
                        )

                elif eType == 'complicate':
                    # TODO: Complication of decisions to split them?
                    # (but how would we specify which incoming transitions
                    # to connect to which part?)
                    self.checkFormat(
                        "complicate",
                        eTarget,
                        eParts,
                        None,
                        4
                    )
                    target, newName, newReciprocal, newRR = eParts
                    self.recordComplicate(
                        target,
                        newName,
                        newReciprocal,
                        newRR
                    )

                elif eType == 'fulfills':
                    self.checkFormat(
                        "fulfills",
                        eTarget,
                        eParts,
                        None,
                        2
                    )
                    self.recordFulfills(*eParts)

                elif eType == 'relative':
                    self.checkFormat(
                        "relative",
                        eTarget,
                        eParts,
                        None,
                        (0, 1, 2)
                    )
                    try:
                        if (
                            len(eParts) > 0
                        and eParts[0] == self.parseFormat.markerFor(
                                'relative'
                            )
                        ):
                            self.relative(None, *eParts[1:])
                        else:
                            self.relative(*eParts)
                    except core.BadStart:
                        raise JournalParseError(
                            "You cannot enter relative mode before the"
                            " 'start' entry."
                        )

                else:
                    raise NotImplementedError(
                        f"Unrecognized event type '{eType}'."
                    )
        except Exception as e:
            raise LocatedJournalParseError(journalText, currentStartPos, e)

    def defineAlias(
        self,
        name: str,
        parameters: Sequence[str],
        commands: str
    ) -> None:
        """
        Defines an alias: a block of commands that can be played back
        later using the 'custom' command, with parameter substitutions.

        If an alias with the specified name already existed, it will be
        replaced.

        Each of the listed parameters must be supplied when invoking the
        alias, and where they appear within curly braces in the commands
        string, they will be substituted in. Additional names starting
        with '_' plus an optional integer will also be substituted with
        unique names (see `nextUniqueName`), with the same name being
        used for every instance that shares the same numerical suffix
        within each application of the command.

        For example:

        >>> o = JournalObserver()
        >>> o.defineAlias(
        ...     'hintRoom',
        ...     ['name'],
        ...     'o {_5}\\nx {_5} {name} {_5}\\ng hint\\nt {_5}'
        ... ) # _5 to show that the suffix doesn't matter if it's consistent
        >>> o.recordStart('start')
        >>> o.deployAlias('hintRoom', ['hint1'])
        >>> o.deployAlias('hintRoom', ['hint2'])
        >>> e = o.getExploration()
        >>> e.movementAtStep(0)
        (None, None, 0)
        >>> e.movementAtStep(1)
        (0, '_0', 1)
        >>> e.movementAtStep(2)
        (1, '_0', 0)
        >>> e.movementAtStep(3)
        (0, '_1', 2)
        >>> e.movementAtStep(4)
        (2, '_1', 0)
        >>> g = e.getSituation().graph
        >>> len(g)
        3
        >>> g.namesListing([0, 1, 2])
        '  0 (start)\\n  1 (hint1)\\n  2 (hint2)\\n'
        >>> g.decisionTags('hint1')
        {'hint': 1}
        >>> g.decisionTags('hint2')
        {'hint': 1}
        """
        self.aliases[name] = (list(parameters), commands)

    def deployAlias(self, name: str, arguments: Sequence[str]) -> None:
        """
        Deploys an alias, taking its command string and substituting in
        the provided argument values for each of the alias' parameters,
        plus any unique names that it requests. Substitution happens
        first for named arguments and then for unique strings, so named
        arguments of the form '{_-n-}' where -n- is an integer will end
        up being substituted for unique names.

        Raises a `JournalParseError` if the specified alias does not
        exist, or if the wrong number of parameters has been supplied.

        See `defineAlias` for an example.
        """
        # Fetch the alias
        alias = self.aliases.get(name)
        if alias is None:
            raise JournalParseError(
                f"Alias '{name}' has not been defined yet."
            )
        paramNames, commands = alias

        # Check arguments
        arguments = list(arguments)
        if len(arguments) != len(paramNames):
            raise JournalParseError(
                f"Alias '{name}' requires {len(paramNames)} parameters,"
                f" but you supplied {len(arguments)}."
            )

        # Find unique names
        uniques = set([
            match.strip('{}')
            for match in re.findall('{_[0-9]*}', commands)
        ])

        # Build substitution dictionary that passes through uniques
        firstWave = {unique: '{' + unique + '}' for unique in uniques}
        firstWave.update({
            param: value
            for (param, value) in zip(paramNames, arguments)
        })

        # Substitute parameter values
        commands = commands.format(**firstWave)

        uniques = set([
            match.strip('{}')
            for match in re.findall('{_[0-9]*}', commands)
        ])

        # Substitute for remaining unique names
        uniqueValues = {
            unique: self.nextUniqueName()
            for unique in sorted(uniques)  # sort for stability
        }
        commands = commands.format(**uniqueValues)

        # Now run the commands
        self.observe(commands)

    def doDebug(self, action: DebugAction) -> None:
        """
        Prints out a debugging message. Useful for figuring out parsing
        errors. See also `DebugAction` and `JournalEntryType. The action
        will be one of:
        - 'here': prints the ID and name of the current decision, or
            `None` if there isn't one.
        - 'transition': prints the name of the current transition, or `None`
            if there isn't one.
        - 'destinations': prints the ID and name of the current decision,
            followed by the names of each outgoing transition and their
            destinations. Includes any requirements the transitions have.
        - 'steps': prints out the number of steps in the current exploration,
            plus the number since the most recent use of 'steps'.
        - 'decisions': prints out the number of decisions in the current
            graph, plus the number added/removed since the most recent use of
            'decisions'.
        """
        graph = self.exploration.getSituation().graph
        if action == "here":
            dt = self.currentDecisionTarget()
            print(f"Current decision is: {graph.identityOf(dt)}")
        elif action == "transition":
            tTarget = self.currentTransitionTarget()
            if tTarget is None:
                print("Current transition is: None")
            else:
                tDecision, tTransition = tTarget
                print(
                    f"Current transition is {tTransition!r} from"
                    f" {graph.identityOf(tDecision)}."
                )
        elif action == "destinations":
            here = self.currentDecisionTarget()
            if here is None:
                print("There is no current decision.")
            else:
                dests = graph.destinationsFrom(here)
                outgoing = {
                    route: dests[route]
                    for route in dests
                    if dests[route] != here
                }
                actions = {
                    route: dests[route]
                    for route in dests
                    if dests[route] == here
                }
                print(f"The current decision is: {graph.identityOf(here)}")
                if len(outgoing) == 0:
                    print(
                        "There are no outgoing transitions at this"
                        " decision."
                    )
                else:
                    print(
                        f"There are {len(outgoing)} outgoing transitions:"
                    )
                for transition in outgoing:
                    destination = outgoing[transition]
                    req = graph.getTransitionRequirement(
                        here,
                        transition
                    )
                    rstring = ''
                    if req != base.ReqNothing():
                        rstring = f" (requires {req})"
                    print(
                        f"  {transition!r} ->"
                        f" {graph.identityOf(destination)}{rstring}"
                    )

                if len(actions) > 0:
                    print(f"There are {len(actions)} actions:")
                    for oneAction in actions:
                        req = graph.getTransitionRequirement(
                            here,
                            oneAction
                        )
                        rstring = ''
                        if req != base.ReqNothing():
                            rstring = f" (requires {req})"
                        print(f"  {oneAction!r}{rstring}")

        elif action == "steps":
            steps = len(self.getExploration())
            if self.prevSteps is not None:
                elapsed = steps - cast(int, self.prevSteps)
                print(
                    f"There are {steps} steps in the current"
                    f" exploration (which is {elapsed} more than there"
                    f" were at the previous check)."
                )
            else:
                print(
                    f"There are {steps} steps in the current"
                    f" exploration."
                )
            self.prevSteps = steps

        elif action == "decisions":
            count = len(self.getExploration().getSituation().graph)
            if self.prevDecisions is not None:
                elapsed = count - self.prevDecisions
                print(
                    f"There are {count} decisions in the current"
                    f" graph (which is {elapsed} more than there"
                    f" were at the previous check)."
                )
            else:
                print(
                    f"There are {count} decisions in the current"
                    f" graph."
                )
            self.prevDecisions = count
        else:
            raise JournalParseError(
                f"Invalid debug command: {action!r}"
            )

    def recordStart(
        self,
        where: Union[base.DecisionName, base.DecisionSpecifier],
    ) -> None:
        """
        Records the start of the exploration. Use only once in each new
        domain, as the very first action in that domain (possibly after
        some zone declarations). The contextual domain is used if the
        given `base.DecisionSpecifier` doesn't include a domain.

        To create new decision points that are disconnected from the rest
        of the graph that aren't the first in their domain, use the
        `relative` method followed by `recordWarp`.
        """
        if self.inRelativeMode:
            raise JournalParseError(
                "Can't start the exploration in relative mode."
            )

        whereSpec: Union[base.DecisionID, base.DecisionSpecifier]
        if isinstance(where, base.DecisionName):
            whereSpec = self.parseFormat.parseDecisionSpecifier(where)
            if isinstance(whereSpec, base.DecisionID):
                raise JournalParseError(
                    f"Can't use a number for a decision name. Got:"
                    f" {where!r}"
                )
        else:
            whereSpec = where

        if whereSpec.domain is None:
            whereSpec = base.DecisionSpecifier(
                domain=self.context['domain'],
                zone=whereSpec.zone,
                name=whereSpec.name
            )
        self.context['decision'] = self.exploration.start(whereSpec)

    def recordObserveAction(self, name: base.Transition) -> None:
        """
        Records the observation of an action at the current decision,
        which has the given name.
        """
        here = self.definiteDecisionTarget()
        self.exploration.getSituation().graph.addAction(here, name)
        self.context['transition'] = (here, name)

    def recordObserve(
        self,
        name: base.Transition,
        destination: Optional[base.AnyDecisionSpecifier] = None,
        reciprocal: Optional[base.Transition] = None
    ) -> None:
        """
        Records the observation of a new option at the current decision.

        If two or three arguments are given, the destination is still
        marked as unexplored, but is given a name (with two arguments)
        and the reciprocal transition is named (with three arguments).

        TODO: If we do this with a destination and that doesn't add zone
        info, later when we return we should add zone info... OR we
        should add it now.
        """
        here = self.definiteDecisionTarget()

        # Our observation matches `DiscreteExploration.observe`
        obs: Union[
            base.Transition,
            Tuple[base.Transition, base.AnyDecisionSpecifier],
            Tuple[
                base.Transition,
                base.AnyDecisionSpecifier,
                base.Transition
            ]
        ]

        if isinstance(destination, str):
            destination = self.parseFormat.parseDecisionSpecifier(
                destination
            )

        if destination is not None:
            if reciprocal is not None:
                obs = (name, destination, reciprocal)
            else:
                obs = (name, destination)
        elif reciprocal is not None:
            # TODO: Allow this? (make the destination generic)
            raise ValueError(
                "You may not specify a reciprocal name without"
                " specifying a destination."
            )
        else:
            obs = name

        self.exploration.observe(here, obs)
        self.context['transition'] = (here, name)

    def recordExplore(
        self,
        transition: base.Transition,
        destination: Optional[base.AnyDecisionSpecifier] = None,
        reciprocal: Optional[base.Transition] = None,
    ) -> None:
        """
        Records the exploration of a transition which leads to a
        specific destination. The name of the reciprocal transition may
        also be specified. Creates the transition if it needs to.

        If no destination name is specified, the destination node must
        already exist and the name of the destination must not begin
        with '_u.' otherwise a `JournalParseError` will be generated.

        Sets the current transition to the transition taken.

        In relative mode, this makes all the same changes to the graph,
        without adding a new exploration step or applying transition
        effects.
        """
        here = self.definiteDecisionTarget()
        # Create transition if it doesn't already exist
        now = self.exploration.getSituation()
        graph = now.graph
        leadsTo = graph.getDestination(here, transition)

        if isinstance(destination, str):
            destination = self.parseFormat.parseDecisionSpecifier(
                destination
            )

        if (
            destination is not None
        and graph.getDecision(destination) is not None
        ):
            raise JournalParseError(
                f"Destiation {destination} is invalid because that"
                f" decision already exists. Use 'return' to record a"
                f" new connection to a previously-visited decision."
            )

        newDomain: Optional[base.Domain]
        newZone: Union[base.Zone, type[base.DefaultZone], None]
        newName: Optional[base.DecisionName]
        if isinstance(destination, base.DecisionSpecifier):
            newDomain = destination.domain
            newZone = destination.zone
            newName = destination.name
            if newZone is None:
                newZone = base.DefaultZone
            # TODO: Some way to specify non-zone placement in explore?
        elif isinstance(destination, base.DecisionID):
            raise JournalParseError(
                f"You cannot use a decision ID when specifying a new"
                f" name for an exploration destination (got:"
                f" {repr(destination)})"
            )
        else:  # must be None
            newZone = base.DefaultZone
            newDomain = None
            newName = destination

        if leadsTo is None:
            if newName is None:
                raise JournalParseError(
                    f"Transition '{transition}' at decision '{here}'"
                    f" does not already exist, so a destination name"
                    f" must be provided."
                )
            else:
                graph.addUnexploredEdge(
                    here,
                    transition,
                    toDomain=newDomain  # None is the default anyways
                )
                # Zone info only added in next step
        elif newName is None:
            # TODO: Generalize this... ?
            currentName = graph.nameFor(leadsTo)
            if currentName.startswith('_u.'):
                raise JournalParseError(
                    f"Destination {graph.identityOf(leadsTo)} from"
                    f" decision {graph.identityOf(here)} via transition"
                    f" '{transition}' must be named when explored,"
                    f" because its current name is a placeholder."
                )
            else:
                newName = currentName

        # TODO: Check for incompatible domain/zone in destination
        # specifier?

        if self.inRelativeMode:
            graph.replaceUnexplored(
                here,
                transition,
                newName,
                reciprocal,
                placeInZone=newZone
            )
            self.context['decision'] = graph.destination(here, transition)
            self.context['transition'] = (here, transition)
        else:
            destID = self.exploration.explore(
                transition,
                newName,
                reciprocal,
                zone=newZone
            )
            self.context['decision'] = destID
            self.context['transition'] = (here, transition)

    def recordRetrace(self, transition: base.Transition) -> None:
        """
        Records retracing a transition which leads to a known
        destination.

        Sets the current transition to the transition taken.

        In relative mode, simply sets the current transition target to
        the transition taken and sets the current decision target to its
        destination (it does not apply transition effects).
        """
        here = self.definiteDecisionTarget()
        now = self.exploration.getSituation()
        if not self.inRelativeMode:
            self.exploration.retrace(transition)
        self.context['decision'] = now.graph.destination(here, transition)
        self.context['transition'] = (here, transition)

    def recordAction(self, name: base.Transition) -> None:
        """
        Records an action taken at the current decision. If a transition
        of that name already existed, it will be converted into an action
        assuming that its destination is unexplored and has no
        connections yet, and that its reciprocal also has no special
        properties yet. If those assumptions do not hold, a
        `JournalParseError` will be raised under the assumption that the
        name collision was an accident, not intentional, since the
        destination and reciprocal are deleted in the process of
        converting a normal transition into an action.

        In relative mode, the action is created (or the transition is
        converted into an action) but effects are not applied.

        Example:

        >>> o = JournalObserver()
        >>> e = o.getExploration()
        >>> o.recordStart('start')
        >>> o.recordObserve('transition')
        >>> e.effectiveCapabilities()['capabilities']
        set()
        >>> o.recordObserveAction('action')
        >>> o.recordTransitionConsequence([base.effect(gain="capability")])
        >>> o.recordAction('action')
        >>> e.effectiveCapabilities()['capabilities']
        {'capability'}
        >>> o.recordAction('another') # add effects after...
        >>> effect = base.effect(lose="capability")
        >>> # This applies the effect and then adds it to the
        >>> # transition, since we already took the transition
        >>> o.recordAdditionalTransitionConsequence([effect])
        >>> e.effectiveCapabilities()['capabilities']
        set()
        >>> len(e)
        4
        >>> e.getActiveDecisions(0)
        set()
        >>> e.getActiveDecisions(1)
        {0}
        >>> e.getActiveDecisions(2)
        {0}
        >>> e.getActiveDecisions(3)
        {0}
        >>> e.getSituation(0).action
        ('start', 0, 'main', None, None, None)
        >>> e.getSituation(1).action
        ('take', 'active', 0, 'action')
        >>> e.getSituation(2).action
        ('take', 'active', 0, 'another')
        """
        here = self.definiteDecisionTarget()

        # Check if the transition already exists
        now = self.exploration.getSituation()
        graph = now.graph
        destinations = graph.destinationsFrom(here)

        # A transition going somewhere else
        if name in destinations and destinations[name] != here:
            destination = destinations[name]
            reciprocal = graph.getReciprocal(here, name)
            # To replace a transition with an action, the transition may
            # only have outgoing properties. Otherwise we assume it's an
            # error to name the action after a transition which was
            # intended to be a real transition.
            if (
                graph.hasBeenVisited(destination)
             or cast(int, graph.degree(destination)) > 2
                # TODO: Fix MultiDigraph type stubs...
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its destination is already explored or has"
                    f" been connected to."
                )
            if (
                reciprocal is not None
            and graph.getTransitionProperties(
                    destination,
                    reciprocal
                ) != {
                    'requirement': base.ReqNothing(),
                    'effects': [],
                    'tags': {},
                    'annotations': []
                }
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its reciprocal has custom properties."
                )

            if (
                graph.decisionAnnotations(destination) != []
             or graph.decisionTags(destination) != {'unknown': 1}
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its destination has tags and/or annotations."
                )

            # If we get here, re-target the transition, and then destroy
            # the old destination along with the old reciprocal edge.
            graph.retargetTransition(
                here,
                name,
                here,
                swapReciprocal=False
            )
            graph.removeDecision(destination)

        # This will either take the existing action OR create it if
        # necessary
        if self.inRelativeMode:
            if name not in destinations:
                graph.addAction(here, name)
        else:
            self.exploration.takeAction(name, fromDecision=here)
        self.context['transition'] = (here, name)

    def recordReturn(
        self,
        transition: base.Transition,
        destination: base.AnyDecisionSpecifier,
        reciprocal: Optional[base.Transition] = None
    ) -> None:
        """
        Records an exploration which leads back to a
        previously-encountered decision. If a reciprocal is specified,
        we connect to that transition as our reciprocal (it must have
        led to an unknown area or not have existed) or if not, we make a
        new connection with an automatic reciprocal name.

        If the specified transition does not exist, it will be created.

        Sets the current transition to the transition taken.

        In relative mode, does the same stuff but doesn't apply any
        transition effects.
        """
        here = self.definiteDecisionTarget()
        now = self.exploration.getSituation()
        graph = now.graph

        if isinstance(destination, str):
            destination = self.parseFormat.parseDecisionSpecifier(
                destination
            )

        # Add an unexplored edge just before doing the return if the
        # named transition didn't already exist.
        if graph.getDestination(here, transition) is None:
            graph.addUnexploredEdge(here, transition)

        # Works differently in relative mode
        if self.inRelativeMode:
            graph.replaceUnexplored(
                here,
                transition,
                destination,
                reciprocal
            )
            self.context['decision'] = graph.resolveDecision(destination)
            self.context['transition'] = (here, transition)
        else:
            self.exploration.returnTo(
                transition,
                destination,
                reciprocal
            )
            self.context['decision'] = graph.resolveDecision(destination)
            self.context['transition'] = (here, transition)

    def recordWarp(
        self,
        destination: base.AnyDecisionSpecifier,
    ) -> None:
        """
        Records a warp to a specific destination without creating a
        transition. If the destination did not exist, it will be
        created (but only if a `base.DecisionName` or
        `base.DecisionSpecifier` was supplied; a destination cannot be
        created based on a non-existent `base.DecisionID`).

        If the destination already exists its zones won't be changed.
        However, if the destination gets created, it will be added to
        the same zones as the previous position, or to whichever zone
        was specified as the zone component of a
        `base.DecisionSpecifier`, if any.

        Sets the current transition to `None`.

        In relative mode, simply updates the current target decision and
        sets the current target transition to `None`. It will still
        create the destination if necessary, possibly putting it in a
        zone. In relative mode, the destination's exploration status is
        set to "noticed" (and no exploration step is created), while in
        normal mode, the exploration status is set to 'unknown' in the
        original current step, and then a new step is added which will
        set the status to 'exploring'.

        If the previous position was not marked explicitly as
        incompletely-explored (see `recordExplorationIncomplete`),
        warping away from it will change its status from 'exploring' to
        'explored'.
        """
        now = self.exploration.getSituation()
        graph = now.graph

        if isinstance(destination, str):
            destination = self.parseFormat.parseDecisionSpecifier(
                destination
            )

        destID = graph.getDecision(destination)

        newZone: Union[
            base.Zone,
            type[base.DefaultZone],
            None
        ] = base.DefaultZone
        if self.inRelativeMode:  # create the decision if it didn't exist
            if destID not in graph:  # including if it's None
                if isinstance(destination, base.DecisionID):
                    raise JournalParseError(
                        f"Cannot go to decision {destination} because that"
                        f" decision ID does not exist, and we cannot create"
                        f" a new decision based only on a decision ID. Use"
                        f" a DecisionSpecifier or DecisionName to go to a"
                        f" new decision that needs to be created."
                    )
                elif isinstance(destination, base.DecisionName):
                    newName = destination
                    newZone = None
                    newDomain = None
                elif isinstance(destination, base.DecisionSpecifier):
                    newDomain, newZone, newName = destination
                else:
                    raise JournalParseError(
                        f"Invalid decision specifier: {repr(destination)}."
                        f" The destination must be a decision ID, a"
                        f" decision name, or a decision specifier."
                    )
                destID = graph.addDecision(newName, domain=newDomain)
                if newZone is base.DefaultZone:
                    ctxDecision = self.context['decision']
                    if ctxDecision is not None:
                        for zp in graph.zoneParents(ctxDecision):
                            graph.addDecisionToZone(destID, zp)
                elif newZone is not None:
                    graph.addDecisionToZone(destID, newZone)
                    # TODO: If this zone is new create it & add it to
                    # parent zones of old level-0 zone(s)?

                base.setExplorationStatus(now, destID, 'noticed', True)
                # TODO: Some way to specify 'hypothesized' here instead?

        else:
            # in normal mode, 'DiscreteExploration.warp' takes care of
            # creating the decision if needed
            whichFocus = None
            if self.context['focus'] is not None:
                whichFocus = (
                    self.context['context'],
                    self.context['domain'],
                    self.context['focus']
                )
            if destination is None:
                destination = destID

            if isinstance(destination, base.DecisionSpecifier):
                newZone = destination.zone
                newDomain = destination.domain
            else:
                newZone = base.DefaultZone
                newDomain = None

            destID = self.exploration.warp(
                destination,
                domain=newDomain,
                zone=newZone,
                whichFocus=whichFocus,
                inCommon=self.context['context'] == 'common'
            )
            # TODO: Some way to specify the decision type

        self.context['decision'] = destID
        self.context['transition'] = None

    def recordWait(self) -> None:
        """
        Records a wait step. Does not modify the current transition.

        Raises a `JournalParseError` in relative mode, since it wouldn't
        have any effect.
        """
        if self.inRelativeMode:
            raise JournalParseError("Can't wait in relative mode.")
        else:
            self.exploration.wait()

    def recordEnd(self, name: base.DecisionName) -> None:
        """
        Records an ending. Sets the current transition to the transition
        that leads to the ending. Endings are not added to zones.

        In relative mode, an ending is still added, but an exploration
        step taking the new transition is not.
        """
        graph = self.exploration.getSituation().graph
        here = self.definiteDecisionTarget()
        (eTransition, eID) = graph.addEnding(here, name)
        self.context['decision'] = eID
        self.context['transition'] = (here, eTransition)
        if not self.inRelativeMode:
            self.exploration.explore(eTransition, None)
        # TODO: ExplorationAction for an ending?
        # TODO: Prevent things like adding unexplored nodes to the
        # ending...

    def recordRequirement(self, req: Union[base.Requirement, str]) -> None:
        """
        Records a requirement observed on the most recently
        defined/taken transition. If a string is given,
        `ParseFormat.parseRequirement` will be used to parse it.
        """
        if isinstance(req, str):
            req = self.parseFormat.parseRequirement(req)
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Can't set a requirement because there is no current"
                " transition."
            )
        self.exploration.getSituation().graph.setTransitionRequirement(
            *target,
            req
        )

    def recordReciprocalRequirement(
        self,
        req: Union[base.Requirement, str]
    ) -> None:
        """
        Records a requirement observed on the reciprocal of the most
        recently defined/taken transition. If a string is given,
        `ParseFormat.parseRequirement` will be used to parse it.
        """
        if isinstance(req, str):
            req = self.parseFormat.parseRequirement(req)
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Can't set a reciprocal requirement because there is no"
                " current transition or it doesn't have a reciprocal."
            )
        graph = self.exploration.getSituation().graph
        graph.setTransitionRequirement(*target, req)

    def recordTransitionConsequence(
        self,
        consequence: base.Consequence
    ) -> None:
        """
        Records a transition consequence, which replaces any existing
        consequences of the currently-relevant transition (the
        most-recently created or taken transition). A
        `JournalParseError` will be raised if there is no current
        transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot apply a consequence because there is no current"
                " transition."
            )

        now = self.exploration.getSituation()
        return now.graph.setConsequence(*target, consequence)

    def recordReciprocalConsequence(
        self,
        consequence: base.Consequence
    ) -> None:
        """
        Like `recordTransitionConsequence` but applies the effect to the
        reciprocal of the current transition. Will cause a
        `JournalParseError` if the current transition has no reciprocal
        (e.g., it's an ending transition).
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot apply a reciprocal effect because there is no"
                " current transition, or it doesn't have a reciprocal."
            )

        now = self.exploration.getSituation()
        now.graph.setConsequence(*target, consequence)

    def recordAdditionalTransitionConsequence(
        self,
        consequence: base.Consequence,
        hideEffects: bool = True
    ) -> None:
        """
        Records the addition of a new consequence to the current
        relevant transition, while also triggering the effects of that
        consequence (but not the other effects of that transition, which
        we presume have just been applied already).

        By default each effect added this way automatically gets the
        "hidden" property added to it, because the assumption is if it
        were a foreseeable effect, you would have added it to the
        transition before taking it. If you set `hideEffects` to
        `False`, this won't be done.

        This modifies the current state but does not add a step to the
        exploration.
        """
        # Receive begin/end indices from `addConsequence` and send them
        # to `applyTransitionConsequence` to limit which # parts of the
        # expanded consequence are actually applied.
        currentTransition = self.currentTransitionTarget()
        if currentTransition is None:
            consRepr = self.parseFormat.unparseConsequence(consequence)
            raise JournalParseError(
                f"Can't apply an additional consequence to a transition"
                f" when there is no current transition. Got"
                f" consequence:\n{consRepr}"
            )

        if hideEffects:
            for (index, item) in base.walkParts(consequence):
                if isinstance(item, dict) and 'value' in item:
                    assert 'hidden' in item
                    item = cast(base.Effect, item)
                    item['hidden'] = True

        now = self.exploration.getSituation()
        begin, end = now.graph.addConsequence(
            *currentTransition,
            consequence
        )
        self.exploration.applyTransitionConsequence(
            *currentTransition,
            moveWhich=self.context['focus'],
            policy="specified",
            fromIndex=begin,
            toIndex=end
        )
        # This tracks trigger counts and obeys
        # charges/delays, unlike
        # applyExtraneousConsequence, but some effects
        # like 'bounce' still can't be properly applied

    def recordTagDecision(
        self,
        tag: base.Tag,
        value: Union[base.TagValue, type[base.NoTagValue]] = base.NoTagValue
    ) -> None:
        """
        Records a tag to be applied to the current decision.
        """
        now = self.exploration.getSituation()
        now.graph.tagDecision(
            self.definiteDecisionTarget(),
            tag,
            value
        )

    def recordTagTranstion(
        self,
        tag: base.Tag,
        value: Union[base.TagValue, type[base.NoTagValue]] = base.NoTagValue
    ) -> None:
        """
        Records tags to be applied to the most-recently-defined or
        -taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot tag a transition because there is no current"
                " transition."
            )

        now = self.exploration.getSituation()
        now.graph.tagTransition(*target, tag, value)

    def recordTagReciprocal(
        self,
        tag: base.Tag,
        value: Union[base.TagValue, type[base.NoTagValue]] = base.NoTagValue
    ) -> None:
        """
        Records tags to be applied to the reciprocal of the
        most-recently-defined or -taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot tag a transition because there is no current"
                " transition."
            )

        now = self.exploration.getSituation()
        now.graph.tagTransition(*target, tag, value)

    def recordAnnotateStep(
        self,
        *annotations: base.Annotation
    ) -> None:
        """
        Records annotations to be applied to the current exploration
        step.
        """
        self.exploration.annotateStep(annotations)

    def recordAnnotateDecision(
        self,
        *annotations: base.Annotation
    ) -> None:
        """
        Records annotations to be applied to the current decision.
        """
        now = self.exploration.getSituation()
        now.graph.annotateDecision(self.definiteDecisionTarget(), annotations)

    def recordAnnotateTranstion(
        self,
        *annotations: base.Annotation
    ) -> None:
        """
        Records annotations to be applied to the most-recently-defined
        or -taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot annotate a transition because there is no"
                " current transition."
            )

        now = self.exploration.getSituation()
        now.graph.annotateTransition(*target, annotations)

    def recordAnnotateReciprocal(
        self,
        *annotations: base.Annotation
    ) -> None:
        """
        Records annotations to be applied to the reciprocal of the
        most-recently-defined or -taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot annotate a reciprocal because there is no"
                " current transition or because it doens't have a"
                " reciprocal."
            )

        now = self.exploration.getSituation()
        now.graph.annotateTransition(*target, annotations)

    def recordContextSwap(
        self,
        targetContext: Optional[base.FocalContextName]
    ) -> None:
        """
        Records a swap of the active focal context, and/or a swap into
        "common"-context mode where all effects modify the common focal
        context instead of the active one. Use `None` as the argument to
        swap to common mode; use another specific value so swap to
        normal mode and set that context as the active one.

        In relative mode, swaps the active context without adding an
        exploration step. Swapping into the common context never results
        in a new exploration step.
        """
        if targetContext is None:
            self.context['context'] = "common"
        else:
            self.context['context'] = "active"
            e = self.getExploration()
            if self.inRelativeMode:
                e.setActiveContext(targetContext)
            else:
                e.advanceSituation(('swap', targetContext))

    def recordZone(self, level: int, zone: base.Zone) -> None:
        """
        Records a new current zone to be swapped with the zone(s) at the
        specified hierarchy level for the current decision target. See
        `core.DiscreteExploration.reZone` and
        `core.DecisionGraph.replaceZonesInHierarchy` for details on what
        exactly happens; the summary is that the zones at the specified
        hierarchy level are replaced with the provided zone (which is
        created if necessary) and their children are re-parented onto
        the provided zone, while that zone is also set as a child of
        their parents.

        Does the same thing in relative mode as in normal mode.
        """
        self.exploration.reZone(
            zone,
            self.definiteDecisionTarget(),
            level
        )

    def recordUnify(
        self,
        merge: base.AnyDecisionSpecifier,
        mergeInto: Optional[base.AnyDecisionSpecifier] = None
    ) -> None:
        """
        Records a unification between two decisions. This marks an
        observation that they are actually the same decision and it
        merges them. If only one decision is given the current decision
        is merged into that one. After the merge, the first decision (or
        the current decision if only one was given) will no longer
        exist.

        If one of the merged decisions was the current position in a
        singular-focalized domain, or one of the current positions in a
        plural- or spreading-focalized domain, the merged decision will
        replace it as a current decision after the merge, and this
        happens even when in relative mode. The target decision is also
        updated if it needs to be.

        A `TransitionCollisionError` will be raised if the two decisions
        have outgoing transitions that share a name.

        Logs a `JournalParseWarning` if the two decisions were in
        different zones.

        Any transitions between the two merged decisions will remain in
        place as actions.

        TODO: Option for removing self-edges after the merge? Option for
        doing that for just effect-less edges?
        """
        if mergeInto is None:
            mergeInto = merge
            merge = self.definiteDecisionTarget()

        if isinstance(merge, str):
            merge = self.parseFormat.parseDecisionSpecifier(merge)

        if isinstance(mergeInto, str):
            mergeInto = self.parseFormat.parseDecisionSpecifier(mergeInto)

        now = self.exploration.getSituation()

        if not isinstance(merge, base.DecisionID):
            merge = now.graph.resolveDecision(merge)

        merge = cast(base.DecisionID, merge)

        now.graph.mergeDecisions(merge, mergeInto)

        mergedID = now.graph.resolveDecision(mergeInto)

        # Update FocalContexts & ObservationContexts as necessary
        self.cleanupContexts(remapped={merge: mergedID})

    def recordUnifyTransition(self, target: base.Transition) -> None:
        """
        Records a unification between the most-recently-defined or
        -taken transition and the specified transition (which must be
        outgoing from the same decision). This marks an observation that
        two transitions are actually the same transition and it merges
        them.

        After the merge, the target transition will still exist but the
        previously most-recent transition will have been deleted.

        Their reciprocals will also be merged.

        A `JournalParseError` is raised if there is no most-recent
        transition.
        """
        now = self.exploration.getSituation()
        graph = now.graph
        affected = self.currentTransitionTarget()
        if affected is None or affected[1] is None:
            raise JournalParseError(
                "Cannot unify transitions: there is no current"
                " transition."
            )

        decision, transition = affected

        # If they don't share a target, then the current transition must
        # lead to an unknown node, which we will dispose of
        destination = graph.getDestination(decision, transition)
        if destination is None:
            raise JournalParseError(
                f"Cannot unify transitions: transition"
                f" '{transition}' at decision '{decision}' has no"
                f" destination."
            )

        finalDestination = graph.getDestination(decision, target)
        if finalDestination is None:
            raise JournalParseError(
                f"Cannot unify transitions: transition"
                f" '{target}' at decision '{decision}' has no"
                f" destination."
            )

        if destination != finalDestination:
            if graph.hasBeenVisited(destination):
                raise JournalParseError(
                    f"Cannot unify transitions: destination"
                    f" '{destination}' of transition '{transition}' at"
                    f" decision '{decision}' is not an unknown"
                    f" decision."
                )
            # Retarget and delete the unknown node that we abandon
            # TODO: Merge nodes instead?
            now.graph.retargetTransition(
                decision,
                transition,
                finalDestination
            )
            now.graph.removeDecision(destination)

        # Now we can merge transitions
        now.graph.mergeTransitions(decision, transition, target)

        # Update targets if they were merged
        self.cleanupContexts(
            remappedTransitions={
                (decision, transition): (decision, target)
            }
        )

    def recordUnifyReciprocal(
        self,
        target: base.Transition
    ) -> None:
        """
        Records a unification between the reciprocal of the
        most-recently-defined or -taken transition and the specified
        transition, which must be outgoing from the current transition's
        destination. This marks an observation that two transitions are
        actually the same transition and it merges them, deleting the
        original reciprocal. Note that the current transition will also
        be merged with the reciprocal of the target.

        A `JournalParseError` is raised if there is no current
        transition, or if it does not have a reciprocal.
        """
        now = self.exploration.getSituation()
        graph = now.graph
        affected = self.currentReciprocalTarget()
        if affected is None or affected[1] is None:
            raise JournalParseError(
                "Cannot unify transitions: there is no current"
                " transition."
            )

        decision, transition = affected

        destination = graph.destination(decision, transition)
        reciprocal = graph.getReciprocal(decision, transition)
        if reciprocal is None:
            raise JournalParseError(
                "Cannot unify reciprocal: there is no reciprocal of the"
                " current transition."
            )

        # If they don't share a target, then the current transition must
        # lead to an unknown node, which we will dispose of
        finalDestination = graph.getDestination(destination, target)
        if finalDestination is None:
            raise JournalParseError(
                f"Cannot unify reciprocal: transition"
                f" '{target}' at decision '{destination}' has no"
                f" destination."
            )

        if decision != finalDestination:
            if graph.hasBeenVisited(decision):
                raise JournalParseError(
                    f"Cannot unify reciprocal: destination"
                    f" '{decision}' of transition '{reciprocal}' at"
                    f" decision '{destination}' is not an unknown"
                    f" decision."
                )
            # Retarget and delete the unknown node that we abandon
            # TODO: Merge nodes instead?
            graph.retargetTransition(
                destination,
                reciprocal,
                finalDestination
            )
            graph.removeDecision(decision)

        # Actually merge the transitions
        graph.mergeTransitions(destination, reciprocal, target)

        # Update targets if they were merged
        self.cleanupContexts(
            remappedTransitions={
                (decision, transition): (decision, target)
            }
        )

    def recordObviate(
        self,
        transition: base.Transition,
        otherDecision: base.AnyDecisionSpecifier,
        otherTransition: base.Transition
    ) -> None:
        """
        Records the obviation of a transition at another decision. This
        is the observation that a specific transition at the current
        decision is the reciprocal of a different transition at another
        decision which previously led to an unknown area. The difference
        between this and `recordReturn` is that `recordReturn` logs
        movement across the newly-connected transition, while this
        leaves the player at their original decision (and does not even
        add a step to the current exploration).

        Both transitions will be created if they didn't already exist.

        In relative mode does the same thing and doesn't move the current
        decision across the transition updated.

        If the destination is unknown, it will remain unknown after this
        operation.
        """
        now = self.exploration.getSituation()
        graph = now.graph
        here = self.definiteDecisionTarget()

        if isinstance(otherDecision, str):
            otherDecision = self.parseFormat.parseDecisionSpecifier(
                otherDecision
            )

        otherDestination = graph.getDestination(
            otherDecision,
            otherTransition
        )
        if otherDestination is not None:
            if graph.hasBeenVisited(otherDestination):
                raise JournalParseError(
                    f"Cannot obviate transition '{otherTransition}' at"
                    f" decision '{otherDecision}': that transition leads"
                    f" to decision '{otherDestination}' which has"
                    f" already been visited."
                )
        else:
            # We must create the other destination
            graph.addUnexploredEdge(otherDecision, otherTransition)

        destination = graph.getDestination(here, transition)
        if destination is not None:
            if graph.hasBeenVisited(destination):
                raise JournalParseError(
                    f"Cannot obviate using transition '{transition}' at"
                    f" decision '{here}': that transition leads to"
                    f" decision '{destination}' which is not an unknown"
                    f" decision."
                )
        else:
            # we need to create it
            graph.addUnexploredEdge(here, transition)

        # Track exploration status of destination (because
        # `replaceUnexplored` will overwrite it but we want to preserve
        # it in this case.
        if otherDecision is not None:
            prevStatus = base.explorationStatusOf(now, otherDecision)

        # Now connect the transitions and clean up the unknown nodes
        graph.replaceUnexplored(
            here,
            transition,
            otherDecision,
            otherTransition
        )
        # Restore exploration status
        base.setExplorationStatus(now, otherDecision, prevStatus)

        # Update context
        self.context['transition'] = (here, transition)

    def cleanupContexts(
        self,
        remapped: Optional[Dict[base.DecisionID, base.DecisionID]] = None,
        remappedTransitions: Optional[
            Dict[
                Tuple[base.DecisionID, base.Transition],
                Tuple[base.DecisionID, base.Transition]
            ]
        ] = None
    ) -> None:
        """
        Checks the validity of context decision and transition entries,
        and sets them to `None` in situations where they are no longer
        valid, affecting both the current and stored contexts.

        Also updates position information in focal contexts in the
        current exploration step.

        If a `remapped` dictionary is provided, decisions in the keys of
        that dictionary will be replaced with the corresponding value
        before being checked.

        Similarly a `remappedTransitions` dicitonary may provide info on
        renamed transitions using (`base.DecisionID`, `base.Transition`)
        pairs as both keys and values.
        """
        if remapped is None:
            remapped = {}

        if remappedTransitions is None:
            remappedTransitions = {}

        # Fix broken position information in the current focal contexts
        now = self.exploration.getSituation()
        graph = now.graph
        state = now.state
        for ctx in (
            state['common'],
            state['contexts'][state['activeContext']]
        ):
            active = ctx['activeDecisions']
            for domain in active:
                aVal = active[domain]
                if isinstance(aVal, base.DecisionID):
                    if aVal in remapped:  # check for remap
                        aVal = remapped[aVal]
                        active[domain] = aVal
                    if graph.getDecision(aVal) is None: # Ultimately valid?
                        active[domain] = None
                elif isinstance(aVal, dict):
                    for fpName in aVal:
                        fpVal = aVal[fpName]
                        if fpVal is None:
                            aVal[fpName] = None
                        elif fpVal in remapped:  # check for remap
                            aVal[fpName] = remapped[fpVal]
                        elif graph.getDecision(fpVal) is None:  # valid?
                            aVal[fpName] = None
                elif isinstance(aVal, set):
                    for r in remapped:
                        if r in aVal:
                            aVal.remove(r)
                            aVal.add(remapped[r])
                    discard = []
                    for dID in aVal:
                        if graph.getDecision(dID) is None:
                            discard.append(dID)
                    for dID in discard:
                        aVal.remove(dID)
                elif aVal is not None:
                    raise RuntimeError(
                        f"Invalid active decisions for domain"
                        f" {repr(domain)}: {repr(aVal)}"
                    )

        # Fix up our ObservationContexts
        fix = [self.context]
        if self.storedContext is not None:
            fix.append(self.storedContext)

        graph = self.exploration.getSituation().graph
        for obsCtx in fix:
            cdID = obsCtx['decision']
            if cdID in remapped:
                cdID = remapped[cdID]
                obsCtx['decision'] = cdID

            if cdID not in graph:
                obsCtx['decision'] = None

            transition = obsCtx['transition']
            if transition is not None:
                tSourceID = transition[0]
                if tSourceID in remapped:
                    tSourceID = remapped[tSourceID]
                    obsCtx['transition'] = (tSourceID, transition[1])

                if transition in remappedTransitions:
                    obsCtx['transition'] = remappedTransitions[transition]

                tDestID = graph.getDestination(tSourceID, transition[1])
                if tDestID is None:
                    obsCtx['transition'] = None

    def recordExtinguishDecision(
        self,
        target: base.AnyDecisionSpecifier
    ) -> None:
        """
        Records the deletion of a decision. The decision and all
        transitions connected to it will be removed from the current
        graph. Does not create a new exploration step. If the current
        position is deleted, the position will be set to `None`, or if
        we're in relative mode, the decision target will be set to
        `None` if it gets deleted. Likewise, all stored and/or current
        transitions which no longer exist are erased to `None`.
        """
        # Erase target if it's going to be removed
        now = self.exploration.getSituation()

        if isinstance(target, str):
            target = self.parseFormat.parseDecisionSpecifier(target)

        # TODO: Do we need to worry about the node being part of any
        # focal context data structures?

        # Actually remove it
        now.graph.removeDecision(target)

        # Clean up our contexts
        self.cleanupContexts()

    def recordExtinguishTransition(
        self,
        source: base.AnyDecisionSpecifier,
        target: base.Transition,
        deleteReciprocal: bool = True
    ) -> None:
        """
        Records the deletion of a named transition coming from a
        specific source. The reciprocal will also be removed, unless
        `deleteReciprocal` is set to False. If `deleteReciprocal` is
        used and this results in the complete isolation of an unknown
        node, that node will be deleted as well. Cleans up any saved
        transition targets that are no longer valid by setting them to
        `None`. Does not create a graph step.
        """
        now = self.exploration.getSituation()
        graph = now.graph
        dest = graph.destination(source, target)

        # Remove the transition
        graph.removeTransition(source, target, deleteReciprocal)

        # Remove the old destination if it's unknown and no longer
        # connected anywhere
        if (
            not graph.hasBeenVisited(dest)
        and len(graph.destinationsFrom(dest)) == 0
        ):
            graph.removeDecision(dest)

        # Clean up our contexts
        self.cleanupContexts()

    def recordComplicate(
        self,
        target: base.Transition,
        newDecision: base.DecisionName,  # TODO: Allow zones/domain here
        newReciprocal: Optional[base.Transition],
        newReciprocalReciprocal: Optional[base.Transition]
    ) -> base.DecisionID:
        """
        Records the complication of a transition and its reciprocal into
        a new decision. The old transition and its old reciprocal (if
        there was one) both point to the new decision. The
        `newReciprocal` becomes the new reciprocal of the original
        transition, and the `newReciprocalReciprocal` becomes the new
        reciprocal of the old reciprocal. Either may be set explicitly to
        `None` to leave the corresponding new transition without a
        reciprocal (but they don't default to `None`). If there was no
        old reciprocal, but `newReciprocalReciprocal` is specified, then
        that transition is created linking the new node to the old
        destination, without a reciprocal.

        The current decision & transition information is not updated.

        Returns the decision ID for the new node.
        """
        now = self.exploration.getSituation()
        graph = now.graph
        here = self.definiteDecisionTarget()

        oldDest = graph.destination(here, target)
        oldReciprocal = graph.getReciprocal(here, target)

        # Create the new node:
        newID = graph.addDecision(newDecision)
        # TODO: Copy over zone/domain info
        # Note that created is not an unknown decision
        # TODO: What exploration status should it have? Depends on the
        # two ends?

        # Retarget the transitions
        graph.retargetTransition(
            here,
            target,
            newID,
            swapReciprocal=False
        )
        if oldReciprocal is not None:
            graph.retargetTransition(
                oldDest,
                oldReciprocal,
                newID,
                swapReciprocal=False
            )

        # Add a new reciprocal edge
        if newReciprocal is not None:
            graph.addTransition(newID, newReciprocal, here)
            graph.setReciprocal(here, target, newReciprocal)

        # Add a new double-reciprocal edge (even if there wasn't a
        # reciprocal before)
        if newReciprocalReciprocal is not None:
            graph.addTransition(
                newID,
                newReciprocalReciprocal,
                oldDest
            )
            if oldReciprocal is not None:
                graph.setReciprocal(
                    oldDest,
                    oldReciprocal,
                    newReciprocalReciprocal
                )

        return newID

    def recordFulfills(
        self,
        requirement: Union[str, base.Requirement],
        capability: base.Capability
    ) -> None:
        """
        Records the observation that a certain requirement fulfills the
        same role as (i.e., is equivalent to) a specific capability.
        Transitions that require that capability will count as traversable
        even if that capability is not obtained, as long as the
        requirement is satisfied. If multiple equivalences are
        established, any one of them being satisfied will count as that
        capability being obtained. Note that if a circular dependency is
        created, the capability (unless actually obtained) will be
        considered as not being obtained during recursive checks.
        """
        if isinstance(requirement, str):
            requirement = self.parseFormat.parseRequirement(requirement)

        self.getExploration().getSituation().graph.addEquivalence(
            requirement,
            capability
        )

    def recordFocusOn(
        self,
        newFocalPoint: base.FocalPointName,
        inDomain: Optional[base.Domain] = None,
        inCommon: bool = False
    ):
        """
        Records a swap to a new focal point, setting that focal point as
        the active focal point in the observer's current domain, or in
        the specified domain if one is specified.

        A `JournalParseError` is raised if the current/specified domain
        does not have plural focalization. If it doesn't have a focal
        point with that name, then one is created and positioned at the
        observer's current decision (which must be in the appropriate
        domain).

        If `inCommon` is set to `True` (default is `False`) then the
        changes will be applied to the common context instead of the
        active context.

        Note that this does *not* make the target domain active; use
        `recordDomainFocus` for that if you need to.
        """
        if inDomain is None:
            inDomain = self.context['domain']

        if inCommon:
            ctx = self.getExploration().getCommonContext()
        else:
            ctx = self.getExploration().getActiveContext()

        if ctx['focalization'].get('domain') != 'plural':
            raise JournalParseError(
                f"Domain '{inDomain}' does not exist or does not have"
                f" plural focalization, so we can't set a focal point"
                f" in it."
            )

        focalPointMap = ctx['activeDecisions'].setdefault(inDomain, {})
        if not isinstance(focalPointMap, dict):
            raise RuntimeError(
                f"Plural-focalized domain '{inDomain}' has"
                f" non-dictionary active"
                f" decisions:\n{repr(focalPointMap)}"
            )

        if newFocalPoint not in focalPointMap:
            focalPointMap[newFocalPoint] = self.context['decision']

        self.context['focus'] = newFocalPoint
        self.context['decision'] = focalPointMap[newFocalPoint]

    def recordDomainUnfocus(
        self,
        domain: base.Domain,
        inCommon: bool = False
    ):
        """
        Records a domain losing focus. Does not raise an error if the
        target domain was not active (in that case, it doesn't need to
        do anything).

        If `inCommon` is set to `True` (default is `False`) then the
        domain changes will be applied to the common context instead of
        the active context.
        """
        if inCommon:
            ctx = self.getExploration().getCommonContext()
        else:
            ctx = self.getExploration().getActiveContext()

        try:
            ctx['activeDomains'].remove(domain)
        except KeyError:
            pass

    def recordDomainFocus(
        self,
        domain: base.Domain,
        exclusive: bool = False,
        inCommon: bool = False
    ):
        """
        Records a domain gaining focus, activating that domain in the
        current focal context and setting it as the observer's current
        domain. If the domain named doesn't exist yet, it will be
        created first (with default focalization) and then focused.

        If `exclusive` is set to `True` (default is `False`) then all
        other active domains will be deactivated.

        If `inCommon` is set to `True` (default is `False`) then the
        domain changes will be applied to the common context instead of
        the active context.
        """
        if inCommon:
            ctx = self.getExploration().getCommonContext()
        else:
            ctx = self.getExploration().getActiveContext()

        if exclusive:
            ctx['activeDomains'] = set()

        if domain not in ctx['focalization']:
            self.recordNewDomain(domain, inCommon=inCommon)
        else:
            ctx['activeDomains'].add(domain)

        self.context['domain'] = domain

    def recordNewDomain(
        self,
        domain: base.Domain,
        focalization: base.DomainFocalization = "singular",
        inCommon: bool = False
    ):
        """
        Records a new domain, setting it up with the specified
        focalization. Sets that domain as an active domain and as the
        journal's current domain so that subsequent entries will create
        decisions in that domain. However, it does not activate any
        decisions within that domain.

        Raises a `JournalParseError` if the specified domain already
        exists.

        If `inCommon` is set to `True` (default is `False`) then the new
        domain will be made active in the common context instead of the
        active context.
        """
        if inCommon:
            ctx = self.getExploration().getCommonContext()
        else:
            ctx = self.getExploration().getActiveContext()

        if domain in ctx['focalization']:
            raise JournalParseError(
                f"Cannot create domain '{domain}': that domain already"
                f" exists."
            )

        ctx['focalization'][domain] = focalization
        ctx['activeDecisions'][domain] = None
        ctx['activeDomains'].add(domain)
        self.context['domain'] = domain

    def relative(
        self,
        where: Optional[base.AnyDecisionSpecifier] = None,
        transition: Optional[base.Transition] = None,
    ) -> None:
        """
        Enters 'relative mode' where the exploration ceases to add new
        steps but edits can still be performed on the current graph. This
        also changes the current decision/transition settings so that
        edits can be applied anywhere. It can accept 0, 1, or 2
        arguments. With 0 arguments, it simply enters relative mode but
        maintains the current position as the target decision and the
        last-taken or last-created transition as the target transition
        (note that that transition usually originates at a different
        decision). With 1 argument, it sets the target decision to the
        decision named, and sets the target transition to None. With 2
        arguments, it sets the target decision to the decision named, and
        the target transition to the transition named, which must
        originate at that target decision. If the first argument is None,
        the current decision is used.

        If given the name of a decision which does not yet exist, it will
        create that decision in the current graph, disconnected from the
        rest of the graph. In that case, it is an error to also supply a
        transition to target (you can use other commands once in relative
        mode to build more transitions and decisions out from the
        newly-created decision).

        When called in relative mode, it updates the current position
        and/or decision, or if called with no arguments, it exits
        relative mode. When exiting relative mode, the current decision
        is set back to the graph's current position, and the current
        transition is set to whatever it was before relative mode was
        entered.

        Raises a `TypeError` if a transition is specified without
        specifying a decision. Raises a `ValueError` if given no
        arguments and the exploration does not have a current position.
        Also raises a `ValueError` if told to target a specific
        transition which does not exist. Raises a `core.BadStart` error
        if called before the exploration is started.
        """
        # TODO: Not this?
        if len(self.exploration.getSituation().graph) == 0:
            raise core.BadStart(
                "Cannot enter relative mode before the exploration is"
                " started (call `recordStart` first)."
            )

        if where is None:
            if transition is None and self.inRelativeMode:
                # If we're in relative mode, cancel it
                self.inRelativeMode = False

                # Here we restore saved sate
                if self.storedContext is None:
                    raise RuntimeError(
                        "No stored context despite being in relative"
                        "mode."
                    )
                self.context = self.storedContext
                self.storedContext = None

            else:
                # Enter or stay in relative mode and set up the current
                # decision/transition as the targets

                # Ensure relative mode
                self.inRelativeMode = True

                # Store state
                self.storedContext = self.context
                where = self.storedContext['decision']
                if where is None:
                    raise ValueError(
                        "Cannot enter relative mode at the current"
                        " position because there is no current"
                        " position."
                    )

                self.context = observationContext(
                    context=self.storedContext['context'],
                    domain=self.storedContext['domain'],
                    focus=self.storedContext['focus'],
                    decision=where,
                    transition=(
                        None
                        if transition is None
                        else (where, transition)
                    )
                )

        else: # we have at least a decision to target
            # If we're entering relative mode instead of just changing
            # focus, we need to set up the current transition if no
            # transition was specified.
            entering: Optional[
                Tuple[
                    base.ContextSpecifier,
                    base.Domain,
                    Optional[base.FocalPointName]
                ]
            ] = None
            if not self.inRelativeMode:
                # We'll be entering relative mode, so store state
                entering = (
                    self.context['context'],
                    self.context['domain'],
                    self.context['focus']
                )
                self.storedContext = self.context
                if transition is None:
                    oldTransitionPair = self.context['transition']
                    if oldTransitionPair is not None:
                        oldBase, oldTransition = oldTransitionPair
                        if oldBase == where:
                            transition = oldTransition

            # Enter (or stay in) relative mode
            self.inRelativeMode = True

            now = self.exploration.getSituation()
            whereID: Optional[base.DecisionID]
            whereName: Optional[base.DecisionName]
            if isinstance(where, str):
                where = self.parseFormat.parseDecisionSpecifier(where)
                # might turn it into a DecisionID

            if isinstance(where, base.DecisionID):
                whereID = where
                whereName = None
            else:
                whereID = now.graph.getDecision(where)
                if isinstance(where, base.DecisionSpecifier):
                    whereName = where.name
                else:
                    raise TypeError(f"Invalid decision specifier: {where!r}")

            # Create a new decision if necessary
            if whereID is None:
                if transition is not None:
                    raise TypeError(
                        f"Cannot specify a target transition when"
                        f" entering relative mode at previously"
                        f" non-existent decision '{where}'."
                    )
                assert whereName is not None
                whereID = now.graph.addDecision(whereName)

            # Create the new context if we're entering relative mode
            if entering is not None:
                self.context = observationContext(
                    context=entering[0],
                    domain=entering[1],
                    focus=entering[2],
                    decision=whereID,
                    transition=(
                        None
                        if transition is None
                        else (whereID, transition)
                    )
                )

            # Target the specified decision
            self.context['decision'] = whereID

            # Target the specified transition
            if transition is not None:
                self.context['transition'] = (whereID, transition)
                if now.graph.getDestination(where, transition) is None:
                    raise ValueError(
                        f"Cannot target transition '{transition}' at"
                        f" decision '{where}': there is no such"
                        f" transition."
                    )
            # otherwise leave self.context['transition'] alone


#--------------------#
# Shortcut Functions #
#--------------------#

def convertJournal(
    journal: str,
    fmt: Optional[JournalParseFormat] = None
) -> core.DiscreteExploration:
    """
    Converts a journal in text format into a `core.DiscreteExploration`
    object, using a fresh `JournalObserver`. An optional `ParseFormat`
    may be specified if the journal doesn't follow the default parse
    format.
    """
    obs = JournalObserver(fmt)
    obs.observe(journal)
    return obs.getExploration()
