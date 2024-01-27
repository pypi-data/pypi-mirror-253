# TextTools cursor controls
import os, re, sys, termios, tty
from ._constants import RE_CURSOR_CONTROL_ESCAPE
from .ansitools import Ansi

class CursorControl(type):
    def __instancecheck__(self, other):
        try:
            assert re.match( RE_CURSOR_CONTROL_ESCAPE, str(other) )
            return True
        except:
            return False

    def __repr__(self):
        return self.__name__

# data = {}
# for i in list(filter( lambda x: bool( not x.startswith('_') or x == '__sc__' ), dir(CursorControls) )):
#     if i == 'help':
#         continue
#     obj = getattr( cc, i )
#     data[i] = { 'code': obj.__sc__(),
#                 'ansi': obj.ansi,
#                 'doc': obj.__doc__ }

class CursorControls:
    """ Ansi escapes to control terminal screen and cursor """

    def __init__(self, *args):
        for attr in dir(self):
            if not attr.startswith('_') and not attr.startswith('help'):
                cls = getattr( self, attr )
                _var = cls.__sc__()
                setattr( self, _var, cls() )

    class CursorUp:
        """
        Cursor Up
          'n': Number of lines
        """
        ansi = ('A',)

        def __call__(self, n = 1):
            return f'\x1b[{abs(n)}A'
        def __repr__(self):
            return "(< CursorUp: esc = "+repr('\x1b[{n}A')+" >)"
        def __str__(self):
            return '\x1b[1A'
        @classmethod
        def __sc__(cls):
            return 'up'

    class CursorDown:
        """
        Cursor Down
          'n': Number of lines
        """
        ansi = ('B',)

        def __call__(self, n = 1):
            return f'\x1b[{abs(n)}B'
        def __repr__(self):
            return "(< CursorDown: esc = "+repr('\x1b[{n}B')+" >)"
        def __str__(self):
            return '\x1b[1B'
        @classmethod
        def __sc__(cls):
            return 'dn'

    class CursorRight:
        """
        Cursor Right
          'n': Number of columns
        """
        ansi = ('C',)

        def __call__(self, n = 1):
            return f'\x1b[{abs(n)}C'
        def __repr__(self):
            return "(< CursorRight: esc = "+repr('\x1b[{n}C')+" >)"
        def __str__(self):
            return '\x1b[1C'
        @classmethod
        def __sc__(cls):
            return 'R'

    class CursorLeft:
        """
        Cursor Left
          'n': Number of columns
        """
        ansi = ('D',)

        def __call__(self, n = 1):
            return f'\x1b[{abs(n)}D'
        def __repr__(self):
            return "(< CursorLeft: esc = "+repr('\x1b[{n}D')+" >)"
        def __str__(self):
            return '\x1b[1D'
        @classmethod
        def __sc__(cls):
            return 'L'

    class CursorToColumn:
        """
        Cursor To Column
          'n': column number
        """
        ansi = ('G',)

        def __call__(self, n = 0):
            return f'\x1b[{abs(n)}G'
        def __repr__(self):
            return "(< CursorToColumn: esc = "+repr('\x1b[{n}G')+" >)"
        def __str__(self):
            return '\x1b[0G'
        @classmethod
        def __sc__(cls):
            return 'col'

    class HideCursor:
        """ Cursor Invisible """
        ansi = ('?25l',)

        def __call__(self):
            return '\x1b[?25l'
        def __repr__(self):
            return "(< HideCursor: esc = "+repr('\x1b[?25l')+" >)"
        def __str__(self):
            return '\x1b[?25l'
        @classmethod
        def __sc__(cls):
            return 'hide'

    class ShowCursor:
        """ Cursor Visible """
        ansi = ('?25h',)

        def __call__(self):
            return '\x1b[?25h'
        def __repr__(self):
            return "(< ShowCursor: esc = "+repr('\x1b[?25h')+" >)"
        def __str__(self):
            return '\x1b[?25h'
        @classmethod
        def __sc__(cls):
            return 'show'

    class PositionCursor:
        """
        Set cursor position
            - PositionCursor( [line], [column] )
        """
        ansi = ('H')

        def __call__(self, line = 0, column = 0):
            if isinstance( line, list|tuple ) and len(line) == 2:
                line, column = ( abs(int(i)) for i in line )
            else:
                line   = abs(int(line))
                column = abs(int(column))
            return f"\x1b[{line};{column}H"

        def __repr__(self):
            return "(< PositionCursor: esc = "+repr('\x1b[{line};{column}H')+" >)"
        def __str__(self):
            return '\x1b[0;0H'
        @classmethod
        def __sc__(cls):
            return 'pos'

    class GetCursorPosition:
        """
        Get cursor position
            - returns tuple( [line], [column] )
        """
        ansi = ('6n')
        _runs_ = 0

        def __call__(self):
            buf = ""
            stdin = sys.stdin.fileno()
            tattr = termios.tcgetattr(stdin)

            try:
                tty.setcbreak(stdin, termios.TCSANOW)
                sys.stdout.write("\x1b[6n")
                sys.stdout.flush()

                while True:
                    buf += sys.stdin.read(1)
                    if buf[-1] == "R":
                        break

            finally:
                termios.tcsetattr(stdin, termios.TCSANOW, tattr)

            # reading the actual values, but what if a keystroke appears while reading
            # from stdin? As dirty work around, GetCursorPosition will try up to 3 times
            # to get a valid result. If all fails, returns None
            try:
                matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
                groups = matches.groups()
            except AttributeError:
                if self._runs_ >= 3:
                    self._runs_ = 0
                    return None
                return GetCursorPosition()

            self._runs_ = 0
            return (int(groups[0]), int(groups[1]))

        def __repr__(self):
            return f"(< GetCursorPosition: esc = "+repr('\x1b[6n')+" >)"
        def __str__(self):
            return ';'.join([ str(i) for i in self() ])
        @classmethod
        def __sc__(cls):
            return 'getpos'


    class Clear(str):
        """
        Clear screen or line
          - alias = 'Cursor.clr'
          - clear entire screen (2J)

            Clear.line
              - clear current line (2K)
                L: clear line left of cursor (1K)
                R: clear line right of cursor (0K)

            Clear.screen
              - clear entire screen (2J)
                up: clear screen above cursor (1J)
                dn: clear screen below cursor (0J)
        """
        ansi = ('K', 'J')

        def __new__(cls): #, s = '\x1b[2J' ):
            class SubStr(str):
                __doc__ = ''
                def __new__( cls, s, name, doc ):
                    clsDict = { '__s__'   : s,
                                # '__doc__' : cls.__doc__,
                                '__name__': name,
                                '__init__': cls.__init__,
                                '__len__' : cls.__len__,
                                '__str__' : cls.__str__,
                                '__call__': cls.__call__,
                                '__repr__': cls.__repr__    }
                    self = type.__new__( type, name, (str,), clsDict )
                    return str.__new__( self, self.__s__ )

                def __init__(self, s, name, doc):
                    setattr( self, '__doc__', doc )

                def __len__(self): return len(str(self))
                def __call__(self): return self
                def __str__(self): return Ansi( self.__s__ )
                def __repr__(self): return f"(< {self.__name__}: esc = "+repr(self.__s__)+" >)"

            _line = SubStr( '\x1b[2K', 'Clear.line', 'Clear line' )
            _L_all = SubStr( '\x1b[2K', 'Clear.line.all', 'Clear entire line (2K)' )
            _L = SubStr( '\x1b[1K', 'Clear.line.L', 'Clear line left of cursor (1K)' )
            _R = SubStr( '\x1b[0K', 'Clear.line.R', 'Clear line right of cursor (0K)' )
            setattr( _line, 'all', _L_all )
            setattr( _line, 'L', _L )
            setattr( _line, 'R', _R )

            _screen = SubStr( '\x1b[2J', 'Clear.screen', 'Clear screen' )
            _S_all = SubStr( '\x1b[2J', 'Clear.screen.all', 'Clear entire screen (2J)' )
            _up = SubStr( '\x1b[1J', 'Clear.screen.up', 'Clear screen above cursor (1J)' )
            _dn = SubStr( '\x1b[0J', 'Clear.screen.dn', 'Clear screen below cursor (0J)' )
            setattr( _screen, 'all', _S_all )
            setattr( _screen, 'up', _up )
            setattr( _screen, 'dn', _dn )

            clsDict = { '__s__'   : '\x1b[2J',
                        '__call__': cls.__call__,
                        '__init__': cls.__init__,
                        '__len__' : cls.__len__,
                        # '__doc__' : cls.__doc__,
                        '__str__' : cls.__str__,
                        'line'    : _line,
                        'screen'  : _screen,
                        'section' : cls.section }

            self = type.__new__( type, 'Clear', (str,), clsDict )
            S = str.__new__( self, self.__s__ )
            setattr( S, '__doc__', cls.__doc__ )
            return S

        def __call__(self): return self
        def __len__(self): return len(str(self))
        def __str__(self): return Ansi( self.__s__ )
        def __repr__(self): return f"(< Clear: esc = "+repr(self.__s__)+" >)"

        def section(self, a, b):
            """
            Clear from position 'a' to position 'b'
                section( (1,6), (1,23) )

              * pos 'a' must be before pos 'b'
            """
            if not ( a[0] < b[0] or ( a[0] == b[0] and a[1] < b[1] )):
                raise ValueError("Invalid order of line/col positions - 'b' must come after 'a'")

            pos = Cursor.getpos()
            width = os.get_terminal_size().columns
            sys.stdout.write(f"{Cursor.pos(a[0],a[1])}")
            for line in range(a[0], b[0]+1):
                if line == a[0]:
                    start = a[1]
                else:
                    start = 0

                if line < b[0]:
                    end = 99999999
                else:
                    end = b[1]

                for col in range( start, end ):
                    if col >= width-2:
                        if line < b[0]:
                            sys.stdout.write('\n')
                        break
                    elif line == b[0] and col >= b[1]:
                        break
                    sys.stdout.write(' ')

            sys.stdout.write( Cursor.pos( *pos ))
            sys.stdout.flush()

        @classmethod
        def __sc__(cls):
            return 'clr'


    @classmethod
    def help(cls, *, get_list = False):
        # _cls = cls.__init__(cls)
        R = [ '  \x1b[1;38;2;240;240;240;4mCursor Controls:\x1b[0m', '',
              '    \x1b[38;2;0;255;255;3m'+cls.__doc__.strip(), '\x1b[0m' ]
        for attr in dir(cls):
            if attr.startswith('_') or len(attr) < 5:
                continue
            c = getattr( cls, attr )
            _d = c.__doc__.strip().split('\n')
            R += [ f"\x1b[38;2;51;153;255m    CursorControls.{c.__name__}():\x1b[38;2;0;255;255;3m",
                   f"        {_d[0]}", *_d[1:], '\x1b[0m' ]

        if get_list:
            return R
        else:
            print( '\n'.join(R) )

Cursor = CursorControls()
