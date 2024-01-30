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


import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep, time as time_
from uuid import uuid4
import pytest

from sodom import literals
from sodom.attrs import Attrs
from sodom.elements import VOID_ELEMENT, NormalElement, VoidElement
from sodom.utils import is_normal_tag, is_void_tag, render, render_py, render_root
from sodom.partial import prebuild
from sodom import *
import sodom


def _build_attrs(join: str = ' ', **attrs: str):
    remove = list[str]()
    new_attrs = dict[str, str]()
    for k, v in attrs.items():
        if (spec_attr := k.split('_', 1)[0]) in literals.SPECIAL_ATTRS:
            remove.append(k)
            k = k.replace(f'{spec_attr}_', f'{spec_attr}-')
            new_attrs[k] = v
    for k in remove:
        attrs.pop(k)
    attrs |= new_attrs

    return join.join(f'{k}="{v}"'for k, v in attrs.items())


def _rand_attr():
    return {
        str(uuid4()): str(uuid4())
    }


class TestVoidElement:
    def test_render_with_tag(self):
        elem = hr()
        assert '<hr>' == render(elem)

    def test_render_with_attrs(self):
        elem = hr(test1='test1', test2='test2', test3='test3')
        assert '<hr test1="test1" test2="test2" test3="test3">' == render(elem)

    def test_str(self):
        h = hr()
        assert (
            '<hr @{}>'.format(id(h))
        ) == str(h)

    def test_parent_changing(self):
        h = hr()

        with div() as d1:
            h()
        assert h.parent == d1
        assert h in d1.children

        with div() as d2:
            h()
        assert h.parent == d2
        assert h in d2.children

    def test_used_tag_values(self):
        for tag in literals.USED_TAG_VALUES:
            if is_void_tag(tag):
                elem = VOID_ELEMENT(tag)
                assert (
                    f'{tag}_()'
                ) == render_py(elem)


class TestNormalElement:
    def test_render_with_tag(self):
        elem = div()
        assert '<div></div>' == render(elem)

    def test_render_with_attrs(self):
        elem = div(test1='test1', test2='test2', test3='test3')
        assert '<div test1="test1" test2="test2" test3="test3"></div>' == render(elem)

    def test_render_with_children_via_args(self):
        attr0 = _rand_attr()

        attr01 = _rand_attr()
        attr02 = _rand_attr()
        attr03 = _rand_attr()

        attr031 = _rand_attr()
        attr032 = _rand_attr()
        attr033 = _rand_attr()

        elem = div(
            '_',
            div(**attr01),
            div(**attr02),
            div(
                div(**attr031),
                div(**attr032),
                div(**attr033),
                **attr03,
            ),
            **attr0,
        )
        assert (
            f'<div {_build_attrs(**attr0)}>\n'
            '  _\n'
            f'  <div {_build_attrs(**attr01)}></div>\n'
            f'  <div {_build_attrs(**attr02)}></div>\n'
            f'  <div {_build_attrs(**attr03)}>\n'
            f'    <div {_build_attrs(**attr031)}></div>\n'
            f'    <div {_build_attrs(**attr032)}></div>\n'
            f'    <div {_build_attrs(**attr033)}></div>\n'
            '  </div>\n'
            '</div>'
        ) == render(elem)

    def test_render_with_children_via_context(self):
        attr0 = _rand_attr()

        attr01 = _rand_attr()
        attr02 = _rand_attr()
        attr03 = _rand_attr()

        attr031 = _rand_attr()
        attr032 = _rand_attr()
        attr033 = _rand_attr()

        with div('_', **attr0) as elem:
            div(**attr01)
            div(**attr02)
            with div(**attr03):
                div(**attr031)
                div(**attr032)
                div(**attr033)

        assert (
            f'<div {_build_attrs(**attr0)}>\n'
            '  _\n'
            f'  <div {_build_attrs(**attr01)}></div>\n'
            f'  <div {_build_attrs(**attr02)}></div>\n'
            f'  <div {_build_attrs(**attr03)}>\n'
            f'    <div {_build_attrs(**attr031)}></div>\n'
            f'    <div {_build_attrs(**attr032)}></div>\n'
            f'    <div {_build_attrs(**attr033)}></div>\n'
            '  </div>\n'
            '</div>'
        ) == render(elem)

    def test_class_with_children(self):
        child = NormalElement('div',
            NormalElement('div',
                NormalElement('div'),
            ),
            NormalElement('div'),
            NormalElement('div',
                VoidElement('hr'),
                '',
            ),
        )
        assert (
            '<div>\n'
            '  <div>\n'
            '    <div></div>\n'
            '  </div>\n'
            '  <div></div>\n'
            '  <div>\n'
            '    <hr>\n'
            '    \n'
            '  </div>\n'
            '</div>'
        ) == render(child)

    def test_render_partial_element_with_context(self):
        with div() as d:
            hr()

        assert (
            '<div>\n'
            '  <hr>\n'
            '</div>'
        ) == render(d)

    def test_build_special_attrs(self):
        attrs = {
            **_rand_attr(),
            **_rand_attr(),
            **_rand_attr(),
        }

        d = div(**attrs)

        assert (
            f'<div {_build_attrs(**attrs)}></div>'
        ) == render(d)

    def test_str(self):
        d = div()
        assert (
            '<div @{}>:0</div>'.format(id(d))
        ) == str(d)

        d = div(div(), attr='attr')
        assert (
            '<div attr="attr" @{}>:1</div>'.format(id(d))
        ) == str(d)

    def test_add_children(self):
        d = div()
        h = hr()
        d.add(h)
        assert h in d.children
        assert h.parent == d

    def test_remove_children(self):
        h = hr()
        d = div(h)
        d.remove(h)
        assert h not in d.children
        assert h.parent is None
        h = hr()

        with div() as d1:
            h()
        assert h.parent == d1
        assert h in d1.children

        with div() as d2:
            h()
        assert h.parent == d2
        assert h in d2.children

    def test_used_tag_values(self):
        for tag in literals.USED_TAG_VALUES:
            if is_normal_tag(tag):
                elem = NormalElement(tag)
                assert (
                    f'{tag}_()'
                ) == render_py(elem)

    def test_normal_lt_attr_operation(self):
        attr0 = Attrs(foo='bar')

        with div() < attr0 as doc: pass

        assert doc.attrs['foo'] == attr0['foo']

    def test_normal_lt_sequence_operation(self):
        attr0 = Attrs(foo='bar')
        attr1 = Attrs(foo='baz')

        with div() < (attr0, attr1) as doc: pass

        assert doc.attrs['foo'] == f'{attr0['foo']} {attr1['foo']}'

    def test_call_attr_with_context(self):
        attr0 = Attrs(foo='bar')
        attr1 = Attrs(foo='baz')

        with div() as doc:
            attr0()
            attr1()

        assert doc.attrs['foo'] == f'{attr0['foo']} {attr1['foo']}'

    def test_empty_attr_adding(self):
        with div() as doc:
            Attrs(disabled='')()
        assert (
            '<div disabled></div>'
        ) == render(doc)

    def test_empty_attr_removing(self):
        doc = div() < {'disabled': ''}
        doc.attrs.pop('disabled')
        assert (
            '<div></div>'
        ) == render(doc)


