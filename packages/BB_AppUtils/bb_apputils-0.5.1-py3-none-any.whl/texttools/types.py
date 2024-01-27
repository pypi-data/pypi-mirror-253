import os, re
from functools import wraps, update_wrapper
from glob import glob
from datetime import datetime as dt
from typing import Union

from ._constants import ( COMPARE_FUNCTIONS,
                          STRING_FUNCTIONS,
                          RE_RGB_ESCAPE,
                          RE_16COLOR_ESCAPE,
                          RE_STYLE_ESCAPE,
                          ANSI_MOD_PERCENTAGE,
                          getLogger,
                          )
from .ansitools import Ansi
from apputils import listFlatten, isSafeAttribName, AppData, Path

def _setXtra_(cls):
    setattr( cls, 'dim'     , lambda n = 10: _dim_(cls, n)    )
    setattr( cls, 'bright'  , lambda n = 10: _bright_(cls, n) )
    setattr( cls, 'blend'   , lambda obj, n = 5: _blend_(cls, obj, n)  )
    setattr( cls, 'invert'  , lambda: _invert_(cls) )

def __percent__(n = 0):
    log = getLogger(__name__)
    try:
        if isinstance( n, str ):
            assert re.match( '^[0-9]*\.?[0-9]+$', n )
            if n.find('.') >= 0:
                n = float(n)
            else:
                n = int(n)

        n = abs(n)
        if ( isinstance( n, int ) and n >= 1 ) or n > 1:
            return n*.01
        return n
    except Exception as E:
        log.exception(E)
        raise

def _bright_(cls, n = ANSI_MOD_PERCENTAGE):
    from .color_mods import Brightened
    p = __percent__(n)
    return Brightened( cls, p )

def _dim_(cls, n = ANSI_MOD_PERCENTAGE):
    from .color_mods import Dimmed
    p = __percent__(n)
    return Dimmed( cls, p )

def _blend_(cls, other, n = ANSI_MOD_PERCENTAGE):
    from .color_mods import Blended
    p = __percent__(n)
    return Blended( cls, other, p )

def _invert_(cls):
    if hasattr( cls, 'revert' ):
        return cls.revert()
    from .color_mods import Inverted
    return Inverted(cls)

class AnsiEscapeMeta(type):
    def __new__(cls, name, bases, clsDict):
        clsDict = { '__code__'  : '',
                    '__com__'   : '',
                    '__doc__'   : '',
                    '__esc__'   : (),
                    '__ext__'   : {},
                    '__invert__': cls._mod_wrapper_( cls.__invert__ ),        # TODO
                    '__pre__'   : '',
                    '__html__'  : {},
                    '__neg__'   : cls._mod_wrapper_( cls.__neg__ ),
                    '__pos__'   : cls._mod_wrapper_( cls.__pos__ ),
                    '__or__'    : cls._ior_wrapper_( cls.__ior__ ),
                    '__rep__'   : '',
                    '__s__'     : Ansi(),
                    'name'      : '',
                    'rgb'       : (),
                    'ansi'      : (),
                    **clsDict       }
        clsDict['__ior__'] = clsDict['__or__']

        return type.__new__( cls, name, bases, clsDict )

    def __instancecheck__(self, other):
        # print(f"{self = }\n{other = }")
        if hasattr( other, '__bases__' ) and self in other.__bases__:
            return True

        types = [ type(other) ]
        if hasattr( other, '__ext__' ) and len(other.__ext__) >= 2:
            types += [ *other.extendedTypes(), AnsiCombo ]

        types = set(types)
        if self in types:
            return True
        else:
            return super().__instancecheck__(other)

    def _ior_wrapper_(func):
        @wraps(func)
        def __inner(self, other, n = ANSI_MOD_PERCENTAGE):
            try:
                if func.__name__ == '__ror__':
                    assert isinstance( other, AnsiEscape ) and hasattr( other, '__or__' )
                    return func( self, other, n )

                types = set( [type(self)]+[ type(i) for i in filter( lambda x: isinstance( x, FG_Color|BG_Color ), [ v for k, v in self.__ext__.items() ])])
                othertypes = set( [type(other)]+[ type(i) for i in filter( lambda x: isinstance( x, FG_Color|BG_Color ), [ v for k, v in other.__ext__.items() ])])
                n = __percent__(n)
                if not types:
                    raise RuntimeError
                assert othertypes
                if not types & othertypes:
                    raise ValueError
            except RuntimeError:
                raise TypeError(f"{repr(self)} doesn't support the blend method")
            except AssertionError:
                raise TypeError(f"{repr(other)} doesn't support the blend method")
            except ValueError:
                raise ValueError(f"No shared color types to blend {repr(self)} and {repr(other)}")

            return func( self, other, n )
        return __inner

    def _mod_wrapper_(func):
        @wraps(func)
        def __inner(cls, n = ANSI_MOD_PERCENTAGE):
            attr = { '__neg__': 'dim', '__pos__': 'bright', '__invert__': 'invert' }
            if not hasattr( cls, attr[ func.__name__ ] ):
                raise TypeError(f"Ansi type '{type(self).__name__}' has no attribute '{attr[func.__name__]}'")
            return func(cls, n)
        return __inner

    def __neg__(self, n):
        return _dim_( self, n )

    def __pos__(self, n):
        return _bright_( self, n )

    def __invert__(self, n):
        return _invert_( self )

    def __ior__(self, other, n):
        return _blend_( self, other, n )

