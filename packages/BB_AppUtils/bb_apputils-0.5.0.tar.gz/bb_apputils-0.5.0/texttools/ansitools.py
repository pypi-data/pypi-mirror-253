import os, sys, json, re
from string import Formatter
from io import StringIO
from typing import Generator
from functools import wraps

from ._constants import ( ANSI_ITERABLES,
                          RE_RGB_ESCAPE,
                          RE_16COLOR_ESCAPE,
                          RE_STYLE_ESCAPE,
                          HTML_SINGLE_CHAR_CODES,
                          getLogger )

class Ansi(str):
    """
        Holds a string object with escapes while still reporting an accurate
      length. also provides a cleaned version (no escapes).

        Using f-strings will 're-class' the object to a standard str() object.
      It is recommended to use the '+' operator to join standard string objects
      with Ansi objects so that they remain Ansi types.
    """
    _html_             = ''
    _kwargs            = {}
    _last_esc_on_slice = False
    _reset_on_slice    = False
    clean              = ''
    escapes            = []
    string             = ''
    strsep             = ' '

    def __new__(cls, *args, **kwargs):          # Create new object
        if len(args) > 1:
            return AnsiList( *[ str(i) for i in args ], **kwargs )
        elif len(args) == 1 and isinstance( args[0], ANSI_ITERABLES ):
            return AnsiList( *[ str(i) for i in args[0] ], **kwargs )
        elif len(args) == 1:
            return super().__new__( cls, str(args[0]) )
        elif not args:
            return super().__new__( cls, '' )
        else:
            raise TypeError(f"Invalid type '{type(args[0])}' for Ansi string")

    def __wrapper__(func):
        @wraps(func)
        def __inner(self, *args, **kwargs):
            name = func.__name__
            return getattr( self.clean, name )(*args, **kwargs)
        return __inner

    def __init__(self, string = '', **kwargs):
        """
        Create an Ansi string
        ========================================================================
        **kwargs:
            'last_esc_on_slices': add last ansi escape to end of string if
                                    slice leaves it out
                                    - DEFAULT = False
            'reset_on_slice'    : add ansi text reset to end of slices
                                    - overrides 'last_esc_on_slices' if True
                                    - DEFAULT = False
            'strsep'            : passed to AnsiList if split is used

            * Also will look for environment variables 'LAST_ESC_ON_SLICES' and
                'RESET_ON_SLICES' in os.environ. Boolean values are expected.
                Anything other than 'false', '0', or 'no' will set these values
                to True.
        """
        for opt in ( 'reset_on_slice', 'last_esc_on_slice' ):
            _setopt = 'false'
            if opt in kwargs:
                setopt = kwargs[opt]
                _setopt = str( setopt ).lower()
            elif opt.upper() in os.environ:
                setopt = os.environ[opt.upper()]
                _setopt = setopt.lower()

            if _setopt in ( 'true', '1', 'yes' ):
                setattr( self, f"_{opt}", True )
            elif _setopt in ( 'false', '0', 'no' ):
                setattr( self, f"_{opt}", False )
            else:
                raise ValueError(f"Invalid bool value for kwarg '{opt}' - '{setopt}' - True|1|yes or False|0|no")

        self._kwargs = kwargs

        if 'strsep' in kwargs:
            self.strsep = kwargs['strsep']
        else:
            self.strsep = ' '

        if isinstance( string, Ansi ):
            for attr in set(string.__dict__) & set([ '_html_','_kwargs','_last_esc_on_slice','_reset_on_slice','clean','escapes','string' ]):
                setattr( self, attr, getattr( string, attr ))
        else:
            self.string = str(string)
            self.clean, self.escapes = self.rmEsc( self.string )

        for attr in ( 'count', 'endswith', 'find', 'isalnum', 'isalpha',
                      'isascii', 'isdecimal', 'isdigit', 'isidentifier',
                      'islower', 'isnumeric', 'isspace', 'istitle', 'isupper' ):
            setattr( self, attr, getattr( self.clean, attr ))

    def __iter__(self):
        L = list(self.clean)
        E = dict(self.escapes)
        if E:
            rng = max(E)+1 if max(E)+1 > len(L) else len(L)
        else:
            rng = len(L)

        items = []
        for i in range(rng):
            if i in E:
                items.append( E[i] )
            try:
                items.append( L[i] )
            except:
                pass

        for i in items:
            yield i

    def __contains__(self, item):
        return item in list(self)

    # def __next__(self):
    #     try:
    #         try:
    #             item = L[self._index_]
    #
    #         except TypeError:
    #             print("TypeError")
    #             self._index_ = self._index_[0]
    #             try:
    #                 item = E[self._index_]
    #
    #             except KeyError:
    #                 print("KeyError")
    #                 item = L[self._index_]
    #                 self._index_ = [ self._index_ + 1 ]
    #
    #         except IndexError:
    #             print("IndexError")
    #             item = E[self._index_]
    #             self._index_ += 1
    #
    #         return item
    #
    #     except ( IndexError, KeyError ):
    #         print("IndexError|KeyError")
    #         self._index_ = [0]
    #         raise StopIteration

    def __add__(self, other): return type(self)( f"{self}{str(other)}" )
    def __radd__(self, other): return type(self)( f"{str(other)}{self}" )
    def __bool__(self): return bool(self.clean)
    def __len__(self): return len(self.clean)

    def __format__(self, format_spec = ''):
        alignment_flag = ''
        if not format_spec:
            return str.__format__( self.string, format_spec )
        elif not self.escapes:
            return str.__format__( self.string, format_spec )

        try:
            alignment_flag = list(set(list(format_spec)) & set(['<', '>', '^']))[-1]
            filler, _, value = format_spec.rpartition( alignment_flag )
            n = int( value )
        except Exception as E:
            return str.__format__( self.string, format_spec )
        else:
            old_num = str(n)
            new_num = str( n + sum([ len(i[1]) for i in self.escapes ]))
            new_fs = format_spec.replace( old_num, new_num )
            return str.__format__( self.string, new_fs )

    def __getitem__(self, key):
        log = getLogger(__name__)
        if isinstance( key, slice ):
            if not key.start:
                start = 0
            elif isinstance( key.start, str ):
                flag = key.start
                index = key.stop
                if not index:
                    raise ValueError("An index must be provided for the second part of the slice when using flags")
                elif not isinstance( index, int ):
                    raise TypeError(f"Index must be an integer, not '{type(index).__name__}'")

                if flag == 'a':
                    L = list(self)
                elif flag == 'e':
                    L = [ i[1] for i in sorted( self.escapes )]
                else:
                    raise ValueError(f"Acceptable flags are 'a' and 'e', not '{flag}'")

                if index < 0:
                    index = len(L) + index
                if index < 0 or index >= len(L):
                    raise IndexError(f"Index '{index}' out of range")
                return L[index]

            else:
                start = key.start if key.start > 0 else len(self.clean)+key.start

            if not key.stop:
                stop = 9223372036854775807
            else:
                stop = key.stop if key.stop > 0 else len(self.clean)+key.stop

            log.debug(f"{start=}, {stop=}")

            if start >= stop:
                return Ansi(**self._kwargs)

        elif isinstance( key, int ):
            start = key if key >= 0 else len(self) + key
            stop = start + 1
            if stop == len(self) and len(self) in dict(self.escapes):
                stop += 1

        else:
            raise TypeError(f"Invalid type for key/index - '{type(key).__name__}'")

        def _filterEsc(e):
            if e[0] in range(start, stop):
                return True
            return False

        log.debug(f"{start=}, {stop=}")
        slist = list(self.clean[start:stop])
        log.debug(f"{slist=}")
        escapes = sorted(filter( _filterEsc, self.escapes ), reverse = True )
        log.debug(f"{escapes=}")
        for esc in escapes:
            slist.insert( esc[0] - start, esc[1] )

        if self._reset_on_slice:
            if escapes[-1] != str(self.reset()):
                slist.append( self.reset() )
        elif self._last_esc_on_slice and escapes[-1] != self.escapes[-1][1]:
            slist.append( self.escapes[-1][1] )

        return type(self)(''.join(slist))

    def __repr__(self):
        return super().__repr__()

    def __setattr__(self, name, value):
        if name == 'strsep':
            if value:
                if not isinstance( value, Ansi|str ):
                    raise TypeError("Ansi.strsep must be a str or Ansi object")
                value = str(value)
                self._kwargs['strsep'] = value
                return super().__setattr__( name, value )
        return super().__setattr__( name, value )

    def __str__(self):
        return self.string

    def afind(self, item):
        """ Find index of item in combined list of characters and escapes """
        return list(self).index(item)

    def ansi_lists(self):
        return [ tuple( re.findall( '[0-9]+', e ) ) for i, e in self.escapes ]

    def endswith(self, item):
        return self.string.endswith(item)

    def efind(self, item):
        """ Find index of escape item """
        return [ i[1] for i in sorted( self.escapes )].index(item)

    def find(self, item):
        """ Find index of text character(s) """
        return self.clean.find(item)

    def iterclean(self):
        for i in list(self.clean):
            yield i

    def partition(self, sep):
        if sep not in self:
            return ( Ansi( self.string ), Ansi(), Ansi() )
        return tuple( Ansi(i) for i in self.string.partition(sep) )

    def elen(self):
        return len(self.escapes)

    def alen(self):
        return len(list(self))

    def rlen(self):
        return len(self.string)

    def _get_strsep(self):
        try:
            sep = self.strsep
            assert sep and isinstance( sep, Ansi|str )
            return sep
        except:
            self.strsep = ' '
            return ' '

    def rsplit(self, sep = '', maxsplit = -1):
        if maxsplit == 0:
            return AnsiList([ self ])

        if not sep:
            sep = self._get_strsep()

        splits = []
        slices = []
        _r = ''.join( reversed(self.clean) )
        sep = ''.join( reversed(str(sep)) )

        n = 0
        while True:
            find = _r.find(sep, n)
            if find >= 0:
                slices.append( slice( len(self) - find, len(self) - n ))
                n = find + len(sep)
            elif n >= len(self):
                slices.append( slice( 0, 0 ))
                break
            else:
                slices.append( slice( 0, len(self) - n ))
                break

            if len(slices) == maxsplit:
                if n >= len(self):
                    end = 0
                else:
                    end = len(self) - n

                slices.append( slice( 0, end ))
                break

        slices = sorted(slices)

        for s in slices:
            splits.append( self[s] )

        return AnsiList( *splits )

    def split(self, sep = '', maxsplit = -1):
        """
        Returns an AnsiList
          'sep'     : character to split string by
          'maxsplit': max amount of splitting to perform, starting with
                      the left-most 'sep' match
                       - ignored if less than 0
                       - default = -1
        """
        if not sep:
            sep = self._get_strsep()

        spl = self.clean.split( sep, maxsplit )
        n = 0
        new = []
        esc = dict(self.escapes)
        for s in spl:
            _s = list(s)
            _n = len(s)
            for i in range(_n):
                if n in esc:
                    _s.insert(i, esc[n])
                n += 1
            if n in esc:
                _s.append(esc[n])
            n += 1
            new.append( Ansi( ''.join(_s) ))
            del _s, _n

        if n in esc:
            new[-1] = new[-1] + esc[n]

        return AnsiList(new, strsep = sep)

    def startswith(self, item):
        return self.string.startswith(item)

    def strip(self, chars = None):
        log = getLogger(__name__)
        C = [ i for i in self ]
        def _filter(c):
            if (( isinstance( chars, str ) and c == chars ) or \
                (( isinstance( chars, list ) or isinstance( chars, tuple )) and c in chars )):
                    return False
            return True

        if not chars:
            string = type(self)( self.string, **self._kwargs )
            log.debug(f"Removing beginning/ending whitespace/newlines")
            log.debug(f"{string.escapes=}")
            while C and C[-1] in (' ', '\n'):
                C.pop(-1)
            while C and C[0] in (' ', '\n'):
                C.pop(0)
        else:
            log.debug(f"Stripping line of character(s) '{repr(chars)}'")
            C = filter( _filter, C )

        return Ansi().join(C)

    def join(self, _list, **kwargs):
        if not isinstance( _list, ANSI_ITERABLES ):
            raise TypeError(f"Can not join {type(_list)} - only 'list', 'tuple', or 'AnsiList'")
        return Ansi( self.string.join([ str(i) for i in _list ]), **kwargs )

    @classmethod
    def reset(cls):
        return Ansi( '\x1b[0m', **cls._kwargs )

    def html(self):
        if self._html_:
            return self._html_
        from .texttools import TextTools
        self._html_ = TextTools.toHtml( self )
        return self._html_

    @classmethod
    def rmEsc(cls, string):
        """
        Remove ansi escapes from string
            - returns a tuple ( cleaned string, tuple(( index. esc), ( index, esc ), ...etc ))
        """
        escapes = re.findall( r'\x1bM|\x1bH|\x1b\[[(\?)?;0-9]+[hlmnsuJKABCDEFG]{1}', string )
        indexed = []
        for e in escapes:
            indexed.append(( string.index(e), e ))
            string = string.replace( e, '', 1 )

        return ( string, tuple(indexed) )

