from typing import Union

from apputils import listFlatten
from .types import FG_Color, BG_Color, AnsiEscape, AnsiCombo, Style, _setXtra_
from .ansitools import Ansi, AnsiList
from ._constants import getLogger

# def __rm_rep__(s):
#     s = s.replace('Dimmed(< ','').replace('Brightened(< ','').replace('Inverted(< ','')
#     return s.replace('Blended(< ','').replace('AnsiCombo(< ','').replace('AnsiColor(< ','').replace(' >)','')

class Dimmed(type):
    def __new__( cls, obj, n ):
        if n < 0 or n > 1:
            raise ValueError(f"'n' must be a value between 0 and 1")
        dim_val = n
        ext = {}
        name = f"{obj.__name__}_dimmed"
        _name = obj.name.split(' (')[0]
        if hasattr( obj, '__pre__' ):
            if obj.__pre__ == (38,2):
                rep = f"Dimmed(< {_name} (Fg) - %{int(n*100)} >)"
                _name = f"{_name} (Dimmed Fg)"
            else:
                rep = f"Dimmed(< {_name} (Bg) - %{int(n*100)} >)"
                _name = f"{_name} (Dimmed Bg)"
        else:
            rep = f"Dimmed(< {_name} (AnsiCombo) - %{int(n*100)} >)"
            _name = f"{_name} (Dimmed AnsiCombo)"

        code  = obj.__code__+'_dim'

    # Combo
        if isinstance( obj, AnsiCombo ):
            doc   = f"Dimmed AnsiCombo: {rep.replace('+','&')}"

            html = {}
            for k, v in obj.__ext__.items():
                if not isinstance( v, FG_Color|BG_Color ):
                    nm, item = k, v
                    ext[nm] = item
                else:
                    item = v.dim(n)
                    nm = item.__name__
                    ext[nm] = item

                if item.__com__:
                    doc += f"\n    - {item.__com__}"
                html = { **html, **item.__html__ }
                del nm, item

            esc   = tuple( v.__esc__ for v in ext.values() )

            R = type.__new__( AnsiCombo, name, (Dimmed,), { '__code__' : code,
                                                            '__doc__'  : doc,
                                                            '__esc__'  : esc,
                                                            '__ext__'  : ext,
                                                            '__pre__'  : (),
                                                            '__rep__'  : rep,
                                                            '__html__' : html,
                                                            'dim_value': dim_val,
                                                            'name'     : _name   })
            _setXtra_(R)
            return R

    # Color
        elif isinstance( obj, FG_Color ):
            base_type = FG_Color
        elif isinstance( obj, BG_Color ):
            base_type = BG_Color
        else:
            raise TypeError(f"Not a dimmable type - {type(obj)}")

        doc = f"Dimmed: {obj.__doc__}"
        rgb = cls.__dim__( cls, obj.rgb, dim_val )
        esc = obj.__pre__ + rgb

        if base_type == FG_Color:
            html = { 'color': f"rgb{rgb}" }
        else:
            html = { 'background-color': f"rgb{rgb}" }

        R = type.__new__( base_type, name, (Dimmed,), { '__code__' : code,
                                                        '__com__'  : obj.__com__,
                                                        '__doc__'  : doc,
                                                        '__esc__'  : esc,
                                                        '__ext__'  : ext,
                                                        '__html__' : html,
                                                        '__pre__'  : obj.__pre__,
                                                        '__rep__'  : rep,
                                                        'dim_value': dim_val,
                                                        'name'     : _name,
                                                        'rgb'      : rgb     })
        _setXtra_(R)
        return R

    def __dim__(self, rgb, n):
        from apputils import tupleCalc as tc
        RGB = []
        diff = tc( rgb, n, '*', round_int = True )
        for i in range(len(rgb)):
            a = 0 if diff[i] > rgb[i] else rgb[i] - diff[i]
            RGB.append(a)
            del a

        return tuple(RGB)