class AnsiEscape(metaclass = AnsiEscapeMeta):
    def _Escape_Wrapper_(func):
        """ Wrapper for Color and Style types """
        @wraps(func)
        def __inner(self, other = 'pass'):
            log = getLogger(__name__)
            fn = func.__name__
            try:
                if other == 'pass':
                    return

                assert isinstance( other, AnsiEscape )
                log.debug(f"{self = }, {other = }, {func = }")
                if fn in ( '__eq__', '__ne__' ):
                    _self, _other = self.escapes(), other.escapes()
                elif self.name == other.name:
                    _self, _other = len( self.escapes() ), len( other.escapes() )
                elif self.name.split()[-1] != other.name.split()[-1]:
                    _self, _other = self.name.split()[-1], other.name.split()[-1]
                else:
                    _self, _other = self.name, other.name

                log.debug(f"{_self = }, {_other = }")
                return func( self, _self, _other )

            except:
                pass
        return __inner

    def __format__( self, format_spec = '' ): return Ansi( f"\x1b[{';'.join([ str(i) for i in listFlatten( self.__esc__, tuples = True ) ])}m" ).__format__( format_spec )
    def __str__(self)                       : return Ansi( f"\x1b[{';'.join([ str(i) for i in listFlatten( self.__esc__, tuples = True ) ])}m" )
    def __len__(self)                       : return len( Ansi( '\x1b[' + ';'.join([ str(i) for i in listFlatten( self.__esc__, tuples = True ) ]) + 'm' ) )
    def __bool__(self)                      : return True
    def __add__( self, other )              : return Ansi( f"\x1b[{';'.join([ str(i) for i in listFlatten( self.__esc__, tuples = True ) ])}m{other}" )
    def __radd__( self, other )             : return Ansi( f"{other}\x1b[{';'.join([ str(i) for i in listFlatten( self.__esc__, tuples = True ) ])}m" )
    # def __repr__(self)                      : return self.__rep__
    @_Escape_Wrapper_
    def __eq__( self, _self, other ): return _self == other
    @_Escape_Wrapper_
    def __ne__( self, _self, other ): return _self != other
    @_Escape_Wrapper_
    def __gt__( self, _self, other ): return _self >  other
    @_Escape_Wrapper_
    def __ge__( self, _self, other ): return _self >= other
    @_Escape_Wrapper_
    def __lt__( self, _self, other ): return _self <  other
    @_Escape_Wrapper_
    def __le__( self, _self, other ): return _self <= other

    def _and_wrapper_(func):
        @wraps(func)
        def __inner(self, other, **kwargs):
            log = getLogger(__name__)
            if not isinstance( other, AnsiEscape ):
                log.debug(f"Not an AnsiEscape object 'other' = '{type(other)}'")
                if isinstance( other, str|Ansi ):
                    if func.__name__ == '__and__':
                        log.debug("Returning as a string using __add__")
                        return self.__add__( other )
                    else:
                        log.debug("Returning as a string using __radd__")
                        return self.__radd__( other )
                raise TypeError(f"Can only add attributes from other AnsiEscape types, not '{type(other)}'")

            try:
                tmp_ext = False
                if not self.__ext__:
                    self.__ext__ = { self.__name__: self }
                    tmp_ext = True

                if type(other) in ( FG_Color, BG_Color ) and type(other) in self.extendedTypes():
                    raise ValueError(f"'{self.__name__}' already contains attribute type '{type(other).__name__}'")

                matches = [ i.replace('rm_','') for i in self.extendedNames() ]
                othername = other.__name__.replace('RM_','').replace('STYLE_','')
                if othername in matches:
                    raise ValueError(f"'{self.__name__}' already contains '{othername}' attributes")

                elif isinstance( other, Reset ):
                    raise TypeError("Can't add 'Reset' type to another attribute")

                R = Combo( self, other, **kwargs )
                if tmp_ext:
                    self.__ext__ = {}
                return R

            except Exception as E:
                if tmp_ext:
                    self.__ext__ = {}
                log.exception(E)
                raise
        return __inner

    @_and_wrapper_
    def __rand__(self, other):
        return str(other)+str(self)
    @_and_wrapper_
    def __and__(self, other):
        return str(self)+str(other)

    def escapes(self):
        """ Return flattened list of esape integers """
        return listFlatten( self.__esc__, tuples = True )

    def extended(self):
        """ Return list of extended escape values """
        return [ v for k, v in self.extendedItems() ]

    def extendedItems(self):
        """ Return item list of extended escapes """
        return self.__ext__.items()

    def extendedNames(self):
        """ Return extended escape names """
        return [ k for k, v in self.extendedItems() ]

    def extendedTypes(self):
        """ Return list of extended types """
        return list({ type(v) for k, v in self.extendedItems() })

    def hex_codes(self):
        def getHex(_h):
            return '#'+''.join([ f"%0{int(6/len(_h))}x" for i in range(int(len(_h))) ])%_h

        st_type = { 0: 'reset', 1: 'bold', 3: 'italic', 4: 'underline', 5: 'blink', 9: 'strikethrough' }
        fg, bg, styles = '', '', {}
        for esc in self.extended():
            s = ','.join(esc)
            if s.startswith('38,2'):
                h['fg'] = getHex(esc)
            elif s.startswith('48,2'):
                h['bg'] = getHex(esc)
            else:
                styles[st_type[esc[0]]] = getHex(esc)

        H = { 'fg': fg,
              'bg': bg,
              'styles': None if not styles else type( 'styles', (), styles )() }

        return type( 'HexCodes', (), H )()

    def htmlItems(self):
        return self.__html__.items()

    def htmlStyle(self):
        return f'''style="{'; '.join([ f'{k}: {v}' for k, v in self.__html__.items() ])}"'''

    def htmlKeys(self):
        return [ k for k, v in self.__html__.items() ]

    def htmlValues(self):
        return [ v for k, v in self.__html__.items() ]

    def prefix(self):
        """ Return color prefix tuple """
        return self.__pre__

