from __future__ import division
import string
import os, sys, json, re, operator, pickle

from datetime import datetime as dt
from os.path import ( abspath,
                      basename as BN,
                      dirname as DN,
                      isabs,
                      isfile,
                      isdir,
                      join as JN,
                      sep as pathsep,
                      splitext )
from shutil import move as MV
from difflib import SequenceMatcher
from functools import wraps, partial
from dataclasses import is_dataclass
from typing import Union, Any

from ._constants import STRING_SEQUENCE_MATCH_RATIO, getLogger
from ._file_lock import AtomicOpen
from .project import findProjectName

def filterList(_list, match, index = None, *, not_in = False, _type = None):
    if not isinstance( match, list|tuple|dict ):
        match = [match]
    if isinstance( index, int ):
        if not_in:
            R = list(filter( None, [ i[index] if i not in match else None for i in _list ]))
        else:
            R = list(filter( None, [ i[index] if i in match else None for i in _list ]))
    elif not_in:
        R = list(filter( None, [ i[index] if i not in match else None for i in _list ]))
    else:
        R = list(filter( None, [ i[index] if i in match else None for i in _list ]))

    if _type:
        return [ type(_type)(i) for i in R ]
    return R

def getBoolFromString(s):
    s = s.lower()
    if s in ( 'true', 'yes', '1', 'y' ):
        return True
    elif s in ( 'false', 'no', '0', 'n' ):
        return False
    else:
        raise ValueError(f"Invalid boolean string - '{s}'")

def getIndexed(item, args):
    """
    getIndexed(item, args) >>> ( item, args )
        Get item from list of arguments. Returns ( indexed item, args minus item )
      if found else ( None, original args )
    """
    log = getLogger(__name__)
    args = list(args)
    try:
        i = args.index( item )
        val = args.pop(i)
        return ( val, args )
    except:
        log.warning(f"Item '{item}' not found in argument list")
        return ( None, args )

def isBinary(filename):
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
    with open( filename, 'rb' ) as f:
        B = is_binary_string( f.read() )
    return B

def attribNameFromString(string):
    s = string.replace(' ', '_').replace('-', '_')
    while s.find('__') >= 0:
        s = s.replace('__','_')
    while s and not re.match( '^[A-Za-z_]+', s ):
        s = s[1:]
    s = ''.join( re.findall( '[A-Za-z0-9_]', s ))
    if not s:
        raise ValueError(f"Could not create a valid attribute name from '{string}'")
    return s

def matchSimilar(find, _list, *, ratio = STRING_SEQUENCE_MATCH_RATIO, getall = False, getalldata = False):
    finds = []
    if isinstance( _list, str|int|float ):
        _list = list(_list)
    elif not hasattr( _list, '__iter__' ):
        raise TypeError(f"Invalid iterable for matchSimilar() - '{type(_list)}'")

    if getalldata:
        getall = True

    for i in _list:
        r = SequenceMatcher(None, find, i).ratio()
        if r >= ratio:
            finds.append((r, i))

    if not finds and getall:
        return []
    elif not finds:
        return None

    finds = tuple(sorted( finds, key = lambda x:x[0], reverse = True ))
    if getalldata:
        return finds
    elif getall:
        return tuple( i[1] for i in finds )

    return finds[0][1]

def mkData(obj):
    """
    Make data dictionary from dataclass, ignoring keys that start with '_'
        - embedded dataclasses are recursively moved to a dict() object as well
    """
    data = {}
    for k, v in obj.__dict__.items():
        if k.startswith('_'):
            continue
        elif is_dataclass(v):
            data[k] = mkData(v)
            continue
        data[k] = v
    return data

def parseDate(s, fmt = ''):
    log = getLogger(__name__)
    if isinstance( s, dt ):
        if fmt:
            return s.strftime(fmt)
        else:
            return s
    try:
        log.debug(f"Attempting to parse date '{s}'")
        date = parser.parse(s)
        if fmt:
            return date.strftime(fmt)
        else:
            return date
    except Exception as E:
        log.exception(E)
        raise E

def isSafeAttribName(name):
    return bool( isinstance( name, str ) and re.match( '^[a-zA-Z_]+[a-zA-Z0-9_]*$', name ))

def greatestComDen( *integers ):
    from math import gcd
    if not all( isinstance( i, int ) for i in integers ):
        raise TypeError(f"Invalid tuple '{integers}' - Can only find lowest common denominator in a tuple of integers")
    _gcd = gcd( *integers )

    R = tuple( int( i / _gcd ) for i in integers )
    if len(R) == 1:
        return R[0]
    return R

def sqrt( *integers ):
    from math import sqrt as sr
    R = tuple( sr(i) for i in integers )
    if len(R) == 1:
        return R[0]
    return R

