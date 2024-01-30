# sodom
__sodom__ if you like to write HTML in Python. __Faster x2~ than `dominate`__
## Installation
```bash
python -m pip install sodom[cli]
```

## Examples
You can check demo via `python -m sodom` or preview code in `sodom.__main__`.
```python
from sodom import *
...
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
...
```

Also added special operations:
```python
Attrs(foo='bar').merge(foo='baz')
Attrs(foo='bar').merge(**Attrs(foo='baz'))
Attrs(foo='bar').merge(**dict(foo='baz'))
Attrs(foo='bar') | Attrs(foo='baz')
Attrs(foo='bar') | {'foo': 'baz'}
# return `Attrs(foo='bar baz'})`

with div() < Attrs(foo='bar') as doc: ...
with div() < {'foo': 'bar'} as doc: ...
# return `<div foo="bar"></div>`

with div() < Attrs(foo='bar') | {'foo': 'baz'} as doc: ...
# return `<div foo="bar baz"></div>`

```

## CLI Generation
Require `[cli]` extra.
```bash
python -m pip install sodom[cli]
```
Check out `--help`.
```bash
python -m sodom --help
```

## Features
- supported standart html element (normal/void). Check `sodom.literals.NORMAL_TAGS` and `sodom.literals.VOID_TAGS`.
- by default, all underscores(`_`) will be replaced by minus(`-`). Use `replace_underscores` in renderers to replace only _special_ attributes like `data-`, `v-`... Check `sodom.literals.SPECIAL_ATTRS`. You can extend list in runtime __before__ library usage.
- sodom is x2~ times faster than `dominate` and x4+ times than `fast_html`. Check `sodom.tests.test_performance_*`.
- avoided builtin keyword trouble via cutting off leading and ending `_` of element names. For example, `[py]class_='button'` equals `[html]class="button"`. Check `python -m sodom demo` or `sodom.__main__.demo`
- supported `ContextVar`. Tested on `asyncio` and `ThreadPoolExecutor`.
- supported python generation from `.html`.
- include simple integrations with `aiohttp`, `flask`, `sanic`, `quart`. Check `sodom.ext.`

## Feedback
If you have any feedback, text me at inbox@protaz.ru