class FG_Color(type, AnsiEscape):
    def __new__( cls, name, bases, clsDict ):
        return AnsiEscape.__new__( cls, name, (_Mod_,)+bases, clsDict )
    def __repr__(self): return self.__rep__
    def bg(self): return AnsiColor( name = self.__name__,
                                    code = self.__code__,
                                    prefix = (48,2),
                                    rgb = self.rgb,
                                    comment = self.__com__  )
    def fg(self): return self

class BG_Color(type, AnsiEscape):
    def __new__( cls, name, bases, clsDict ):
        if not name.startswith('bg_'):
            name = 'bg_'+name
        return AnsiEscape.__new__( cls, 'bg_'+name, bases, clsDict )
    def __repr__(self): return self.__rep__
    def fg(self): return AnsiColor( name = self.__name__[3:],
                                    code = self.__code__,
                                    prefix = (38,2),
                                    rgb = self.rgb,
                                    comment = self.__com__  )
    def bg(self): return self

class Style(type, AnsiEscape):
    def __new__( cls, name, bases, clsDict ):
        return AnsiEscape.__new__( cls, name, bases, clsDict )
    def __repr__(self): return self.__rep__

class Reset(type, AnsiEscape):
    def __new__( cls, name, bases, clsDict ):
        return AnsiEscape.__new__( cls, name, bases, clsDict )
    def __repr__(self): return self.__rep__

class AnsiCombo(type, AnsiEscape):
    def __new__( cls, name, bases, clsDict ):
        return AnsiEscape.__new__( cls, name, bases, clsDict )
    def __repr__(self): return self.__rep__