class TestUtils:
    def test_document(self):
        d = div()
        assert (
            '<!DOCTYPE html>\n'
            + render(d)
        ) == render_root(d)

    def test_text(self):
        text_data = str(uuid4())
        with div() as d:
            text(text_data)
        assert text_data in d.children

    def test_render_py(self):
        attr = {
            'foo': 'bar',
            'data_baz': 'qux',
        }

        with div(**attr) as d:
            hr(**attr)
            text('')

        assert (
            f'with div({_build_attrs(', ', **attr)}):\n'
            f'    hr({_build_attrs(', ', **attr)})\n'
            f'    text(\'\')'
        ) == render_py(d, replace_underscores=False)

    def test_prebuild_element(self):
        attrs = {
            **_rand_attr(),
            **_rand_attr(),
            **_rand_attr(),
        }

        partial_test_hr = prebuild(VoidElement[literals.HR])

        test_hr = partial_test_hr(**attrs)

        assert 'hr' == test_hr.tag
        for k in attrs:
            assert test_hr.attrs[k] == attrs[k]

    def test_prebuild_prebuild(self):
        alone_attr_key0, alone_attr_value0 = list(_rand_attr().items())[0]
        alone_attr_key1, alone_attr_value1 = list(_rand_attr().items())[0]
        attrs = {
            **_rand_attr(),
            **_rand_attr(),
            **_rand_attr(),
        }

        partial_test_hr = prebuild(hr, **attrs, **{alone_attr_key1: alone_attr_value1})

        test_hr = partial_test_hr(**{alone_attr_key0: alone_attr_value0}, **{alone_attr_key1: alone_attr_value1})

        assert 'hr' == test_hr.tag
        assert test_hr.attrs[alone_attr_key0] == alone_attr_value0
        assert test_hr.attrs[alone_attr_key1] == f'{alone_attr_value1} {alone_attr_value1}'
        for k in attrs:
            assert test_hr.attrs[k] == attrs[k]