class Brightened(type):
    def __new__( cls, obj, n ):
        # print(f"{cls = }\n{obj = }\n{n = }\n")
        if n < 0 or n > 1:
            raise ValueError(f"'n' must be a value between 0 and 1")
        br_val = n
        ext = {}
        name = f"{obj.__name__}_brightened"
        _name = obj.name.split(' (')[0]
        if hasattr( obj, '__pre__' ):
            if obj.__pre__ == (38,2):
                rep = f"Brightened(< {_name} (Fg) - %{int(n*100)} >)"
                _name = f"{_name} (Brightened Fg)"
            else:
                rep = f"Brightened(< {_name} (Bg) - %{int(n*100)} >)"
                _name = f"{_name} (Brightened Bg)"
        else:
            rep = f"Brightened(< {_name} (AnsiCombo) - %{int(n*100)} >)"
            _name = f"{_name} (Brightened AnsiCombo)"

        code  = obj.__code__+'_bright'

    # Combo
        if isinstance( obj, AnsiCombo ):
            doc   = f"Brightened AnsiCombo: {rep.replace('+','&')}"
            html = {}
            for k, v in obj.__ext__.items():
                if not isinstance( v, FG_Color|BG_Color ):
                    nm, item = k, v
                    ext[nm] = item
                else:
                    item = v.bright(n)
                    nm = item.__name__
                    ext[nm] = item

                if item.__com__:
                    doc += f"\n    - {item.__com__}"
                html = { **html, **item.__html__ }
                del nm, item

            esc = tuple( v.__esc__ for v in ext.values() )
            R = type.__new__( AnsiCombo, name, (Brightened,), { '__code__'    : code,
                                                                '__doc__'     : doc,
                                                                '__esc__'     : esc,
                                                                '__ext__'     : ext,
                                                                '__pre__'     : (),
                                                                '__rep__'     : rep,
                                                                '__html__'    : html,
                                                                'bright_value': br_val,
                                                                'name'        : _name   })
            _setXtra_(R)
            return R

    # Color
        elif isinstance( obj, FG_Color ):
            base_type = FG_Color
        elif isinstance( obj, BG_Color ):
            base_type = BG_Color
        else:
            raise TypeError(f"Type {type(obj)} can not be brightened")

        doc = f"Brightened: {obj.__doc__}"
        rgb = cls.__br__( cls, obj.rgb, br_val )
        esc = obj.__pre__ + rgb

        if base_type == FG_Color:
            html = { 'color': f"rgb{rgb}" }
        else:
            html = { 'background-color': f"rgb{rgb}" }

        R = type.__new__( base_type, name, (Brightened,), { '__code__'    : code,
                                                            '__com__'     : obj.__com__,
                                                            '__doc__'     : doc,
                                                            '__esc__'     : esc,
                                                            '__ext__'     : ext,
                                                            '__html__'    : html,
                                                            '__pre__'     : obj.__pre__,
                                                            '__rep__'     : rep,
                                                            'bright_value': br_val,
                                                            'name'        : _name,
                                                            'rgb'         : rgb     })
        _setXtra_(R)
        return R

    def __br__(self, rgb, n):
        from apputils import tupleCalc as tc
        RGB = []
        _diff = [ 255 - i for i in rgb ]
        diff = tc( _diff, n, '*', round_int = True )
        for i in range(len(rgb)):
            a = diff[i] + rgb[i]
            if a > 255:
                a = 255
            RGB.append(a)
            del a

        return tuple(RGB)

