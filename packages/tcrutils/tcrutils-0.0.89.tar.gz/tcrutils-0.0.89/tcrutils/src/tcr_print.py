from collections.abc import Generator, Iterable
from copy import deepcopy as copy
from typing import TypeAlias

from .tcr_color import c
from .tcr_constants import NEWLINE
from .tcr_int import hex
from .tcr_null import Null

PIRepassable: TypeAlias = (
  type(Null)
  | list
  | tuple
  | dict
  | set
  | Generator
  | range
  | bytes
  | bytearray
  | str
  | None
  | bool
  | int
)

# fmt: off
BRACKET_COLOR    = "Cyan"

COLON_COLOR      = "Orange\\_1"
COMMA_COLOR      = "Dark\\_gray"

B_COLOR          = "Red" # b''

TRUE_COLOR       = "Green"
FALSE_COLOR      = "Red"

NULL_COLOR       = "Dark\\_gray"
NONE_COLOR       = "Light\\_gray"

MORE_ITEMS_COLOR = "Purple\\_1B"
# fmt: on


def print_iterable(
  it: Iterable,
  *its: Iterable,
  recursive=True,
  raw=False,
  item_limit=100,
  syntax_highlighting=False,
  printhook=print,
) -> str | None:
  """Print an iterable in a nicely formatted way. If raw=True return the nicely formatted string instead of printing.

  Supports lists, tuples, sets, dicts, strings, generators, bytestrings, bytearrays and may work with other Iterables
  `item_limit` determines the limit of iterable items before it displays them instead of continuing to get more
  `syntax_highlighting` adds ansi codes to highlight syntax (may be buggy)
  """

  if its:
    return print_iterable(
      (it, *its),
      recursive=recursive,
      raw=raw,
      item_limit=item_limit,
      syntax_highlighting=syntax_highlighting,
    )

  def synhi_s(symbol):
    if not syntax_highlighting:
      return symbol
    # fmt: off
    colors = {
      ":": COLON_COLOR,
      ",": COMMA_COLOR,
      "[": BRACKET_COLOR,
      "]": BRACKET_COLOR,
      "{": BRACKET_COLOR,
      "}": BRACKET_COLOR,
      "(": BRACKET_COLOR,
      ")": BRACKET_COLOR,
      "<": BRACKET_COLOR,
      ">": BRACKET_COLOR,
      "b": B_COLOR,
      "?": B_COLOR,
    }
    # fmt: on

    return c(colors[symbol]) + symbol + c('reset')

  def synhi(ncstr, origitem: type) -> str:
    # fmt: off
    colors = {
      "str+": 'White',
      "str":  'gold',
      "int":  'Blue'
    }
    # fmt: on

    # input(f"> {ncstr!r} // {origitem!r} ({type(origitem)}) <")
    if not syntax_highlighting:
      return ncstr
    if origitem == 'more':
      return c(MORE_ITEMS_COLOR) + ncstr + c('reset')
    elif origitem is Null:
      return 'Null' if not syntax_highlighting else c(NULL_COLOR) + 'Null' + c('reset')
    elif origitem is None:
      return 'None' if not syntax_highlighting else c(NONE_COLOR) + 'None' + c('reset')
    elif origitem is True:
      return 'True' if not syntax_highlighting else c(TRUE_COLOR) + 'True' + c('reset')
    elif origitem is False:
      return 'False' if not syntax_highlighting else c(FALSE_COLOR) + 'False' + c('reset')
    elif isinstance(origitem, str):
      return f"{c(colors['str+'] if syntax_highlighting != '?' else B_COLOR)}{ncstr[0]}{c('reset')+c(colors['str'])}{ncstr[1:-1]}{c('reset')}{c(colors['str+'] if syntax_highlighting != '?' else B_COLOR)}{ncstr[-1]}{c('reset')}"
    elif isinstance(origitem, int):
      return f"{c(colors['int'])}{ncstr}{c('reset')}"
    elif isinstance(origitem, bytes):
      return f"{synhi_s('b')}{c(colors['str+'])}{ncstr[1]}{c('reset')+c(colors['str'])}{ncstr[2:-1]}{c('reset')}{c(colors['str+'])}{ncstr[-1]}{c('reset')}"

    return ncstr

  if it is Null:
    a = 'Null' if not syntax_highlighting else c(NULL_COLOR) + 'Null' + c('reset')
    return a if raw else print(a)

  if it is None:
    a = 'None' if not syntax_highlighting else c(NONE_COLOR) + 'None' + c('reset')
    return a if raw else print(a)

  if it is True:
    a = 'True' if not syntax_highlighting else c(TRUE_COLOR) + 'True' + c('reset')
    return a if raw else print(a)

  if it is False:
    a = 'False' if not syntax_highlighting else c(FALSE_COLOR) + 'False' + c('reset')
    return a if raw else print(a)

  if isinstance(it, str):
    it = repr(it)
    if syntax_highlighting:
      it = synhi(it, '')
    return it if raw else print(it)

  if isinstance(it, bytes):
    it = repr(it)
    if syntax_highlighting:
      it = synhi(it, b'')
    return it if raw else print(it)

  if isinstance(it, int):
    if not syntax_highlighting:
      return repr(it) if raw else print(it)
    return synhi(it, 1) if raw else print(synhi(it, 1))

  if it == []:
    if not raw:
      print(f'{synhi_s("[")}{synhi_s("]")}')
      return it
    return f'{synhi_s("[")}{synhi_s("]")}'

  if it == ():
    if not raw:
      print(f'{synhi_s("(")}{synhi_s(")")}')
      return it
    return f'{synhi_s("(")}{synhi_s(")")}'

  if it == {}:
    if not raw:
      print(f'{synhi_s("{")}{synhi_s("}")}')
      return it
    return f'{synhi_s("{")}{synhi_s("}")}'

  if it == set():
    if not raw:
      print(f'{synhi_s("{")}{synhi_s(",")}{synhi_s("}")}')
      return it
    return f'{synhi_s("{")}{synhi_s(",")}{synhi_s("}")}'

  orig_bytearray = False
  if isinstance(it, bytearray):
    orig_bytearray = True
    it = [synhi(hex(x), 1) for x in it]

  orig_bytes = False
  if isinstance(it, bytes):
    orig_bytes = True
    it = [chr(x) for x in it]

  def parenthesis(it: Iterable):
    # fmt: off
    parenthesis_lookup = {
      Generator: ('<', '>'),
      range:     ('<', '>'),
      list:      ('[', ']'),
      set:       ('{', '}'),
      dict:      ('{', '}'),
      tuple:     ('(', ')'),
      None:      ('(', ')'),
    }
    # fmt: on

    default = parenthesis_lookup.pop(None)

    for k, v in parenthesis_lookup.items():
      if isinstance(it, k):
        return tuple(synhi_s(x) for x in v)

    return default

  parenthesis = parenthesis(it)

  if isinstance(it, dict):
    text = parenthesis[0]
    for key, value in it.items():
      try:
        ovalu = copy(value)
      except TypeError:
        ovalu = value
      if recursive and isinstance(value, PIRepassable):
        value = print_iterable(
          value,
          raw=True,
          item_limit=item_limit,
          recursive=True,
          syntax_highlighting=syntax_highlighting,
        ).replace('\n', '\n  ')
      elif orig_bytearray:
        value = value
      elif orig_bytes:
        value = synhi(value, b'')
      else:
        value = synhi(repr(value), ovalu)
      text += f'\n  {synhi(repr(key), key)}{synhi_s(":")} {value}{synhi_s(",")}'
    text += f'\n{parenthesis[1]}'
  else:
    text = parenthesis[0]
    vals = 0
    addmore = True
    for value in it:
      if item_limit is not None and item_limit != -1 and vals >= item_limit:
        break
      vals += 1
      ovalu = copy(value)
      if recursive and isinstance(value, PIRepassable) and not orig_bytearray and not orig_bytes:
        value = print_iterable(
          value,
          raw=True,
          item_limit=item_limit,
          recursive=True,
          syntax_highlighting=syntax_highlighting,
        ).replace('\n', '\n  ')
      else:
        if orig_bytearray:
          pass
        elif orig_bytes:
          value = f'{synhi_s("b")}{value!r}'
        else:
          value = synhi(repr(value), ovalu)
      text += f'\n  {value}{synhi_s(",")}'
    else:
      addmore = False
    if addmore:
      try:
        ns = len(it) - item_limit
      except TypeError:
        ns = '?'
      text += f'\n  {synhi("(", "more")}{synhi(ns, 1)}{synhi(" more items...)", "more")}'
    text += f'\n{parenthesis[1]}'

  if raw:
    return text
  printhook(text)
  return it