@pytest.mark.asyncio
async def test_building_html_in_two_tasks():
    async def task1():
        with div() as d:
            text('task1')
            await asyncio.sleep(2)
            text('task1')
        return d

    async def task2():
        with div() as d:
            text('task2')
            await asyncio.sleep(5)
            text('task2')
        return d

    div1, div2 = await asyncio.gather(
        task1(),
        task2(),
    )

    assert div1.children[0] == 'task1'
    assert div1.children[1] == 'task1'
    assert div2.children[0] == 'task2'
    assert div2.children[1] == 'task2'


def test_building_html_in_two_threads():
    def task1():
        with div() as d:
            text('task1')
            sleep(2)
            text('task1')
        return d

    def task2():
        with div() as d:
            text('task2')
            sleep(5)
            text('task2')
        return d

    with ThreadPoolExecutor(2) as pool:
        t1 = pool.submit(task1)
        t2 = pool.submit(task2)
        div1 = t1.result()
        div2 = t2.result()

    assert div1.children[0] == 'task1'
    assert div1.children[1] == 'task1'
    assert div2.children[0] == 'task2'
    assert div2.children[1] == 'task2'


def _dominate_case():
    with dominate_tags.body() as root:
        with dominate_tags.div(cls='d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow'):
            with dominate_tags.h5(cls='my-0 mr-md-auto font-weight-normal'):
                dominate_text('Company name')
            with dominate_tags.nav(cls='my-2 my-md-0 mr-md-3'):
                with dominate_tags.a(cls='p-2 text-dark', href='#'):
                    dominate_text('Features')
                with dominate_tags.a(cls='p-2 text-dark', href='#'):
                    dominate_text('Enterprise')
                with dominate_tags.a(cls='p-2 text-dark', href='#'):
                    dominate_text('Support')
                with dominate_tags.a(cls='p-2 text-dark', href='#'):
                    dominate_text('Pricing')
    return root.render('')


def _sodom_case():
    with sodom.body() as root:
        with sodom.div(class_='d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow'):
            with sodom.h5(class_='my-0 mr-md-auto font-weight-normal'):
                sodom.text('Company name')
            with sodom.nav(class_='my-2 my-md-0 mr-md-3'):
                with sodom.a(class_='p-2 text-dark', href='#'):
                    text('Features')
                with sodom.a(class_='p-2 text-dark', href='#'):
                    text('Enterprise')
                with sodom.a(class_='p-2 text-dark', href='#'):
                    text('Support')
                with sodom.a(class_='p-2 text-dark', href='#'):
                    text('Pricing')
    return render(root, space='')


def _fast_html_case():
    root = fast_html.body(
        fast_html.div(
            class_='d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow',
            i=(
                fast_html.h5(
                    'Company name'
                ),
                fast_html.nav(
                    class_='my-2 my-md-0 mr-md-3',
                    i=(
                        fast_html.a('Features', class_='p-2 text-dark', href='#'),
                        fast_html.a('Enterprise', class_='p-2 text-dark', href='#'),
                        fast_html.a('Support', class_='p-2 text-dark', href='#'),
                        fast_html.a('Pricing', class_='p-2 text-dark', href='#'),
                    )
                ),
            ),
        )
    )
    return fast_html.render(root)


try:
    from dominate import tags as dominate_tags
    from dominate.util import text as dominate_text
except ImportError:
    pass
else:
    def test_performance_dominate():
        # d = dominate_case()
        # s = sodom_case()

        dominate_case_total_time = 0
        for _ in range(10_000):
            start = time_()
            _dominate_case()
            dominate_case_total_time += time_() - start

        sodom_case_total_time = 0
        for _ in range(10_000):
            start = time_()
            _sodom_case()
            sodom_case_total_time += time_() - start

        result = round((dominate_case_total_time / sodom_case_total_time) * 100)
        assert result >= 100


try:
    import fast_html
except ImportError:
    pass
else:
    def test_performance_fast_html():
        # f = fast_html_case()
        # s = sodom_case()

        fast_html_total_time = 0
        for _ in range(10_000):
            start = time_()
            _fast_html_case()
            fast_html_total_time += time_() - start

        sodom_case_total_time = 0
        for _ in range(10_000):
            start = time_()
            _sodom_case()
            sodom_case_total_time += time_() - start

        result = round((fast_html_total_time / sodom_case_total_time) * 100)
        assert result >= 100

try:
    from aiohttp import web
    from sodom.ext import aiohttp as aiohttp_
except ImportError as e:
    print(e)
