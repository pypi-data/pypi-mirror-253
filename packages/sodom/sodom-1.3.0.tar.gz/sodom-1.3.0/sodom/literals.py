from typing import Any, Literal, get_args


def _init_tags(TAGS: Any) -> tuple[str, ...]:
    result = list[str]()
    for l in get_args(TAGS):
        result.extend(get_args(l))
    return tuple(result)


A = Literal['a']
ABBR = Literal['abbr']
ACRONYM = Literal['acronym']
ADDRESS = Literal['address']
ARTICLE = Literal['article']
ASIDE = Literal['aside']
AUDIO = Literal['audio']
B = Literal['b']
BDI = Literal['bdi']
BDO = Literal['bdo']
BIG = Literal['big']
BLOCKQUOTE = Literal['blockquote']
BODY = Literal['body']
BUTTON = Literal['button']
CANVAS = Literal['canvas']
CAPTION = Literal['caption']
CENTER = Literal['center']
CITE = Literal['cite']
CODE = Literal['code']
COLGROUP = Literal['colgroup']
DATA = Literal['data']
DATALIST = Literal['datalist']
DD = Literal['dd']
DEL = Literal['del']
DETAILS = Literal['details']
DFN = Literal['dfn']
DIALOG = Literal['dialog']
DIR = Literal['dir']
DIV = Literal['div']
DL = Literal['dl']
DT = Literal['dt']
EM = Literal['em']
FIELDSET = Literal['fieldset']
FIGCAPTION = Literal['figcaption']
FIGURE = Literal['figure']
FONT = Literal['font']
FOOTER = Literal['footer']
FORM = Literal['form']
FRAME = Literal['frame']
FRAMESET = Literal['frameset']
H1 = Literal['h1']
H2 = Literal['h2']
H3 = Literal['h3']
H4 = Literal['h4']
H5 = Literal['h5']
H6 = Literal['h6']
HEAD = Literal['head']
HEADER = Literal['header']
HGROUP = Literal['hgroup']
HTML = Literal['html']
I = Literal['i']
IFRAME = Literal['iframe']
IMAGE = Literal['image']
INS = Literal['ins']
KBD = Literal['kbd']
LABEL = Literal['label']
LEGEND = Literal['legend']
LI = Literal['li']
MAIN = Literal['main']
MAP = Literal['map']
MARK = Literal['mark']
MARQUEE = Literal['marquee']
MENU = Literal['menu']
MENUITEM = Literal['menuitem']
METER = Literal['meter']
NAV = Literal['nav']
NOBR = Literal['nobr']
NOEMBED = Literal['noembed']
NOFRAMES = Literal['noframes']
NOSCRIPT = Literal['noscript']
OBJECT = Literal['object']
OL = Literal['ol']
OPTGROUP = Literal['optgroup']
OPTION = Literal['option']
OUTPUT = Literal['output']
P = Literal['p']
PICTURE = Literal['picture']
PLAINTEXT = Literal['plaintext']
PORTAL = Literal['portal']
PRE = Literal['pre']
PROGRESS = Literal['progress']
Q = Literal['q']
RB = Literal['rb']
RP = Literal['rp']
RT = Literal['rt']
RTC = Literal['rtc']
RUBY = Literal['ruby']
S = Literal['s']
SAMP = Literal['samp']
SCRIPT = Literal['script']
SEARCH = Literal['search']
SECTION = Literal['section']
SELECT = Literal['select']
SLOT = Literal['slot']
SMALL = Literal['small']
SPAN = Literal['span']
STRIKE = Literal['strike']
STRONG = Literal['strong']
STYLE = Literal['style']
SUB = Literal['sub']
SUMMARY = Literal['summary']
SUP = Literal['sup']
TABLE = Literal['table']
TBODY = Literal['tbody']
TD = Literal['td']
TEMPLATE = Literal['template']
TEXTAREA = Literal['textarea']
TFOOT = Literal['tfoot']
TH = Literal['th']
THEAD = Literal['thead']
TIME = Literal['time']
TITLE = Literal['title']
TR = Literal['tr']
TT = Literal['tt']
U = Literal['u']
UL = Literal['ul']
VAR = Literal['var']
VIDEO = Literal['video']
XMP = Literal['xmp']

AREA = Literal['area']
BASE = Literal['base']
BR = Literal['br']
COL = Literal['col']
EMBED = Literal['embed']
HR = Literal['hr']
IMG = Literal['img']
INPUT = Literal['input']
LINK = Literal['link']
META = Literal['meta']
PARAM = Literal['param']
SOURCE = Literal['source']
TRACK = Literal['track']
WBR = Literal['wbr']

NORMAL_TAGS = (
    A
    | ABBR
    | ACRONYM
    | ADDRESS
    | ARTICLE
    | ASIDE
    | AUDIO
    | B
    | BDI
    | BDO
    | BIG
    | BLOCKQUOTE
    | BODY
    | BUTTON
    | CANVAS
    | CAPTION
    | CENTER
    | CITE
    | CODE
    | COLGROUP
    | DATA
    | DATALIST
    | DD
    | DEL
    | DETAILS
    | DFN
    | DIALOG
    | DIR
    | DIV
    | DL
    | DT
    | EM
    | FIELDSET
    | FIGCAPTION
    | FIGURE
    | FONT
    | FOOTER
    | FORM
    | FRAME
    | FRAMESET
    | H1
    | H2
    | H3
    | H4
    | H5
    | H6
    | HEAD
    | HEADER
    | HGROUP
    | HTML
    | I
    | IFRAME
    | IMAGE
    | INS
    | KBD
    | LABEL
    | LEGEND
    | LI
    | MAIN
    | MAP
    | MARK
    | MARQUEE
    | MENU
    | MENUITEM
    | METER
    | NAV
    | NOBR
    | NOEMBED
    | NOFRAMES
    | NOSCRIPT
    | OBJECT
    | OL
    | OPTGROUP
    | OPTION
    | OUTPUT
    | P
    | PICTURE
    | PLAINTEXT
    | PORTAL
    | PRE
    | PROGRESS
    | Q
    | RB
    | RP
    | RT
    | RTC
    | RUBY
    | S
    | SAMP
    | SCRIPT
    | SEARCH
    | SECTION
    | SELECT
    | SLOT
    | SMALL
    | SPAN
    | STRIKE
    | STRONG
    | STYLE
    | SUB
    | SUMMARY
    | SUP
    | TABLE
    | TBODY
    | TD
    | TEMPLATE
    | TEXTAREA
    | TFOOT
    | TH
    | THEAD
    | TIME
    | TITLE
    | TR
    | TT
    | U
    | UL
    | VAR
    | VIDEO
    | XMP
)

VOID_TAGS = (
    AREA
    | BASE
    | BR
    | COL
    | EMBED
    | HR
    | IMG
    | INPUT
    | LINK
    | META
    | PARAM
    | SOURCE
    | TRACK
    | WBR
)

ANY_TAGS = NORMAL_TAGS | VOID_TAGS

NORMAL_TAG_STRS = _init_tags(NORMAL_TAGS)
VOID_TAG_STRS = _init_tags(VOID_TAGS)
ANY_TAG_STRS = NORMAL_TAG_STRS + VOID_TAG_STRS

USED_TAG_VALUES: tuple[str, ...] = (
    'del',
    'dir',
    'map',
    'object',
    'input',
    'class',
)

SPECIAL_ATTRS = set((
    'data',
    'aria',
    'x',
    'v',
    'hx'
))
