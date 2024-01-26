# ANSI escapes for text manipulation
#
# Import and use these to make your python scripts perdy.
# All escape codes are returned in octal format.
# A few cursor controls are included but you can find
# many more with a few duckduckgo searches.

import re, os, json
from importlib.resources import files as _src
from ._constants import RE_RGB_ESCAPE, RE_16COLOR_ESCAPE, COLORS_RGB_DIFF_KEY, getLogger

from apputils.tools import tupleCalc
from . import _data

class TextTools:
    """
    Tools for getting and printing colorized/styled text
    """
    from .cursorcontrols import CursorControls
    from .ansitools import Ansi, AnsiList
    from ._ansi_data import ( colors16,
                              fraction,
                              esc2html,
                              esc2style,
                              # esc2span,
                              toHtml,
                              SubScript as Sub,
                              SuperScript as Sup )
    from .escapes import AnsiEscape

    from .escapes import Escapes as E
    _E = E()
    StyleDict   = _E.StyleDict
    ColorDict   = _E.ColorDict
    ColorDict16 = _E.ColorDict16
    Cursor      = CursorControls()
    Styles      = _E.Styles
    FG_Colors   = _E.FG_Colors
    BG_Colors   = _E.BG_Colors
    del E, _E, CursorControls

    D = {}
    # for k, v in ColorDict.items():
    #     D[(48,2)+v['rgb']] = { 'background-color': f"rgb{str(v['rgb'])}" }
    #     D[(38,2)+v['rgb']] = { 'color': f"rgb{str(v['rgb'])}" }

    for k, v in ColorDict16.items():
        v['ansi'] = tuple( v['ansi'] )
        v['rgb'] = tuple( v['rgb'] )
        D[v['ansi']] = v['html']

    for k, v in StyleDict.items():
        if k == '_Reset_':
            D[(0,)] = {}
        D[v['ansi']] = v['html']

    _Esc2HtmlDict = dict(sorted( D.items(), key = lambda x: ( -len( x[0] ), x[0][0] )))
    del D

    @classmethod
    def ansi2rgb(cls, ansi, *, fg_color = True, bg_color = True):
        """
        ansi2rgb( ansi, *, fg_color = True, bg_color = True ) >>> tuple()

            Returns a 5 or 10 part tuple from a string containing ansi escapes
              *args
                'ansi': string containing ansi escape patterns

              **kwargs
                'fg_color': include foreground tuple in results
                             - default = True
                'bg_color': include background color in results
                             - default = True

                Foreground color is always at the beginning of the tuple if both
              'fg_color' and 'bg_color' are True and both values are found
        """
        log = getLogger(__name__)
        try:
            esc = []
            ansi = cls.Ansi( ansi )
            escapes = [[ int(c) for c in re.findall( '[0-9]+', e ) ] for i, e in ansi.escapes ]
            while escapes:
                e = escapes.pop(-1)
                esc.append({ 'fg': (), 'bg': () })
                while True:
                    rgb = ()
                    if len(e) >= 5 and any( i in e for i in (38,48) ):
                        try:
                            fgbg = e.index(38)
                        except:
                            fgbg = e.index(48)
                        if fgbg < len(e) - 4:
                            two = e[fgbg+1]
                            if two == 2 and len(e) >= fgbg + 4:
                                for r in range(5):
                                    rgb = rgb + (e.pop(fgbg),)
                    if not rgb:
                        for i, E in zip( reversed( range(len(e))), reversed(e) ):
                            for _e in range(30,38):
                                if E == _e:
                                    if 1 in e:
                                        rgb = cls.from16( (1,E) )
                                    elif 2 in e:
                                        rgb = cls.from16( (2,E) )
                                    else:
                                        rgb = cls.from16( (0,E) )
                    if not rgb:
                        break
                    elif rgb[0] == 38:
                        esc[-1]['fg'] = rgb
                    else:
                        esc[-1]['bg'] = rgb

                    del rgb, fgbg, two
                    if not e:
                        break

            fg, bg = (), ()
            while esc:
                e = esc.pop(-1)
                if not fg and e['fg']:
                    fg = e['fg']
                if not bg and e['bg']:
                    bg = e['bg']

                if fg and bg:
                    break

            return ( fg[2:], bg[2:] )

        except Exception as E:
            log.exception(E)
            raise

    @classmethod
    def blockTxt( cls, txt, *,
                  fill_indent = False,
                  fill_width = False,
                  indent = 0,
                  indent_first = 0,
                  keep_newlines = False,
                  line_break = ' ',
                  push = 0,
                  push_first = False,
                  split_escapes = True,
                  start_column = 0,
                  width = 0,
                  width_includes_indent = True ):
        """
        Indents text for neater printing
          *args:
            'indent'   : amount of indenting to use after 1st line
                          - 'txt' is split by newlines and 'line_break' value
                          - if 'keep_newlines' == True, only 'line_break' value is
                            used to split 'txt'
                          - default = 0
            'push'     : push all indent values (does not include width)
                         to the right [n] amount of columns
                          - default = 0
            'txt'      : full text string
            'width'    : total width of text block
                          - if negative, subtract from the width found
                            using os.get_terminal_size
                          - does not include indent if width_includes_indent == False

          **kwargs:
            'indent_first'         : Amount of columns to indent to first line
                                      - 'indent' to matches the indent value
                                      - a negative value subtracts from indent value
                                        ( minumum value will be 0 )
                                      - default = 0
            'width_includes_indent': If True (default), includes indent in total width,
                                     otherwise total width = width + indent
            'start_column'         : Column that first line starts on
                                      - use 'indent' to match the indent value
                                      - default = 0
            'split_escapes'        : Resets text at end of lines and uses escapes from
                                     the previous line to reset it.
                                      - default = True
            'keep_newlines'        : Doesn't remove newlines from provided text
                                      - might have double newlines in result
            'line_break'           : Provide a string pattern to try to break lines on
                                      - default = ' '
            'push_first'           : Include the first line when using 'push' argument
                                      - default = False
           ** use fill options to make sure background colors, if used, will cover before
                and/or after the text characters

            'fill_width'           : Fill the remaining width in each line with a space
                                      - default = False
            'fill_indent'          : Insert escape code before the indent spaces when using
                                     'split_escapes'
                                      - default = False
        """
        log = getLogger(__name__)
        Ansi = cls.Ansi
        AnsiList = cls.AnsiList
        line_break = Ansi( line_break )
        indent = int(indent)

        if not txt:
            return Ansi()

        if start_column == 'indent':
            start_column = indent
        else:
            start_column = int(start_column)
            if start_column < 0:
                start_column = indent - start_column if -start_column >= indent else 0

        if indent_first == 'indent':
            indent_first = indent
        else:
            indent_first = int(indent_first)
            if indent_first < 0:
                indent_first = indent + indent_first if -indent_first >= indent else 0

        _p = push
        while _p > 0:
            if push_first:
                indent_first += 1
            indent += 1
            _p -= 1

        total_columns = os.get_terminal_size().columns - 1
        if width == 0:
            width = total_columns
        elif width < 0:
            width = total_columns + width
        else:
            width = int(width)

        if width_includes_indent:
            if width <= indent:
                log.error("Width must be greater than indent when including indent in total width - adding indent to width")
                width += indent
        else:
            width += indent

        if width > total_columns:
            log.warning(f"Width '{width}' is wider than total columns '{total_columns}'. Output might be ugly!")

        def _stripSpace(_s):
            while _s.startswith(' '):
                _s = _s[1:]
            while _s.endswith(' '):
                _s = _s[:-1]
            return _s

        if line_break == ' ':
            _strp = _stripSpace
        else:
            _strp = lambda x: x

        if keep_newlines:
            def _filter(_s):
                return bool(_s)
            T = AnsiList( filter( _filter, [ _strp(i) for i in txt.split( line_break ) ]))
        else:
            T = AnsiList([ _strp(i) for i in txt.replace('\n',' ').split( line_break ) ])

        block = AnsiList( f"{'':<{indent_first}}", strsep = '' )

        while T:
            try:
                line_len = len( block.join().split('\n')[-1] )
            except:
                line_len = 0

            if len( block.join().split('\n') ) == 1:
                line_len += start_column
            next_word = Ansi( T.pop(0) )

            if next_word == '\n':
                block.append( f"\n{'':<{indent}}" )
                continue

            elif next_word.find('\n') >= 0:
                next_word, newline, _n = next_word.partition('\n')
                if _n.string:
                    T.insert( 0, _n )
                T.insert( 0, '\n' )
                if not next_word.string:
                    continue

            if line_len + len(next_word) + len(line_break.strip()) > width:
                if line_len < ( width - indent )*0.67 or len(next_word) + len(line_break.strip()) > width - indent:
                    hyphen = next_word.find('-')
                    if hyphen >= 0 and hyphen + line_len + 1 < width:
                        _a, _b = next_word.split('-', 1)
                        block.append( f"{_a}-\n{'':<{indent}}" )
                    else:
                        split_index = width - line_len - 2
                        _a = next_word[:split_index]
                        _b = next_word[split_index:]
                        block.append( f"{_a}-\n{'':<{indent}}" )
                    T.insert( 0, _b )
                else:
                    block.append( f"\n{'':<{indent}}" )
                    T.insert( 0, next_word )

            else:
                block.append( f"{next_word}{line_break}" )

        _blocks = AnsiList( _stripSpace( block.join('') ).split('\n'), strsep = '\n' )
        if fill_width or fill_indent or split_escapes:
            new = AnsiList( strsep = '\n' )
            last_esc = ''
            for index, line in enumerate( _blocks ):
                if split_escapes:
                    while any( line.string.endswith(i) for i in ( '\x1b[0m', ' ' )):
                        if line[-1] == ' ':
                            line = line[:-1]
                        else:
                            line = line[:-1] + line[-1].clean

                    ei = None
                    if line.escapes:
                        ei = min([ i[0] for i in line.escapes ])

                    if fill_indent:
                        if index == 0 and ei != None and re.match( f'^ {{{start_column},}}\x1b\[.*', line ):
                            line = line[:start_column] + dict(line.escapes)[ei] + line[start_column:ei] + line[ei].clean + line[ei+1:]
                            ei = max([ i[0] for i in line.escapes ])

                        elif index > 0 and last_esc:
                            line = line[:start_column] + last_esc + line[start_column:]
                            ei = max([ i[0] for i in line.escapes ])

                    elif last_esc:
                        line = line[:indent] + last_esc + line[indent:]
                        ei = max([ i[0] for i in line.escapes ])

                    if ei != None:
                        last_esc = dict(line.escapes)[ei]

                line = Ansi(line)
                if fill_width:
                    while len( line ) < width:
                        line = line + ' '

                if split_escapes and line.escapes:
                    line = line + cls.Styles._

                new.append(line)
            _blocks = new

        return str( _blocks )

    @classmethod
    def hex2rgb(cls, HEX):
        """
        Returns an RGB tuple from a hexidecimal code
            'HEX': hexidecimal value representing a color
        """
        h = HEX.replace('#','')[:6]
        return tuple( s for s in tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

    @classmethod
    def rgb2ansi(cls, R = 0, G = 0, B = 0, *, bg = False):
        """
        Returns an ansi escape string from RGB values
            'R': integer for Red    [0-255]
            'G': integer for Green  [0-255]
            'B': integer for Blue   [0-255]

          * default values are set to Black - (0,0,0)
        """
        log = getLogger(__name__)
        try:
            RGB = ( int(R), int(G), int(B) )
            if not all( i in range(256) for i in RGB ):
                raise ValueError

            pre = "48;2" if bg else "38;2"
            return cls.Ansi(f"\x1b[{pre};" + ';'.join([ str(i) for i in RGB ]) + 'm')

        except ValueError as E:
            log.exception(f"R, G, B values must be integers between 0-255, not {R = }, {G = }, {B = }")
            raise
        except Exception as E:
            log.exception(E)
            raise

    @classmethod
    def rgb2hex(cls, RGB):
        """
        Returns a hexidecimal code from an rgb code
            'RGB': tuple|list of 3 integers
        """
        if isinstance( RGB, str ):
            rgb = RGB.replace('rgb','').replace('(','').replace(')','')
            if rgb.find(',') >= 0:
                rgb = tuple([ int(i.strip()) for i in rgb.split(',') ])
            else:
                rgb = tuple([ int(i.strip()) for i in rgb.split() ])
        elif isinstance( RGB, tuple ) or isinstance( RGB, list ):
            rgb = RGB

        assert len(rgb) == 3
        return '#%02x%02x%02x'%rgb

    @classmethod
    def rgbString(cls, value):
        """
        Create an rgb string
            'value': hex, string of integers, list|tuple, or FG_Color|BG_Color
        """
        from .types import FG_Color, BG_Color
        if isinstance( value, str ):
            if re.match( '^#?[A-Fa-f0-9]{6}$', value ):
                value = cls.hex2rgb(value)
            else:
                value = [ int(i) for i in re.findall( '[0-9]+', value )]

        elif isinstance( value, FG_Color|BG_Color ):
            value = value.rgb

        if not ( isinstance( value, list|tuple ) and all( isinstance( i, int ) and i >= 0 and i <= 255 for i in value )):
            raise ValueError(f"Invalid rgb value - '{value}'")

        return f"rgb{tuple(i for i in value)}"

    @classmethod
    def money_fmt(cls, n, *, color_type = 'term'):
        """
        Return formatted number to money string
            accepted color_type:
                'term', 'term_reverse', 'html', or 'html_reverse'
        """
        if not n:
            return

        n = str(n)
        assert re.match( '^[$,\.0-9]+$', n )
        _n = float(''.join( re.findall( '[0-9\.]', n )))

        if _n == 0:
            col = 'green'
        elif n.startswith('-'):
            _n = -_n
            if color_type.endswith('_reverse'):
                col = 'green'
            else:
                col = 'red'
        else:
            if color_type.endswith('_reverse'):
                col = 'red'
            else:
                col = 'green'

        color_type = color_type.split('_')[0]
        if color_type:
            C = getColor( col, color_type )
            return f"{C['start']}${_n:,.02f}{C['end']}"
        else:
            return f"${_n:,.02f}"

    @classmethod
    def t2a(cls, t: tuple|list, *, end = 'm'):
        """
        Tuple to ansi escape
            - provide a tuple or list of ansi escape integers
            - returns an ansi escape string
        """
        return '\x1b[' + ';'.join( str(i) for i in t ) + end

    @classmethod
    def from16(cls, color, *, return_data = False):
        """
        16 color tuple to rgb tuple
            - if len(tup) == 1, assumes 0 for first value
        """
        fg_rng = list(range(30,38))
        bg_rng = list(range(40,48))
        try:
            if isinstance( color, str ):
                color = tuple( int(i) for i in re.findall( '[0-9]+', color ))
            if isinstance( color, int ):
                color = ( 0, color )
            elif isinstance( color, list|tuple ):
                if len(color) == 1:
                    color = ( 0, color[0] )
            else:
                raise AssertionError

            assert len(color) == 2 and color[0] in (0,1,2) and color[1] in fg_rng + bg_rng
            rgb = { **cls.colors16('fg'), **cls.colors16('bg') }[color]['rgb']

            if color[1] in fg_rng:
                return tuple([ 38, 2, *rgb ])
            else:
                return tuple([ 48, 2, *rgb ])

        except AssertionError:
            raise ValueError(f"Invalid 16 color tuple '{color}'")

    @classmethod
    def to16color(cls, rgb, *, bg = False, color_dict = False, diff_key = COLORS_RGB_DIFF_KEY, all_results = False ):
        """
        Rgb to 16 color tuple
            - rgb length can be 3 or 5
            - if rgb doesn't match color, tries to find the closest match
            - if len(rgb) != 5, a fg color is returned by default

            'bg'         : True to force or set to return a bg color
            'data'       : True to return a dict
            'diff_key'   : key to sort matches by
                            [ 'mean'||'median'||'max'||'min'||'min_max_avg' ]
            'all_results': return a list of all result data
                            - assumes 'data' == True
        """
        log = getLogger(__name__)
        if bg:
            mode = 'bg'
        else:
            mode = 'fg'

        c16_rng = list(range(30,38)) + list(range(40,48))
        try:
            _D_rgb = cls.colors16('rgb')
            if isinstance( rgb, str ):
                rgb = tuple( int(i) for i in re.findall( '[0-9]+', rgb ))
            else:
                rgb = tuple(rgb)

            if len(rgb) == 1 and rgb[0] in c16_rng:
                return ( 0, rgb[0] )

            elif len(rgb) == 2 and rgb[1] in c16_rng:
                assert rgb[0] in (1,2,3)
                return rgb

            elif len(rgb) == 3:
                assert all( i >= 0 and i <= 255 for i in rgb )

            elif len(rgb) == 5:
                if rgb[0] == 38:
                    if not bg:
                        mode = 'fg'
                elif rgb[0] == 48:
                    mode = 'bg'
                else:
                    raise AssertionError
                assert rgb[1] == 2

                rgb = tuple( rgb[2:] )

            else:
                raise AssertionError

            if rgb in _D_rgb:
                return _D_rgb[rgb]

            _r = [{ **_D_rgb[i], **tupleCalc( rgb, i, '-', diff = True )} for i in list( _D_rgb )]
            _r_sorted = sorted( _r, key = lambda x:x[ diff_key ] )

            if all_results:
                return _r
            elif color_dict:
                return _D_rgb[ _r_sorted[0] ]
            else:
                return _D_rgb[ _r[0] ][mode]

        except SyntaxError:
            raise ValueError(f"Invalid rgb tuple '{rgb}'")

        except Exception as E:
            log.exception(E)
            raise E

    @classmethod
    def help(cls, *, return_list = False):
        """
        TextTools help message
            - prints detailed list of available colors

          'return_list': return as a list instead of printing
                          - default = False
        """
        docs = {}
        for attr in dir(cls):
            if attr.startswith('_') or len(attr) < 5:
                continue
            try:
                d = getattr( cls, attr ).__doc__
                if not d:
                    continue
                docs[attr] = d
            except:
                continue

        R = [ '  \x1b[1;38;2;240;240;240;4mTextTools:\x1b[0m', '',
              '    \x1b[38;2;0;255;255;3m'+cls.__doc__.strip(), '\x1b[0m' ]

        for attr, doc in docs.items():
            _d = doc.strip().split('\n')

            R += [ f"\x1b[38;2;51;153;255m    {'TextTools.'+attr+'():':<25}\x1b[38;2;0;255;255;3m",
                   f"        {_d[0]}", *_d[1:], '\x1b[0m' ]

            if attr in ( 'Colors', 'Controls', 'Styles' ):
                R += [ f"        {i}" for i in getattr( cls, attr )().help( get_list = True )]

        if get_list:
            return R
        else:
            print( '\n'.join(R) )
