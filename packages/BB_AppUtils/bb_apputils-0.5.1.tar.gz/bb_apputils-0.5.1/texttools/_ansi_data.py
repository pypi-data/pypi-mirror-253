# data methods for Ansi
import re
from ._constants import getLogger

class Fraction(str):
    string = ''
    numerator = ''
    denominator = ''
    value = 0.0

    def __new__(cls, s):
        log = getLogger(__name__)
        if not s:
            return super().__new__( cls, '' )

        s = str(s).strip()

        try:
            assert re.match( '^[0-9]+/[0-9]+$', s )
            _n, _d = s.split('/')
            s = SuperScript(_n)+'/'+SubScript(_d)
        except Exception as E:
            log.error(f"Invalid fraction '{s}'")
            log.exception(E)

        return super().__new__(cls, s)

    def __init__(self, s):
        self.string = str(s).strip()
        _n, _d = ( int(i) for i in self.string.split('/') )
        self.numerator = _n
        self.denominator = _d
        self.value = _n / _d

class SuperScript(str):
    _sups = { 1: '\u00B9', 2: '\u00B2', 3: '\u00B3', 4: '\u2074', 5: '\u2075',
              6: '\u2076', 7: '\u2077', 8: '\u2078', 9: '\u2079', 0: '\u2070' }
    sup = ''
    original = ''

    def __new__(cls, n):
        log = getLogger(__name__)
        if not n:
            return super().__new__( cls, '' )

        try:
            n = int(n)
            sup = ''.join([ cls._sups[int(i)] for i in list(str(n)) ])
        except ValueError:
            log.error(f"Invalid number '{n}'")
            sup = ''
        except Exception as E:
            log.exception(E)
            sup = ''
        return super().__new__(cls, sup)

    def __init__(self, sup):
        sup2int = dict([(v, k) for k, v in self._sups.items() ])
        try:
            self.original = int(''.join([ str( sup2int[i] ) for i in list(sup) ]))
        except:
            self.original = sup
        self.sup = sup

class SubScript(str):
    _subs = { 1: '\u2081', 2: '\u2082', 3: '\u2083', 4: '\u2084', 5: '\u2085',
              6: '\u2086', 7: '\u2087', 8: '\u2088', 9: '\u2089', 0: '\u2080' }
    sub = ''
    original = ''

    def __new__(cls, n):
        log = getLogger(__name__)
        if not n:
            return super().__new__( cls, '' )

        try:
            n = int(n)
            sub = ''.join([ cls._subs[int(i)] for i in list(str(n)) ])
        except ValueError:
            log.error(f"Invalid number '{n}'")
            sub = str(n)
        except Exception as E:
            log.exception(E)
            sub = str(n)
        return super().__new__(cls, sub)

    def __init__(self, sub):
        sub2int = dict([(v, k) for k, v in self._subs.items() ])
        self.sub = sub
        try:
            self.original = int(''.join([ str( sub2int[i] ) for i in list(sub) ]))
        except:
            self.original = sub

@classmethod
def fraction(cls, n):
    """
    Create fraction from a set of integers or a fraction string
    """
    try:
        if isinstance( n, list|tuple ):
            assert len(n) == 2 and \
                all( isinstance( i, int ) or ( isinstance( i, str ) and i.isnumeric() ) for i in n )
            n = '/'.join( str(i) for i in n )
        else:
            assert isinstance( n, str )
            n = '/'.join( re.findall( '[0-9]+', n ))

        # assert re.match( '^[0-9]+/[0-9]+$', n )
        return Fraction(n)

    except AssertionError:
        raise ValueError(f"Invalid value for fraction '{n}'")

