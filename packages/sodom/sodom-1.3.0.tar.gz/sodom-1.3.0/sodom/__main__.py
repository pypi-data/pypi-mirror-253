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


from collections import deque
from pathlib import Path
from typing import cast

from sodom import *
from sodom.elements import ANY_ELEMENT, NORMAL_ELEMENT, VOID_ELEMENT, NormalElement, VoidElement
from sodom.utils import is_normal_element, is_normal_tag, is_void_tag, render_py

try:
    from lxml import etree as ETree
    from xml.etree.ElementTree import Element, ElementTree
    from typer import Typer
    from loguru import logger
except ImportError as e:
    raise ImportError('Please install modules required for cli usage `python -m pip install sodom[cli]`.') from e
else:
    cli = Typer()


    def _build_sodom_document(tree: ElementTree, include_empty_rows: bool) -> NORMAL_ELEMENT:
        xml_root = tree.getroot()
        xml_elems = deque[Element]()
        xml_elems.extend(xml_root)

        sodom_xml_map: dict[NORMAL_ELEMENT | VOID_ELEMENT, Element] = {}

        def build_sodom_element(xml_elem: Element) -> ANY_ELEMENT:
            html_tag = xml_elem.tag
            html_attrs = xml_elem.attrib
            text = (xml_elem.text or '').split('\n')
            text = (
                t.strip()
                for t in text
            )
            text = (
                t
                for t in text
                if bool(t) or include_empty_rows
            )

            if is_normal_tag(html_tag):
                sodom_elem = NormalElement(html_tag, *text, **html_attrs)
            elif is_void_tag(html_tag):
                sodom_elem = VoidElement(html_tag, **html_attrs)
            else:
                raise RuntimeError(f'Unknown tag: {html_tag}')
            sodom_xml_map[sodom_elem] = xml_elem
            return sodom_elem

        sodom_root = build_sodom_element(xml_root)
        if is_normal_element(sodom_root):
            current_sodom_parent = sodom_root
        else:
            raise RuntimeError(f'Invalid root type element: {type(sodom_root)}')

        while True:
            try:
                current_xml_element: Element = xml_elems.popleft()
                xml_elems.extendleft(reversed(current_xml_element))

                with current_sodom_parent:
                    new_element = build_sodom_element(current_xml_element)
                    if set(current_xml_element).intersection(xml_elems):
                        if is_normal_element(new_element):
                            current_sodom_parent = new_element
                        else:
                            raise RuntimeError('')

                    while not set(sodom_xml_map[current_sodom_parent]).intersection(xml_elems):
                        if current_sodom_parent.parent is not None:
                            current_sodom_parent = cast(NORMAL_ELEMENT, current_sodom_parent.parent)
                        else:
                            raise StopIteration()
            except StopIteration:
                break

        return sodom_root


    @cli.command(
        help='test',
        short_help='Generate python code via HTML (.html) file.',
    )
    def generator(source: Path, target: Path, dialect: str = 'sodom', include_empty_rows: bool = False):
        logger.info('Parsing source: {}', source)
        tree: ElementTree = ETree.parse(
            source,
            ETree.HTMLParser(
                remove_comments=True,
                remove_blank_text=True,
            ),
        )

        if dialect == 'sodom':
            logger.info('Building python structure via {}...', 'sodom')
            document = _build_sodom_document(tree, include_empty_rows)
            logger.info('Generating python code via {}...', 'sodom')
            code = render_py(document)
        else:
            raise ValueError(f'dialect must be {('sodom')}')

        logger.info('Writing {} target: {}', document, target)
        with open(target, 'w+') as f:
            f.write(code)
        for row in code.split('\n'):
            logger.info(row)
        logger.info('Done!')


    @cli.command()
    def demo():
        def example1():
            '''
            https://getbootstrap.com/docs/4.0/examples/pricing/
            '''
            def card(_header: str, _price: str, _submit_text: str, *_conditions: str):
                with div(class_='card mb-4 box-shadow'):
                    with div(class_='card-header'), h4(class_='my-0 font-weight-normal'):
                        text(_header)
                    with div(class_='card-body'):
                        with h1(class_='card-title pricing-card-title'):
                            text(_price)
                            with small(class_='text-muted'):
                                text(' mo')
                        with ul(class_='list-unstyled mt-3 mb-4'):
                            for _c in _conditions:
                                li(_c)
                        with button(type_='button', class_='btn btn-lg btn-block btn-primary'):
                            text(_submit_text)

            def footer_column(*_row: str):
                with div(class_='col-6 col-md'):
                    h5('Features')
                    with ul(class_='list-unstyled text-small'):
                        for _r in _row:
                            with li(), a(class_='text-muted', href='#'):
                                text(_r)

            with html(lang='en') as document:
                with head():
                    meta(charset='utf-8')
                    meta(name='viewport', content='width=device-width, initial-scale=1, shrink-to-fit=no')
                    meta(name='description', content='')
                    meta(name='author', content='')
                    link(rel='icon', href='/docs/4.0/assets/img/favicons/favicon.ico')
                    title('Pricing example for Bootstrap')
                    link(rel='canonical', href='https://getbootstrap.com/docs/4.0/examples/pricing/')
                    link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm', crossorigin='anonymous')
                    with style():
                        text('''html {
        font-size: 14px;
        }
        @media (min-width: 768px) {
        html {
            font-size: 16px;
        }
        }

        .container {
        max-width: 960px;
        }

        .pricing-header {
        max-width: 700px;
        }

        .card-deck .card {
        min-width: 220px;
        }

        .border-top { border-top: 1px solid #e5e5e5; }
        .border-bottom { border-bottom: 1px solid #e5e5e5; }

        .box-shadow { box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05); }
        ''')
                with body():
                    with div(class_='d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow'):
                        with h5(class_='my-0 mr-md-auto font-weight-normal'):
                            text('Company name')
                        with nav(class_='my-2 my-md-0 mr-md-3'):
                            with a(class_='p-2 text-dark', href='#'):
                                text('Features')
                            with a(class_='p-2 text-dark', href='#'):
                                text('Enterprise')
                            with a(class_='p-2 text-dark', href='#'):
                                text('Support')
                            with a(class_='p-2 text-dark', href='#'):
                                text('Pricing')
                        with a(class_='btn btn-outline-primary', href='#'):
                            text('Sign up')
                    with div(class_='pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center'):
                        with h1(class_='display-4'):
                            text('Pricing')
                        with p(class_='lead'):
                            text('Quickly build an effective pricing table for your potential customers with this Bootstrap example.')
                            text('It\'s built with default Bootstrap components and utilities with little customization.')
                    with div(class_='container'):
                        with div(class_='card-deck mb-3 text-center'):
                            card(
                                'Free',
                                '$0 ',
                                'Sign up for free',
                                '10 users included',
                                '2 GB of storage',
                                'Email support',
                                'Help center access',
                            )
                            card(
                                'Pro',
                                '$15 ',
                                'Get started',
                                '20 users included',
                                '10 GB of storage',
                                'Priority email support',
                                'Help center access',
                            )
                            card(
                                'Enterprise',
                                '$29 ',
                                'Contact us',
                                '10 users included',
                                '2 GB of storage',
                                'Email support',
                                'Help center access',
                            )

                        with footer(class_='pt-4 my-md-5 pt-md-5 border-top'):
                            with div(class_='row'):
                                with div(class_='col-12 col-md'):
                                    img(class_='mb-2', src='https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg', alt='', width='24', height='24')
                                    with small(class_='d-block mb-3 text-muted'):
                                        text('&copy; 2017-2018')
                                footer_column(
                                    'Cool stuff',
                                    'Random feature',
                                    'Team feature',
                                    'Stuff for developers',
                                    'Another one',
                                    'Last time',
                                )
                                footer_column(
                                    'Resource',
                                    'Resource name',
                                    'Another resource',
                                    'Final resource',
                                )
                                footer_column(
                                    'Team',
                                    'Locations',
                                    'Privacy',
                                    'Terms',
                                )

                    script(
                        src="https://code.jquery.com/jquery-3.2.1.slim.min.js",
                        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN",
                        crossorigin="anonymous",
                    )
                    script(src="https://code.jquery.com/jquery-3.2.1.slim.min.js", integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN", crossorigin="anonymous")
                    script(src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js", integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q", crossorigin="anonymous")
                    script(src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js", integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl", crossorigin="anonymous")
                    script(src="https://cdn.jsdelivr.net/npm/holderjs@2.9.9/holder.min.js")
                    script('''Holder.addTheme('thumb', {bg: '#55595c', fg: '#eceeef', text: 'Thumbnail'});''')
            return render_root(document)

        import tempfile
        import webbrowser

        example1_html = example1()
        tmp_file_path = tempfile.mktemp('.example1.html', 'sodom.')
        with open(tmp_file_path, 'w+') as f:
            f.write(example1_html)
        webbrowser.open_new_tab(tmp_file_path)


    if __name__ == '__main__':
        cli()