class Blended(type):
    def __new__( cls, obj, other, n ):
        log = getLogger(__name__)
        if n < 0 or n > 1:
            raise ValueError(f"'n' must be a value between 0 and 1")
        elif not all( isinstance( i, FG_Color|BG_Color|AnsiCombo ) for i in ( obj, other )):
            raise TypeError(f"Can't blend types '{type(obj).__name__}' and '{type(other).__name__}'")

        blend_val = n
        ext = {}
        code  = '_'.join([ c[:2] for c in ( 'blend', obj.__code__, other.__code__ )])

        objcolors  = dict([( type(i), i ) for i in filter( lambda x: isinstance( x, FG_Color|BG_Color ), obj.extended() )])
        if not objcolors:
            objcolors = { type(obj): obj }

        othercolors = dict([( type(i), i ) for i in filter( lambda x: isinstance( x, FG_Color|BG_Color ), other.extended() )])
        if not othercolors:
            othercolors = { type(other): other }

        to_blend = [( objcolors[T], othercolors[T] ) for T in set(objcolors) & set(othercolors) ]
        log.debug(f"{obj = }, {other = }, {n = }")
        log.debug(f"{to_blend = }")
        if not to_blend:
            raise ValueError(f"No shared color types to blend {repr(obj)} and {repr(other)}")

    # Combo
        if isinstance( obj, AnsiCombo ):
            log.debug(f"Object to blend '{repr(obj)}' is type 'AnsiCombo'")
            styles = list(filter( lambda x: isinstance( x, Style ), obj.extended() ))

            names = []
            for A, B in to_blend:
                log.debug(f"Blending colors '{repr(A)}' and '{repr(B)}'")
                _blend = A.blend( B, n )
                objcolors.pop( type(A) )
                ext[ _blend.__name__ ] = _blend
                names.append( _blend.name.split(' (')[0] )
                del _blend

            ext = { **ext, **dict([( i.__name__, i ) for i in objcolors.values() ]), **dict([( i.__name__, i ) for i in styles ])}
            name = 'Blended.AnsiCombo'
            _name = ' + '.join(names + [ i.name for i in styles ])
            rep = f"Blended(< {_name} >)"

            doc_lists = AnsiList( listFlatten([ obj.__doc__.split('\n'),
                                                other.__doc__.split('\n'),
                                                *[ i.__doc__.split('\n') for i in styles ],
                                                ]),
                                strsep = '\n    ' )
            doc = f"Blended: {_name.replace('+','&')}\n    {doc_lists}"

            code = AnsiList( ['blend'], strsep = '_' )
            esc = ()
            html = {}
            for E in ext.values():
                code.append( E.__code__[:2] )
                esc += E.__esc__
                html = { **html, **E.__html__ }

            return type.__new__( AnsiCombo, name, (Blended,), { '__code__'    : str(code).clean,
                                                                '__doc__'     : doc,
                                                                '__esc__'     : esc,
                                                                '__ext__'     : ext,
                                                                '__pre__'     : (),
                                                                '__rep__'     : rep,
                                                                '__html__'    : html,
                                                                'blend_value': blend_val,
                                                                'name'        : _name   })

            ansi = objcolors.pop(0)
            while objcolors:
                ansi = ansi & objcolors.pop(0)
            while styles:
                ansi = ansi & styles.pop(0)

            for k, v in ext.items():
                if v.__com__:
                    doc += f"\n    - {v.__com__}"

    # Color
        elif isinstance( obj, FG_Color ):
            base_type = FG_Color
            suffix = 'Fg'
        elif isinstance( obj, BG_Color ):
            base_type = BG_Color
            suffix = 'Bg'
        else:
            raise TypeError(f"Type {type(obj)} can not be blended")


        log.debug(f"Object to blend '{repr(obj)}' is type '{base_type}'")
        bname = '||'.join([ i.name.split(' (')[0] for i in to_blend[0] ])
        rep = f"Blended(< {bname}- %{int(n*100)} >)"
        _name = f"{bname} (Blended {suffix})"
        name = f"{obj.__name__}_{other.__name__}_blend"
        rgb = cls.__blend__( obj, other, n )
        esc = obj.__pre__ + rgb

        if base_type == FG_Color:
            html = { 'color': f"rgb{rgb}" }
        else:
            html = { 'background-color': f"rgb{rgb}" }
        code = f"{obj.__code__[:2]}_{other.__code__[:2]}_blend"

        doc = str(AnsiList([ f"Blended: {bname}",
                             *[ f"    {i}" for i in obj.__doc__.split('\n') ],
                             *[ f"    {i}" for i in obj.__doc__.split('\n') ]],
                            strsep = '\n' ))

        R = type.__new__( base_type, name, (Blended,), { '__code__'   : code,
                                                         '__com__'    : obj.__com__,
                                                         '__doc__'    : doc,
                                                         '__esc__'    : esc,
                                                         '__ext__'    : ext,
                                                         '__html__'   : html,
                                                         '__pre__'    : obj.__pre__,
                                                         '__rep__'    : rep,
                                                         'blend_value': blend_val,
                                                         'name'       : _name,
                                                         'rgb'        : rgb     })
        _setXtra_(R)
        return R

    def __blend__(a, b, n):
        from apputils import tupleCalc as tc
        if n == 1:
            return b.rgb
        elif n == 0:
            return a.rgb

        return tc( tc( a.rgb, 1-n, '*' ), tc( b.rgb, n, '*' ), '+', round_int = True )

class Inverted(type):
    def __new__( cls, obj ):
        ext = {}
        name = f"{obj.__name__}_inverted"
        _name = obj.name.split(' (')[0]
        if hasattr( obj, '__pre__' ):
            if obj.__pre__ == (38,2):
                rep = f"Inverted(< {_name} (Fg) >)"
                _name = f"{_name} (Inverted Fg)"
            else:
                rep = f"Inverted(< {_name} (Bg) >)"
                _name = f"{_name} (Inverted Bg)"
        else:
            rep = f"Inverted(< {_name} (AnsiCombo) >)"
            _name = f"{_name} (Inverted AnsiCombo)"

        code  = obj.__code__+'_bright'

    # Combo
        if isinstance( obj, AnsiCombo ):
            doc   = f"Inverted AnsiCombo: {rep.replace('+','&')}"

            html = {}
            for k, v in obj.__ext__.items():
                if not isinstance( v, FG_Color|BG_Color ):
                    nm, item = k, v
                    ext[nm] = item
                else:
                    item = v.invert()
                    nm = item.__name__
                    ext[nm] = item

                if item.__com__:
                    doc += f"\n    - {item.__com__}"
                html = { **html, **item.__html__ }
                del nm, item

            esc = tuple( v.__esc__ for v in ext.values() )
            R = type.__new__( AnsiCombo, name, (Inverted,), { '__code__'    : code,
                                                              '__doc__'     : doc,
                                                              '__esc__'     : esc,
                                                              '__ext__'     : ext,
                                                              '__pre__'     : (),
                                                              '__rep__'     : rep,
                                                              '__html__'    : html,
                                                              'name'        : _name   })
            _setXtra_(R)
            return R

    # Color
        elif isinstance( obj, FG_Color ):
            base_type = FG_Color
        elif isinstance( obj, BG_Color ):
            base_type = BG_Color
        else:
            raise TypeError(f"Type {type(obj)} can not be inverted")

        doc = f"Inverted: {obj.__doc__}"
        rgb = cls.__inv__( cls, obj.rgb )
        esc = obj.__pre__ + rgb

        if base_type == FG_Color:
            html = { 'color': f"rgb{rgb}" }
        else:
            html = { 'background-color': f"rgb{rgb}" }

        R = type.__new__( base_type, name, (Inverted,), { '__code__'    : code,
                                                          '__com__'     : obj.__com__,
                                                          '__doc__'     : doc,
                                                          '__esc__'     : esc,
                                                          '__ext__'     : ext,
                                                          '__html__'    : html,
                                                          '__pre__'     : obj.__pre__,
                                                          '__rep__'     : rep,
                                                          'name'        : _name,
                                                          'revert'      : lambda: obj,
                                                          'rgb'         : rgb     })
        _setXtra_(R)
        return R

    def __inv__(self, rgb):
        from apputils import tupleCalc as tc
        RGB = []
        return tuple( abs( i - 255 ) for i in rgb )