def tupleCalc( a, b, op, *, diff = False, round_int = False ):
    log = getLogger(__name__)
    import math
    def _roundToInt(*tuples):
        R = []
        for t in tuples:
            R.append( tuple( int(round(i)) for i in t ))
        if len(R) == 1:
            return R[0]
        return tuple(R)

    def _floordiv(a, b):
        R_flr, R_mod = [], []
        for _a, _b in zip(a, b):
            ra, rb = operator.floordiv( _a, _b )
            R_flr.append( ra )
            R_mod.append( rb )
        return ( tuple(R_flr), tuple(R_mod) )

    ops = { '+'   : operator.add,
            '-'   : operator.sub,
            '/'   : operator.truediv,
            '//'  : operator.floordiv,
            '*'   : operator.mul,
            '**'  : operator.pow,
            '%'   : operator.mod,
            }

    log.debug(f"Calculating '{a} {op} {b}'")
    try:
        if isinstance( b, int|float ) and isinstance( a, list|tuple ):
            b = [ b for i in range(len(a))]
        elif isinstance( a, int|float ) and isinstance( b, list|tuple ):
            a = [ a for i in range(len(b))]

        if all( isinstance( i, int|float ) for i in (a, b) ):
            a, b = [a], [b]
        else:
            assert all( isinstance( args, list|tuple ) and all( isinstance( i, int|float ) for i in args ) for args in (a, b) )
            a = list(a)
            b = list(b)

        while len(a) < len(b):
            if op in ('*','/','**','//','%'):
                a.append(1)
            else:
                a.append(0)
        while len(b) < len(a):
            if op in ('*','/'):
                b.append(1)
            else:
                b.append(0)
    except:
        raise SyntaxError(f"Invalid tuples {a = }, {b = }")

    if op not in ops:
        raise ValueError(f"Invalid operator value - '{op}'")

    result = tuple( ops[op]( _a, _b ) for _a, _b in zip( a, b ))
    if not diff:
        if round_int:
            return tuple( int(round(i)) for i in result )
        else:
            return result

    R = []
    for _a, _b in zip( a, result ):
        R.append( abs( _a - _b ))
        # while any( _i < 0 for _i in ( _a, _b )):
        #     _a += 1
        #     _b += 1
        # r0, r1 = sorted([ _a, _b ])
        # R.append( r1 - r0 )

    m_index = len(R)/2
    if m_index % 1 == 0:
        median = ( R[int(m_index)] + R[int(m_index-1)] )/2
    else:
        median = R[ int(m_index) ]

    max_diff = sorted(R)[-1]
    min_diff = sorted(R)[0]
    min_max_avg = ( max_diff + min_diff ) / 2
    mean = sum(R) / len(R)

    if round_int:
        R = _roundToInt(R)
    else:
        R = tuple(R)

    cls = type( 'TupleDiff', (tuple,), { '__new__'    : tuple.__new__,
                                         'mean'       : mean,
                                         'median'     : median,
                                         'max'        : max_diff,
                                         'min'        : min_diff,
                                         'min_max_avg': min_max_avg })
    return cls( R )

def readFile( path, *, mode = None, encoding = 'utf-8', **kwargs ):
    log = getLogger(__name__)
    try:
        assert isfile(path)
    except AssertionError as E:
        log.exception(f"File '{path}' doesn't exist!")
        raise

    R = None
    if mode == None:
        if isBinary(path):
            mode = 'rb'
        else:
            mode = 'r'
            kwargs['encoding'] = encoding

    else:
        assert mode in ( 'r', 'rb', 'b' )
        if mode == 'b':
            mode = 'rb'
        elif mode == 'r':
            kwargs['encoding'] = encoding
            kwargs['errors'] = 'ignore'

    with AtomicOpen( path, mode, **kwargs ) as f:
        R = f.read()
    return R

def writeFile( path, data, *, mode = 'w', encoding = 'utf-8', **kwargs ):
    assert isinstance( data, str )
    assert mode in ( 'w', 'wb', 'a', 'ab' )
    if mode == 'b':
        mode = 'wb'

    with AtomicOpen( path, mode, encoding = encoding, **kwargs ) as f:
        f.write(data)

def appendFile( path, data, *, mode = 'a', encoding = 'utf-8', **kwargs ):
    assert mode in ( 'a', 'ab', 'b' )
    if mode == 'b':
        mode = 'ab'
    return writeFile( path, mode, encoding = encoding, **kwargs )

def uniqueName(path, *, move_existing = False):
    log = getLogger(__name__)
    log.debug(f"Creating unique name for '{path}'")
    try:
        fn, ext = splitext(path)
    except:
        fn = path
        ext = ''

    newpath, c = abspath(path), 1
    existing = []
    while isfile(newpath):
        existing.append( newpath )
        newpath = f"{fn} ({c}){ext}"
        c += 1

    if move_existing and existing:
        while existing:
            old = existing.pop(-1)
            log.debug(f"Moving old file '{Path.bn(old)}' to '{newpath}'")
            Path.mv( old, newpath )
            newpath = old

    log.debug(f"Returning '{newpath}'")
    return newpath

