import re
from functools import wraps

# Session custom colors cache
from ._cache import _custom_colors_
from ._constants import getLogger

global _session_colors
_session_colors = _custom_colors_()
del _custom_colors_

from .escapes import AnsiEscapeDict as _ansiEscapeDict

from .texttools import TextTools
_ColorDict          = TextTools.ColorDict
_ColorDict16        = TextTools.ColorDict16
Ansi                = TextTools.Ansi
AnsiList            = TextTools.AnsiList
Cursor              = TextTools.Cursor
FG                  = TextTools.FG_Colors
BG                  = TextTools.BG_Colors
StyleDict           = TextTools.StyleDict
Styles              = TextTools.Styles
ansi2rgb            = TextTools.ansi2rgb
ansiMoneyFmt        = TextTools.money_fmt
blockTxt            = TextTools.blockTxt
fraction            = TextTools.fraction
hex2rgb             = TextTools.hex2rgb
rgb2ansi            = TextTools.rgb2ansi
rgb2hex             = TextTools.rgb2hex
rgbString           = TextTools.rgbString
rgbTo16             = TextTools.to16color
subscript           = TextTools.Sub
superscript         = TextTools.Sup
tuple2ansi          = TextTools.t2a
viewTextToolsHelp   = TextTools.help

class __new_color__:
    """
    Session colors saved in cache
    """

    def __color_getter(func):
        @wraps(func)
        def __call(self, *args, __no_call__ = False, **kwargs):
            if __no_call__:
                return func( self, *args, **kwargs )
            return self.__call__( *args, **kwargs )
        return __call

    def __call__(self, *args, **kwargs):
        log = getLogger("Colors.new")
        run = lambda a, skip = {'__no_call__': True}, kw = kwargs: self.mkColor( a, **skip, **kw )
        try:
            if len(args) == 3 and all( isinstance(i, int) and i in range(256) for i in args ):
                R = run( args )
            elif len(args) == 1 and isinstance( args[0], str ) and re.match( '^#?[A-Fa-f0-9]{6}$', args[0] ):
                rgb = hex2rgb( args[0].replace('#','') )
                R = run( rgb )
            elif len(args) == 1 and isinstance(args[0], list|tuple) \
                and all( isinstance(i, int) and i in range(256) for i in args[0] ):
                    R = run( args[0] )
            else:
                raise SyntaxError(f"Invalid argument for 'args' - '{args}'")

            return R

        except Exception as E:
            log.exception(E)
            return ''

    @__color_getter
    def mkColor(cls, rgb: list|tuple, **kwargs):
        """
        Create a color
          - returns color match if 'arg' is found in colors
            'arg': hex string or rgb tuple

            **kwargs:
                - options for creating a color from an rgb value [optional]

              'code'  : str() extra attribute name to add to FG and BG color classes
              'name'  : str() color name
              'prefix': tuple() only used to signify whether to return FG or BG ansi code
                         - default returns FG
                         - can also return bg color by signifying 'bg' in the color name
              'comment': str() adds to attribute's docstring
        """
        log = getLogger("Colors.new")
        try:
            if not ( isinstance( rgb, list|tuple ) and len(rgb) == 3 \
                and all( isinstance( i, int ) and i in range(256) for i in rgb )):
                    raise SyntaxError(f"Invalid argument for 'rgb' - '{rgb}'")

            existing = Colors.fromRGB(rgb)
            if existing:
                return existing

            valid_opts = set(['code', 'name', 'prefix', 'comment'])
            for i in set(kwargs).symmetric_difference( valid_opts ) & set(kwargs):
                log.warning(f"Invalid kwarg '{i}' - valid kwargs -> {tuple(valid_opts)}")

            opts = { **dict([(k, kwargs[k]) for k in set(kwargs) & valid_opts ]),
                     '_FG_': FG,
                     '_BG_': BG,
                     'rgb' : rgb    }

            return _session_colors( **opts )

        except Exception as E:
            log.exception(E)
            return ''

class Colors:
    FG = FG
    BG = BG
    Styles = Styles
    new = __new_color__()

    @classmethod
    def names(cls):
        """ Returns name list of all color/style objects """
        return [ *cls.FG.names(), *cls.BG.names(), *cls.Styles.names() ]

    @classmethod
    def codeItems(cls):
        """
        Returns ( code, object ) items list of all color/style objects
            - foreground and background colors share the same codes
        """
        return [ ( '_', cls.Styles._ ), *[( i.__code__, i ) for i in cls.FG.values() + cls.BG.values() + cls.Styles.values() ]]

    @classmethod
    def codes(cls):
        """
        Returns list of all color codes (shortened names)
            - foreground and background colors share the same codes
        """
        return [ '_', *cls.FG.codes(), *cls.Styles.codes() ]

    @classmethod
    def _allnames_(cls):
        """
        Dictionary of of name variations to search for color/style objects
        """
        return { **cls.FG._allnames_(), **cls.BG._allnames_(), **cls.Styles._allnames_() }

    @classmethod
    def values(cls):
        """ Return all color/style objects """
        return [ *cls.FG.values(), *cls.BG.values(), *cls.Styles.values() ]

    @classmethod
    def items(cls):
        """ Return ( name, object ) items list of all color/style objects """
        return [ *cls.FG.items(), *cls.BG.items(), *cls.Styles.items() ]

    @classmethod
    def get(cls, *names):
        """
        Provide 1 or more names of colors or styles
            - returns AnsiColor, AnsiStyle, or AnsiCombo
        """
        from apputils import matchSimilar
        log = getLogger(__name__)
        _D = cls._allnames_()
        items = []
        for name in names:
            try:
                _item = matchSimilar( name, list(_D) )
                if not _item:
                    log.error(f"Couldn't find item '{name}'")
                    continue

                _item = _D[ _item ]
                if _item not in items:
                    items.append(_item)
                else:
                    log.warning(f"Item '{_item.__name__}' added more than once")
            except Exception as E:
                log.exception(E)

        try:
            assert items
            if FG._ in items:
                item = items.pop( items.index( FG._ ))
            else:
                item = items.pop(0)

            while items:
                item = item & items.pop(0)

        except AssertionError:
            log.error(f"Invalid color/style name(s) - {names}")
            return None
        except Exception as E:
            log.exception(E)
            return None
        return item

    @classmethod
    def fromHex(cls, H):
        log = getLogger(__name__)
        try:
            return cls.fromRGB( hex2rgb( H ))
        except Exception as E:
            log.exception(E)
            raise

    @classmethod
    def fromRGB(cls, rgb):
        log = getLogger(__name__)
        try:
            assert isinstance( rgb, list|tuple ) and len(rgb) == 3 \
                and all( isinstance( i, int ) and i in range(256) for i in rgb )
        except Exception as E:
            log.exception("'rgb' must be tuple of integers")
            raise

        rgbD = dict([( i['rgb'], i ) for i in TextTools.ColorDict.values() ])
        if rgb in rgbD:
            return getattr( FG, rgbD[rgb]['name'] )
        return None

getColor = Colors.get
newColor = Colors.new

__all__ = [ 'Ansi',
            'AnsiList',
            'BG',
            'Colors',
            'Cursor',
            'FG',
            'StyleDict',
            'Styles',
            'TextTools',
            'ansi2rgb',
            'ansiMoneyFmt',
            'blockTxt',
            'fraction',
            'getColor',
            'hex2rgb',
            'newColor',
            'rgb2ansi',
            'rgb2hex',
            'rgbString',
            'rgbTo16',
            'subscript',
            'superscript',
            'tuple2ansi',
            'viewTextToolsHelp',
            ]