# class HighContrast(type):                                         # TODO
#     def __new__( cls, obj ):
#         ext = {}
#         name = f"{obj.__name__}_inverted"
#         _name = obj.name.split(' (')[0]
#         if hasattr( obj, '__pre__' ):
#             if obj.__pre__ == (38,2):
#                 rep = f"Inverted(< {_name} (Fg) >)"
#                 _name = f"{_name} (Inverted Fg)"
#             else:
#                 rep = f"Inverted(< {_name} (Bg) >)"
#                 _name = f"{_name} (Inverted Bg)"
#         else:
#             rep = f"Inverted(< {_name} (AnsiCombo) >)"
#             _name = f"{_name} (Inverted AnsiCombo)"
#
#         code  = obj.__code__+'_bright'
#
#     # Combo
#         if isinstance( obj, AnsiCombo ):
#             doc   = f"Inverted AnsiCombo: {rep.replace('+','&')}"
#
#             html = {}
#             for k, v in obj.__ext__.items():
#                 if not isinstance( v, FG_Color|BG_Color ):
#                     nm, item = k, v
#                     ext[nm] = item
#                 else:
#                     item = v.invert()
#                     nm = item.__name__
#                     ext[nm] = item
#
#                 if item.__com__:
#                     doc += f"\n    - {item.__com__}"
#                 html = { **html, **item.__html__ }
#                 del nm, item
#
#             esc = tuple( v.__esc__ for v in ext.values() )
#             R = type.__new__( AnsiCombo, name, (Inverted,), { '__code__'    : code,
#                                                               '__doc__'     : doc,
#                                                               '__esc__'     : esc,
#                                                               '__ext__'     : ext,
#                                                               '__pre__'     : (),
#                                                               '__rep__'     : rep,
#                                                               '__html__'    : html,
#                                                               'name'        : _name   })
#             _setXtra_(R)
#             return R
#
#     # Color
#         elif isinstance( obj, FG_Color ):
#             base_type = FG_Color
#         elif isinstance( obj, BG_Color ):
#             base_type = BG_Color
#         else:
#             raise TypeError(f"Type {type(obj)} can not be inverted")
#
#         doc = f"Inverted: {obj.__doc__}"
#         rgb = cls.__inv__( cls, obj.rgb )
#         esc = obj.__pre__ + rgb
#
#         if base_type == FG_Color:
#             html = { 'color': f"rgb{rgb}" }
#         else:
#             html = { 'background-color': f"rgb{rgb}" }
#
#         R = type.__new__( base_type, name, (Inverted,), { '__code__'    : code,
#                                                           '__com__'     : obj.__com__,
#                                                           '__doc__'     : doc,
#                                                           '__esc__'     : esc,
#                                                           '__ext__'     : ext,
#                                                           '__html__'    : html,
#                                                           '__pre__'     : obj.__pre__,
#                                                           '__rep__'     : rep,
#                                                           'name'        : _name,
#                                                           'revert'      : lambda: obj,
#                                                           'rgb'         : rgb     })
#         _setXtra_(R)
#         return R
#
#     def __inv__(self, rgb):
#         from apputils import tupleCalc as tc
#         RGB = []
#         return tuple( abs( i - 255 ) for i in rgb )

# from apputils import tupleCalc
# from texttools import *
# bg = BG
# S = Styles
# c = FG
# bgi = c.B&bg.g&S.I
# _bg = c.B&bg.g
# B = c.B
