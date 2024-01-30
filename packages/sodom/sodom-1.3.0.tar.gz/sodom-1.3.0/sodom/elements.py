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


from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from contextvars import ContextVar, Token
from typing import Any, MutableSequence, Self, Sequence

from sodom.attrs import Attrs
from sodom.literals import ANY_TAGS, NORMAL_TAGS, VOID_TAGS


CURRENT_ELEMENT = ContextVar['NORMAL_ELEMENT | None']("CURRENT_ELEMENT", default=None)


def opening_tag_content(
    tag: ANY_TAGS,
    attrs: Attrs,
    quotes: str = '"',
    replace_underscores: bool = True,
) -> str:
    result = ' '.join(filter(
        bool,
        (tag, attrs.torow(quotes=quotes, replace_underscores=replace_underscores))
    ))

    return result


_tag_begin_form = '{}<{}>'.format
_tag_end_form = '</{}>'.format


class HTMLElement[TAG: ANY_TAGS](ABC):
    tag: TAG
    attrs: Attrs
    parent: 'HasChildren | None'

    def __lt__(self, others: Attrs | dict[str, str] | Sequence[Attrs | dict[str, str]]) -> Self:
        if isinstance(others, dict):
            others = (others,)
        for other in others:
            self.attrs.merge_update(**other)
        return self

    def __call__(self) -> None:
        new_parent = CURRENT_ELEMENT.get()
        if new_parent is not None:
            new_parent.add(self)
        else:
            self.parent = None

    @abstractmethod
    def __html__(
        self,
        *,
        level: int = 0,
        space: str = '  ',
        replace_underscores: bool = True,
    ) -> str:
        ...

    @abstractmethod
    def __py__(
        self,
        *,
        level: int = 0,
        space: str = '    ',
        quotes: str = '"',
        replace_underscores: bool = True
    ) -> str:
        ...


class HasChildren(ABC):
    _children: MutableSequence['ANY_ELEMENT']

    @property
    def children(self) -> Sequence['ANY_ELEMENT']:
        return tuple(self._children)

    def add(self, *children: 'ANY_ELEMENT') -> None:
        for child in children:
            if isinstance(child, HTMLElement):
                if child.parent is not None:
                    child.parent.remove(child)
                child.parent = self
        self._children.extend(children)

    def remove(self, *children: 'ANY_ELEMENT') -> None:
        for child in children:
            if isinstance(child, (NormalElement, VoidElement)):
                child.parent = None
            self._children.remove(child)


class VoidElement[HTML_TAGS: VOID_TAGS](HTMLElement[HTML_TAGS]):
    __slots__ = (
        'tag',
        'attrs',
        'parent',
    )

    def __init__(self, _tag: HTML_TAGS, *_: Any, **attrs: str) -> None:
        self.tag = _tag
        self.attrs = Attrs(attrs)
        self.parent = None
        self()

    ##### RENDERING #####
    def __str__(self) -> str:
        return self.__repr__()

    def __html__(
        self,
        *,
        level: int = 0,
        space: str = '  ',
        replace_underscores: bool = True,
    ) -> str:
        tag_content = opening_tag_content(
            self.tag,
            self.attrs,
            replace_underscores=replace_underscores,
        )
        result = _tag_begin_form(space * level, tag_content)
        return result

    def __py__(
        self,
        *,
        level: int = 0,
        space: str = '    ',
        quotes: str = '"',
        replace_underscores: bool = True
    ) -> str:
        from sodom.utils import escape_python

        attrs = self.attrs.torow(
            ', ',
            quotes=quotes,
            replace_underscores=replace_underscores,
        )

        result = '{}{}({})'.format(space * level, escape_python(self.tag), attrs)
        return result

    def __repr__(self) -> str:
        tag_content = opening_tag_content(self.tag, self.attrs)
        result = '<{} @{}>'.format(tag_content, id(self))
        return result


class NormalElement[TAG: NORMAL_TAGS](
    AbstractContextManager, # type: ignore
    HTMLElement[TAG],
    HasChildren,
):
    __slots__ = (
        'tag',
        'attrs',
        'parent',
        '_children',
        '_context_token',
    )

    _context_token: Token['NORMAL_ELEMENT | None']

    def __init__(self, _tag: TAG, *_children: 'ANY_ELEMENT', **attrs: str) -> None:
        self.tag = _tag
        self.attrs = Attrs(attrs)
        self.parent = None
        self()
        self._children = []
        self.add(*_children)

    ##### CONTEXT MANAGEMENT #####
    def __enter__(self) -> Self:
        self._context_token = CURRENT_ELEMENT.set(self)
        return self

    def __exit__(self, *_) -> None:
        CURRENT_ELEMENT.reset(self._context_token)

    ##### RENDERING #####
    def __str__(self) -> str:
        return self.__repr__()

    def __html__(
        self,
        *,
        level: int = 0,
        space: str = '  ',
        replace_underscores: bool = True,
    ) -> str:
        from sodom.utils import render as _render

        tag_content = opening_tag_content(
            self.tag,
            self.attrs,
            replace_underscores=replace_underscores,
        )

        tag_begin = _tag_begin_form(space * level, tag_content)
        body_content = '\n'.join(map(
            lambda c: _render(c, level=level+1, space=space, replace_underscores=replace_underscores),
            self._children,
        ))
        tag_end = _tag_end_form(self.tag)

        if body_content:
            tag_end = space * level + tag_end

        result = ('\n' if body_content else '').join((
            tag_begin,
            body_content,
            tag_end,
        ))
        return result

    def __py__(
        self,
        *,
        level: int = 0,
        space: str = '    ',
        quotes: str = '"',
        replace_underscores: bool = True
    ) -> str:
        from sodom.utils import escape_python, render_py

        attrs = self.attrs.torow(
            ', ',
            quotes=quotes,
            replace_underscores=replace_underscores,
        )

        if self._children:
            children = render_py(
                *self._children,
                level=level+1,
                space=space,
                quotes=quotes,
                replace_underscores=replace_underscores,
            )

            result = '{}with {}({}):\n{}'.format(
                space * level,
                escape_python(self.tag),
                attrs,
                children,
            )
        else:
            result = '{}{}({})'.format(
                space * level,
                escape_python(self.tag),
                attrs,
            )

        return result

    def __repr__(self) -> str:
        tag = self.tag
        tag_content = opening_tag_content(self.tag, self.attrs)
        body_content = len(self._children)

        result = '<{} @{}>:{}</{}>'.format(
            tag_content,
            id(self),
            body_content,
            tag,
        )

        return result


VOID_ELEMENT = VoidElement[VOID_TAGS]
NORMAL_ELEMENT = NormalElement[NORMAL_TAGS]
type ANY_ELEMENT = HTMLElement[Any] | str