def stringFilter( obj: Any, *, func = None, start = [], end = [], re_search: re.compile = None, re_match: re.compile = None):
    if func:
        if not hasattr( func, '__call__' ):
            raise TypeError("'func' must ba a callable function or class")
        L = func(obj)
        if not hasattr( L, '__iter__' ):
            raise TypeError("Function returned an invalid type - must be iterable")
    else:
        L = obj
        if not hasattr( L, '__iter__' ):
            raise TypeError("Invalid type for 'obj' - must be iterable")

    if ( re_search and not isinstance( re_search, re.compile )) \
        or ( re_match and not isinstance( re_match, re.compile )):
            raise TypeError(f"'re_*' must be type 're.compile'")

    _end, _noend, _start, _nostart = [], [], [], []

    if isinstance( start, str ):
        start = [start]
    for s in start:
        if s.startswith('\\'):
            _start.append(s[1:])
        elif s.startswith('!_'):
            _nostart.append(s[2:])
        else:
            _start.append(s)

    if isinstance( end, str ):
        end = [end]
    for s in end:
        if s.startswith('!_'):
            _noend.append(s[2:])
        else:
            _end.append(s)

    def _start_(s):
        return bool( not _start or any( s.startswith(i) for i in _start ))
    def _nostart_(s):
        return bool( not _nostart or all( not s.startswith(i) for i in _nostart ))
    def _end_(s):
        return bool( not _end or any( s.endswith(i) for i in _end ))
    def _noend_(s):
        return bool( not _noend or all( not s.endswith(i) for i in _noend ))
    def _re_search_(s):
        return bool( not re_search or re_search.search(s) )
    def _re_match_(s):
        return bool( not re_match or re_match.match(s) )
    def _filter(s):
        return all( F(s) for F in ( _end_,
                                    _noend_,
                                    _start_,
                                    _nostart_,
                                    _re_match_,
                                    _re_search_ ))

    return list(filter( _filter, [ i for i in L ]))

def filter_dir(attr, **kwargs):
    return filterStrings( attr, func = dir, **kwargs )

def moveListItem( L: list, from_index, to_index, *, items = False ):
    assert isinstance( L, list )
    _from = from_index if isinstance( from_index, int ) and not items else L.index(from_index)
    _to = to_index if isinstance( to_index, int ) and not items else L.index(to_index)
    _from = _from if _from >= 0 else len(L) + _from
    _to   = _to if _to >= 0 else len(L) + _to
    if _from == _to:
        return L

    _L = L.copy()
    _L.insert( _to, _L.pop(_from) )
    return _L

def sortDiverseList( L: list|tuple, *, reverse = False, unknowns_last = False ):
    """
    Sorts lists|tuples containing both str and int
        - integers are returned before strings
        - always returns a list object

        Types other than int|float|str are sorted by their '__name__'
      attribute if existing. These will come before the unkown types,
      which will be first in the list, unless 'unknowns_last' is set
      to True, and sorted by their __repr__ value.
    """
    assert isinstance( L, list|tuple )
    def unknown(obj): return bool( not hasattr( obj, '__name__' ) and not isinstance( obj, str|int|float ))

    R = [ sorted(filter( unknown, L ), key = lambda x: repr(x) ),
          sorted(filter( lambda x: isinstance( x, int|float ), L )),
          sorted(filter( lambda x: isinstance( x, str ), L )),
          sorted(filter( lambda x: hasattr( x, '__name__' ), L ))]

    if unknowns_last:
        R = moveListItem( R, 0, 3 )

    return listFlatten(R)

def listDepth( L: list, *, tuples = False ):
    _ins = list|tuple if tuples else list
    D = 0
    while any( isinstance( i, _ins ) for i in L ):
        D += 1
        L = listFlatten( L, tuples = tuples )
    return D

def listFlatten( *L, depth: int = 1, tuples = False ):
    _ins = list|tuple if tuples else list
    if not all( isinstance( i, _ins ) for i in L ):
        raise TypeError(f"Can only include type(s) '{_ins}'")

    def flatten(l): return [ i for item in [ _i if isinstance( _i, _ins ) else [_i] for _i in l ] for i in item ]

    if depth < 0:
        depth = 99999999
    elif depth == 0:
        if len(L) > 1:
            return list(L)
        return list(L[0])

    D = 0
    if not L:
        return []
    elif len(L) == 1:
        L = L[0]
    else:
        L = flatten(L)
        D += 1

    while any( isinstance( _i, _ins ) for _i in L ) and D < depth:
        L = flatten(L)
        D += 1

    return L

def timeDeltaString(t):
    """
    Convert time from timedelta object to xx:xx:xx
    """
    from datetime import timedelta
    assert isinstance( t, timedelta )
    hrs = 0
    mins = 0
    secs = int(round( t.total_seconds(), 0 ))

    if secs >= 60:
        mins = int(secs/60)
        secs = secs % 60
        if mins >= 60:
            hrs = int(mins/60)
            mins = mins % 60

    return f"{hrs}:{mins}:{secs}"

__all__ = [ 'appendFile',
            'attribNameFromString',
            'filterList',
            'filter_dir',
            'findProjectName',
            'getBoolFromString',
            'getIndexed',
            'isBinary',
            'isSafeAttribName',
            'listDepth',
            'listFlatten',
            'matchSimilar',
            'mkData',
            'moveListItem',
            'parseDate',
            'readFile',
            'sortDiverseList',
            'stringFilter',
            'tupleCalc',
            'uniqueName',
            'timeDeltaString',
            'writeFile',
            ]