class AnsiColor:
    """ Color Escape """

    def __new__( cls, *args, name, code, prefix, rgb, ext = {}, comment = '', **kwargs ):
        rgb = tuple(rgb)
        pre = tuple(prefix)
        esc = pre + rgb
        html = {}

        if pre == (38,2):
            _name = name.title().replace('_',' ').strip() + ' (Fg)'
            base_type = FG_Color
            doc = f"Ansi foreground color"
            html = { 'color': f"rgb{rgb}" }
        elif pre == (48,2):
            _name = name.title().replace('_',' ').strip() + ' (Bg)'
            base_type = BG_Color
            doc = f"Ansi background color"
            html = { 'background-color': f"rgb{rgb}" }
        else:
            raise TypeError(f"Invalid prefix for AnsiColor '{pre}'")

        if '_name' in kwargs:
            _name = kwargs['_name']

        rep = f"AnsiColor(< {_name} >)"

        if comment:
            doc += f"\n  - {comment}"

        clsDict = { '__code__' : code,
                    '__com__'  : comment,
                    '__doc__'  : doc,
                    '__esc__'  : esc,
                    '__ext__'  : ext,
                    '__html__' : html,
                    '__pre__'  : pre,
                    '__rep__'  : rep,
                    'hex'      : '#%02x%02x%02x'%rgb,
                    'name'     : _name,
                    'rgb'      : rgb,
                    }

        R = type.__new__( base_type, name, (), clsDict )
        _setXtra_(R)
        return R

class AnsiStyle:
    def __new__( cls, *args, name, code, html, ansi, key = '', ext = {}, comment = '' ):
        ansi = tuple(ansi)
        _name = name.title().replace('_',' ').strip()

        rep = f"AnsiStyle(< {_name} >)"
        if comment:
            doc = f"Ansi style: {_name}\n  - {comment}"
        else:
            doc = f"Ansi style: {_name}"

        if name == 'reset':
            base_type = Reset
        else:
            base_type = Style
            if name.startswith('remove_'):
                name = f"{name.replace('remove_','rm_')}"
            else:
                name = f"{name}"

        esc = ansi
        ext = {}
        pre = ()

        clsDict = { '__code__': code,
                    '__com__' : comment,
                    '__doc__' : doc,
                    '__esc__' : esc,
                    '__ext__' : ext,
                    '__html__': html,
                    '__pre__' : pre,
                    '__rep__' : rep,
                    'name'    : _name,
                    'ansi'    : ansi,
                    }

        return type.__new__( base_type, name, (), clsDict )

class Combo:
    def __new__( cls, base, other, *, key = '', **kwargs ):
        baserep = base.__rep__.replace('AnsiCombo(< ','').replace('AnsiColor(< ','').replace('AnsiStyle(< ','').replace(' >)','')
        otherrep = other.__rep__.replace('AnsiCombo(< ','').replace('AnsiColor(< ','').replace('AnsiStyle(< ','').replace(' >)','')

        doc   = f"AnsiCombo: {baserep.replace('+','&')} & {otherrep}"
        code  = other.__code__
        ext   = { **base.__ext__, other.__name__: other }
        esc   = tuple( v.__esc__ for k, v in ext.items() )
        if key:
            rep   = f"AnsiCombo(< {baserep} + {otherrep} [{key}] >)"
            name  = f"{baserep} + {otherrep} ({key})"
            doc = f"{doc} ({key})"
            clsName = f"{key}.AnsiCombo"
        else:
            clsName = "AnsiCombo"
            name  = f"{baserep} + {otherrep}"
            rep   = f"AnsiCombo(< {baserep} + {otherrep} >)"

        for k, v in ext.items():
            if v.__com__:
                doc += f"\n    - {v.__com__}"

        html = base.__html__.copy()
        for k, v in other.__html__.items():
            if k in html and html[k] not in ( 'normal', 'none' ):
                html[k] = f"{html[k]} {v}"
            else:
                html[k] = v

        bases = ()
        if '__type__' in kwargs:
            bases = (kwargs.pop('__types__'),)

        clsDict = { '__code__': code,
                    '__rep__' : rep,
                    '__esc__' : esc,
                    '__doc__' : doc,
                    '__ext__' : ext,
                    '__pre__' : (),
                    '__html__': html,
                    'name'    : name,
                    **kwargs,
                    }

        R = type.__new__( AnsiCombo, clsName, bases, clsDict )
        for n, item in R.__ext__.items():
            setattr( R, n, item )

        if any( i in [ type(a) for a in R.extended() ] for i in ( FG_Color, BG_Color )):
            _setXtra_(R)
        return R