else:
    def test_aiohttp():
        attr0 = _rand_attr()

        attr01 = _rand_attr()
        attr02 = _rand_attr()
        attr03 = _rand_attr()

        attr031 = _rand_attr()
        attr032 = _rand_attr()
        attr033 = _rand_attr()

        with div('_', **attr0) as root:
            div(**attr01)
            div(**attr02)
            with div(**attr03):
                div(**attr031)
                div(**attr032)
                div(**attr033)
        response = aiohttp_.sodom_response(root)

        assert isinstance(response, web.Response)
        assert (
            '<!DOCTYPE html>\n'
            f'<div {_build_attrs(**attr0)}>\n'
            '  _\n'
            f'  <div {_build_attrs(**attr01)}></div>\n'
            f'  <div {_build_attrs(**attr02)}></div>\n'
            f'  <div {_build_attrs(**attr03)}>\n'
            f'    <div {_build_attrs(**attr031)}></div>\n'
            f'    <div {_build_attrs(**attr032)}></div>\n'
            f'    <div {_build_attrs(**attr033)}></div>\n'
            '  </div>\n'
            '</div>'
        ) == response.text

try:
    from flask import Response
    from sodom.ext import flask as flask_
except ImportError as e:
    print(e)
else:
    def test_flask():

        attr0 = _rand_attr()

        attr01 = _rand_attr()
        attr02 = _rand_attr()
        attr03 = _rand_attr()

        attr031 = _rand_attr()
        attr032 = _rand_attr()
        attr033 = _rand_attr()

        with div('_', **attr0) as root:
            div(**attr01)
            div(**attr02)
            with div(**attr03):
                div(**attr031)
                div(**attr032)
                div(**attr033)
        response = flask_.sodom_response(root)

        assert isinstance(response, Response)
        assert (
            '<!DOCTYPE html>\n'
            f'<div {_build_attrs(**attr0)}>\n'
            '  _\n'
            f'  <div {_build_attrs(**attr01)}></div>\n'
            f'  <div {_build_attrs(**attr02)}></div>\n'
            f'  <div {_build_attrs(**attr03)}>\n'
            f'    <div {_build_attrs(**attr031)}></div>\n'
            f'    <div {_build_attrs(**attr032)}></div>\n'
            f'    <div {_build_attrs(**attr033)}></div>\n'
            '  </div>\n'
            '</div>'
        ) == ''.join((r.decode() for r in response.response if isinstance(r, (bytes, bytearray))))

try:
    import quart
    from sodom.ext import quart as quart_
except ImportError as e:
    print(e)
else:
    @pytest.mark.asyncio
    async def test_quart():

        attr0 = _rand_attr()

        attr01 = _rand_attr()
        attr02 = _rand_attr()
        attr03 = _rand_attr()

        attr031 = _rand_attr()
        attr032 = _rand_attr()
        attr033 = _rand_attr()

        with div('_', **attr0) as root:
            div(**attr01)
            div(**attr02)
            with div(**attr03):
                div(**attr031)
                div(**attr032)
                div(**attr033)
        response = quart_.sodom_response(root)

        assert isinstance(response, quart.Response)
        assert (
            '<!DOCTYPE html>\n'
            f'<div {_build_attrs(**attr0)}>\n'
            '  _\n'
            f'  <div {_build_attrs(**attr01)}></div>\n'
            f'  <div {_build_attrs(**attr02)}></div>\n'
            f'  <div {_build_attrs(**attr03)}>\n'
            f'    <div {_build_attrs(**attr031)}></div>\n'
            f'    <div {_build_attrs(**attr032)}></div>\n'
            f'    <div {_build_attrs(**attr033)}></div>\n'
            '  </div>\n'
            '</div>'
        ) == await response.get_data(as_text=True)


try:
    from sanic.response.types import HTTPResponse
    from sodom.ext import sanic as sanic_
except ImportError as e:
    print(e)
else:
    def test_sanic():
        attr0 = _rand_attr()

        attr01 = _rand_attr()
        attr02 = _rand_attr()
        attr03 = _rand_attr()

        attr031 = _rand_attr()
        attr032 = _rand_attr()
        attr033 = _rand_attr()

        with div('_', **attr0) as root:
            div(**attr01)
            div(**attr02)
            with div(**attr03):
                div(**attr031)
                div(**attr032)
                div(**attr033)
        response = sanic_.sodom_response(root)

        assert isinstance(response, HTTPResponse)
        assert (
            '<!DOCTYPE html>\n'
            f'<div {_build_attrs(**attr0)}>\n'
            '  _\n'
            f'  <div {_build_attrs(**attr01)}></div>\n'
            f'  <div {_build_attrs(**attr02)}></div>\n'
            f'  <div {_build_attrs(**attr03)}>\n'
            f'    <div {_build_attrs(**attr031)}></div>\n'
            f'    <div {_build_attrs(**attr032)}></div>\n'
            f'    <div {_build_attrs(**attr033)}></div>\n'
            '  </div>\n'
            '</div>'
        ).encode() == response.body