def print_block(
  text: str,
  border_char: str = '#',
  *,
  margin: int = 1,
  border: int = 3,
  padding: int = 0,
  padding_top: int = 1,
  padding_bottom: int = 1,
  text_color: str = 'Gold',
  border_color: str = 'White',
  raw: bool = False,
  allow_invalid_config: bool = False,
) -> str | None:
  """Print or return a string of a "comment-like" block with text. Colors may optionally be set to `''` (empty string) to skip coloring of that part. Ends with a color reset unless none of the colors are enabled (both set to `''`).

  Params:
      - `margin`: The amount of spaces between the text and the inner walls (left-right only)
      - `border`: The width of walls (number of border_char characters, left-right only)
      - `padding`: The number of extra spaces added to the left of each line (left side only)
      - `padding_top` & `padding_bottom`: How many '\\n' characters to add at the beginning and the end of the string (top-bottom only)
  """

  text = str(text)

  if not allow_invalid_config and margin < 0 or border < 0 or padding < 0:
    msg = f'Invalid margin, border and/or padding(s) configuration {(margin, border, padding, padding_top, padding_bottom)!r}. Override this by passing in allow_invalid_config=True'
    raise ValueError(msg)

  if not allow_invalid_config and len(border_char) != 1:
    msg = f'border_char must be 1 character long (got {border_char!r} which is {len(border_char)!r} characters long). Override this by passing in allow_invalid_config=True'
    raise ValueError(msg)

  if text_color != '':
    text_color = c(text_color)
  if border_color != '':
    border_color = c(border_color)
  reset = c('reset')

  if not text_color and not border_color:
    reset = ''

  bar = f'{border_char * (border + margin + len(text) + margin + border)}'
  block = f"""
{padding_top * NEWLINE}{padding * ' '}{reset}{border_color}{bar}
{padding * ' '}{border * border_char}{reset}{margin * ' '}{text_color}{text}{reset}{margin * ' '}{border_color}{border * border_char}
{padding * ' '}{bar}{reset}{padding_bottom * NEWLINE}
"""[1:-1]
  if raw:
    return block

  print(block)
  return None