@classmethod
def colors16(cls, key = ''):
    """
    Return list of tuples ( name, fg ansi pair, bg ansi pair, rgb )
    """
    _list = [( 'Black'      , ( 0, 30 ), ( 0, 40 ), (0,0,0)       ),
             ( 'Gray'       , ( 1, 30 ), ( 1, 40 ), (104,104,104) ),
             ( 'Dark Gray'  , ( 2, 30 ), ( 2, 40 ), (24,24,24)    ),
             ( 'Red'        , ( 0, 31 ), ( 0, 41 ), (178,24,24)   ),
             ( 'Light Red'  , ( 1, 31 ), ( 1, 41 ), (255,84,84)   ),
             ( 'Dark Red'   , ( 2, 31 ), ( 2, 41 ), (101,0,0)     ),
             ( 'Green'      , ( 0, 32 ), ( 0, 42 ), (24,178,24)   ),
             ( 'Light Green', ( 1, 32 ), ( 1, 42 ), (84,255,84)   ),
             ( 'Dark Green' , ( 2, 32 ), ( 2, 42 ), (0,101,0)     ),
             ( 'Orange'     , ( 0, 33 ), ( 0, 43 ), (178,104,24)  ),
             ( 'Yellow'     , ( 1, 33 ), ( 1, 43 ), (255,255,84)  ),
             ( 'Gold'       , ( 2, 33 ), ( 2, 43 ), (101,94,0)    ),
             ( 'Blue'       , ( 0, 34 ), ( 0, 44 ), (24,24,178)   ),
             ( 'Light Blue' , ( 1, 34 ), ( 1, 44 ), (84,84,255)   ),
             ( 'Dark Blue'  , ( 2, 34 ), ( 2, 44 ), (0,0,101)     ),
             ( 'Purple'     , ( 0, 35 ), ( 0, 45 ), (178,24,178)  ),
             ( 'Pink'       , ( 1, 35 ), ( 1, 45 ), (255,84,255)  ),
             ( 'Dark Purple', ( 2, 35 ), ( 2, 45 ), (101,0,101)   ),
             ( 'Cyan'       , ( 0, 36 ), ( 0, 46 ), (24,178,178)  ),
             ( 'Light Cyan' , ( 1, 36 ), ( 1, 46 ), (84,255,255)  ),
             ( 'Dark Cyan'  , ( 2, 36 ), ( 2, 46 ), (0,101,101)   ),
             ( 'Light Gray' , ( 0, 37 ), ( 0, 47 ), (178,178,178) ),
             ( 'White'      , ( 1, 37 ), ( 1, 47 ), (255,255,255) ),
             ( 'Silver'     , ( 2, 37 ), ( 2, 47 ), (101,101,101) )]


    items = [ dict([( 'name', a ), ( 'fg', b ), ( 'bg', c ), ( 'rgb', d )]) for a, b, c, d in _list ]

    if not key:
        return items

    if key == 'fg':
        return dict([( i['fg'], i ) for i in sorted(items, key = lambda x:x['fg']) ])
    elif key == 'bg':
        return dict([( i['bg'], i ) for i in sorted(items, key = lambda x:x['bg']) ])
    elif key == 'rgb':
        return dict([( i['rgb'], i ) for i in sorted(items, key = lambda x:x['rgb']) ])
    elif key == 'name':
        return dict([( i['name'], i ) for i in sorted(items, key = lambda x:x['name']) ])
    elif key in range(len(items)):
        return items[key]
    else:
        for i in items:
            if i['name'] == key:
                return i

        raise ValueError(f"Invalid keyument for TextTools.colors16() - '{key}'")

@classmethod
def esc2html(cls, t):
    if not ( isinstance( t, list|tuple ) and all( isinstance(i, int) for i in t )):
        raise TypeError("Argument must be a list|tuple of escape integers")

    _d = [( ';'.join([ str(i) for i in k ]) + ';', v ) for k, v in cls._Esc2HtmlDict.items() ]
    s = ';'.join([ str(i) for i in t ]) + ';'
    html = { 'RESET': 0 }
    for i, ( k, v ) in enumerate(_d):
        if not s:
            break
        a, b, c = s.partition(k)
        if not b:
            continue
        if k == '0;':
            html['RESET'] = 1
            continue
        html = { **html, **v }
        s = a+c
        del a, b, c
    return html

@classmethod
def esc2span( cls, t, exit_span = 0 ):
    ES = ''
    html = cls.esc2html(t)
    if exit_span and html['RESET']:
        ES = '</span>'
    html.pop('RESET')
    if not html:
        return ES
    return f'''{ES}<span style="{'; '.join([ ':'.join([k, v]) for k, v in html.items() ])}">'''

@classmethod
def esc2style(cls, esc):
    log = getLogger(__name__)
    D = {}
    s = esc
    reset = False
    while re.search( '[0-9]+', s ):
        m = None
        if re.search( '38;2;[0-9]+;[0-9]+;[0-9+]+', s ):
            m = ( 'color', re.search( '38;2;[0-9]+;[0-9]+;[0-9+]+', s ).group() )
        elif re.search( '48;2;[0-9]+;[0-9]+;[0-9+]+', s ):
            m = ( 'background-color', re.search( '48;2;[0-9]+;[0-9]+;[0-9+]+', s ).group() )

        if m:
            D[m[0]] = f"rgb{tuple([ int(i) for i in re.findall( '[0-9]+', m[1] )][2:])}"

        else:
            m = ( None, re.search( '[0-9]+', s ).group() )
            if m[1] == '0':
                reset = True
            else:
                _m = (int(re.search( '[0-9]+', s ).group()),)
                if _m in cls._Esc2HtmlDict:
                    D = { **D, **cls._Esc2HtmlDict[_m] }
                else:
                    log.error(f"Unknown escape code '{_m[0]}'")

        s = s.replace( m[1], '' )

    return ( reset, D )

@classmethod
def toHtml(cls, string, *, tag = '', end = True, ending_tag = True):
    Ansi = cls.Ansi
    string = Ansi(string)
    span_lvl = 0
    style = {}
    html = ''
    endtag = ''
    if tag:
        if not tag.startswith('<'):
            tag = f"<{tag}"
        if not tag.endswith('>'):
            tag = f"{tag}>"
        endtag = f"</tag[1:].split()[0].replace('>','')>"

    start = 0
    for index, esc in string.escapes:
        html += string.clean[start:index]
        start = index

        r, css = cls.esc2style( esc )
        while r and span_lvl > 0:
            html += '</span>'
            span_lvl -= 1

        if css:
            html += f"<span style=\"{'; '.join(f'{k}: {v}' for k, v in css.items())};\">"
            span_lvl += 1

    html += string.clean[start:len(string)]

    if end or ending_tag:
        while span_lvl > 0:
            html += '</span>'
            span_lvl -= 1

        if ending_tag:
            html += endtag

    return html
