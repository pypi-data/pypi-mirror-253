__license__ = '''
sodom
Copyright (C) 2023  Dmitry Protasov (inbox@protaz.ru)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from typing import Any, LiteralString, TypeGuard

from sodom.elements import ANY_ELEMENT, NORMAL_ELEMENT, VOID_ELEMENT
from sodom.literals import NORMAL_TAG_STRS, USED_TAG_VALUES, VOID_TAG_STRS, VOID_TAGS, NORMAL_TAGS


def text(*_text: str) -> None:
    from sodom.elements import CURRENT_ELEMENT
    if (elem := CURRENT_ELEMENT.get()) is not None and _text:
        elem.add(*_text)


def render_py(
    *elements: ANY_ELEMENT,
    level: int = 0,
    space: str = '    ',
    quotes: str = '"',
    replace_underscores: bool = True,
) -> str:
    result: list[str] = []
    for element in elements:
        if isinstance(element, str):
            result.append('{}{}(\'{}\')'.format(space * level, text.__name__, element))
        else:
            result.append(
                element.__py__(
                    level=level,
                    space=space,
                    quotes=quotes,
                    replace_underscores=replace_underscores,
                )
            )
    return '\n'.join(result)


def render(
    *elements: ANY_ELEMENT,
    level: int = 0,
    space: str = '  ',
    replace_underscores: bool = True,
) -> str:
    result: list[str] = []
    for element in elements:
        if isinstance(element, str):
            result.append(space * level + element)
        else:
            result.append(
                element.__html__(
                    level=level,
                    space=space,
                    replace_underscores=replace_underscores,
                )
            )
    return '\n'.join(result)


def render_root(
    *elements: ANY_ELEMENT,
    level: int = 0,
    space: str = '  ',
    replace_underscores: bool = True,
):
    return render(
        '<!DOCTYPE html>',
        *elements,
        level=level,
        space=space,
        replace_underscores=replace_underscores,
    )


def render_now(
    element: ANY_ELEMENT,
    level: int = 0,
    space: str = '  ',
    replace_underscores: bool = True,
):
    import tempfile
    import webbrowser

    tmp_file_path = tempfile.mktemp('.example1.html', 'sodom.')
    with open(tmp_file_path, 'w+') as f:
        root = render_root(
            element,
            level=level,
            space=space,
            replace_underscores=replace_underscores,
        )
        f.write(root)
    webbrowser.open_new_tab(tmp_file_path)


def escape_python(tag: LiteralString) -> str:
    '''Escape Python keywords and builtins.'''
    if tag.startswith(USED_TAG_VALUES):
        tag = f'{tag}_'
    return tag


def is_normal_element(element: Any) -> TypeGuard[NORMAL_ELEMENT]:
    from sodom.elements import NormalElement
    return isinstance(element, NormalElement)


def is_void_element(element: Any) -> TypeGuard[VOID_ELEMENT]:
    from sodom.elements import VoidElement
    return isinstance(element, VoidElement)


def is_tag(tag: str) -> TypeGuard[NORMAL_TAGS | VOID_TAGS]:
    return is_normal_tag(tag) or is_void_tag(tag)


def is_normal_tag(tag: str) -> TypeGuard[NORMAL_TAGS]:
    return tag in NORMAL_TAG_STRS


def is_void_tag(tag: str) -> TypeGuard[VOID_TAGS]:
    return tag in VOID_TAG_STRS
