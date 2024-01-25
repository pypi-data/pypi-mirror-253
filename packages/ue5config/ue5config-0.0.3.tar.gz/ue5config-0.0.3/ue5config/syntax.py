from typing import Any

import pyparsing as pyp
from pyparsing import pyparsing_common as ppc


def fnSectionIdentifier(s: str, loc: int, toks: pyp.ParseResults) -> Any:
    return toks[0]


def make_keyword(kwd: str, value: Any) -> Any:
    return pyp.Keyword(kwd).set_parse_action(pyp.replace_with(value))


def build_syntax() -> pyp.ParserElement:
    """
    DANGER:
        Do not modify this method unless you know how grammatical parsers work.
    """

    Comment = pyp.Regex(r";.*").set_name("Comment")
    TRUE = make_keyword("True", True)
    FALSE = make_keyword("False", False)
    NONE = make_keyword("None", None)
    OpenParen = pyp.Literal("(").suppress()
    CloseParen = pyp.Literal(")").suppress()
    OpenSquareBracket = pyp.Literal("[").suppress()
    CloseSquareBracket = pyp.Literal("]").suppress()
    Equals = pyp.Literal("=").suppress()
    SectionIdentifier = pyp.Regex(r"[^\]]*").set_name("SectionIdentifier")
    Key = pyp.Regex(r"[^=]+").set_name("Key")
    SectionHeader = OpenSquareBracket + SectionIdentifier + CloseSquareBracket

    # USON is just what I call this.  Unreal probably uses another name idfk. I'm a Unity boy (kill me).
    usonString = pyp.dbl_quoted_string().set_parse_action(pyp.remove_quotes)
    usonInteger = (ppc.integer() | ppc.signed_integer() | ppc.hex_integer()).set_name(
        "IntegerValue"
    )
    usonUnquotedString = (
        # pyp.rest_of_line()
        pyp.Regex(r"[^\", =\(\)\r\n0-9][^\", =\(\)\r\n]+").set_name(
            "usonUnquotedString"
        )
    )
    usonFloat = ppc.real.set_name("usonFloat")
    usonObject = pyp.Forward().set_name("usonObject")
    usonValue = pyp.Forward().set_name("usonValue")
    # DO NOT SCREW WITH THE ORDERING
    usonValue << (
        usonFloat
        | TRUE
        | FALSE
        | NONE
        | usonUnquotedString
        | usonInteger
        | usonString
        | usonObject
    )
    usonMemberDef = pyp.Group(Key + Equals + usonValue, aslist=True).set_name(
        "usonMemberDef"
    )
    usonMembers = pyp.delimited_list(usonMemberDef, delim=",").set_name(None)

    usonObject << pyp.Dict(
        OpenParen + pyp.Optional(usonMembers) + CloseParen, asdict=True
    )

    SectionMapBlock = ~OpenSquareBracket + Key + Equals + pyp.Empty() + usonValue
    SectionBody = pyp.Dict(pyp.ZeroOrMore(pyp.Group(SectionMapBlock)))
    Document = pyp.Dict(pyp.ZeroOrMore(pyp.Group(SectionHeader + SectionBody)))
    Document.ignore(Comment)

    return Document


SYNTAX = build_syntax()