class AnsiList(list):
    _kwargs = {}
    strsep = ''

    def __init__(self, *args, strsep = '', **kwargs):
        self.strsep = Ansi( strsep )
        kwargs['strsep'] = self.strsep
        self._kwargs = kwargs

        if len(args) == 1:
            if isinstance( args[0], ANSI_ITERABLES ):
                args = args[0]
            elif isinstance( args[0], Ansi|str ):
                args = [ args[0] ]
            else:
                raise TypeError(f"Invalid type '{repr(type(args[0]))}' for AnsiList")

        super().__init__( Ansi( arg, **self._kwargs ) for arg in args )

    def __chk_index__(func):
        @wraps(func)
        def __inner(self, index):
            if index >= len(self) or ( index < 0 and len(self) - index < 0 ):
                raise IndexError("Index out of range")
            return func(self, index)
        return __inner

    def __concat(func):
        @wraps(func)
        def __wrap(self, other):
            if isinstance( other, ANSI_ITERABLES ):
                other = AnsiList( other, **self._kwargs )
            else:
                other = AnsiList([ other ], **self._kwargs )

            return func(self, other)
        return __wrap

    @__concat
    def __add__(self, other):
        return AnsiList( *self.copy(),
                         *other,
                         **self._kwargs )

    @__concat
    def __iadd__(self, other):
        return self.__add__(other)

    @__concat
    def __radd__(self, other):
        return AnsiList( *other,
                         *self.copy(),
                         **self._kwargs )

    def __setitem__(self, index, item):
        super().__setitem__( index, Ansi( item, **self._kwargs ))

    def __str__(self):
        return self.strsep.join([ i for i in self ])

    def append(self, item):
        super().append( Ansi( item, **self._kwargs ))

    def clean(self):
        return AnsiList([ i.clean for i in self ], **self._kwargs )

    def copy(self):
        return AnsiList( *[ i.string for i in self ], **self._kwargs )

    def index(self, arg, start=0, stop=9223372036854775807):
        if stop < 0:
            rng = range( start, len(self)+stop )
        else:
            rng = range( start, stop )

        for index, item in zip( rng, self[start:stop] ):
            if arg == item or str(arg) in ( item.clean, item.string ):
                return index
        raise ValueError(f"List doesn't contain value '{arg}'")

    def insert(self, index, item):
        super().insert( index, Ansi( str(item), **self._kwargs ))

    def iterclean(self):
        """
        A generator of this list with all ansi escapes removed
        """
        for i in range(len(self)):
            yield self[i].clean

    def join(self, s = None, **kwargs):
        """
        Join items in the list with the character in self.strsep
            - returns an Ansi object
        """
        if s == None:
            s = self.strsep
        else:
            s = Ansi( s, **kwargs )

        return s.join( self )

    def strip(self, item = None, *, strip_none = False ):
        """
        Removes any list items matching 'item'
            - returns a new AnsiList object
        """
        L = self.copy()
        def _filter(s):
            if ( item and s == item ) or ( not s and strip_none ):
                return False
            return True

        if item or not strip_none:
            return AnsiList( filter( _filter, self ), **self._kwargs )
        else:
            L = [ i for i in self ]
            for i in (0, -1):
                while L and not L[i]:
                    L.pop(i)
                return AnsiList( L, **self._kwargs )

    @__concat
    def extend(self, other):
        super().extend([ Ansi( i, **self._kwargs ) for i in other ])

ANSI_ITERABLES |= AnsiList
