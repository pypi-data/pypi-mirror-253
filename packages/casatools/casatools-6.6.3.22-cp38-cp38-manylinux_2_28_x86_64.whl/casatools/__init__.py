from __future__ import absolute_import
__name__ = 'casatools'
__all__ = [ "ctsys", "version", "version_string"
            'image',
            'logsink',
            'coordsys',
            'synthesisutils',
            'synthesisnormalizer',
            'calanalysis',
            'mstransformer',
            'calibrater',
            'functional',
            'table',
            'measures',
            'imagepol',
            'simulator',
            'sdm',
            'synthesisimstore',
            'miriadfiller',
            'ms',
            'vpmanager',
            'synthesisdeconvolver',
            'vlafiller',
            'sakura',
            'linearmosaic',
            'tablerow',
            'iterbotsink',
            'sidebandseparator',
            'imagemetadata',
            'atcafiller',
            'agentflagger',
            'synthesismaskhandler',
            'regionmanager',
            'msmetadata',
            'imager',
            'singledishms',
            'atmosphere',
            'quanta',
            'synthesisimager',
            'componentlist',
            'spectralline',
          ]
from .image import image
from .logsink import logsink
from .coordsys import coordsys
from .synthesisutils import synthesisutils
from .synthesisnormalizer import synthesisnormalizer
from .calanalysis import calanalysis
from .mstransformer import mstransformer
from .calibrater import calibrater
from .functional import functional
from .table import table
from .measures import measures
from .imagepol import imagepol
from .simulator import simulator
from .sdm import sdm
from .synthesisimstore import synthesisimstore
from .miriadfiller import miriadfiller
from .ms import ms
from .vpmanager import vpmanager
from .synthesisdeconvolver import synthesisdeconvolver
from .vlafiller import vlafiller
from .sakura import sakura
from .linearmosaic import linearmosaic
from .tablerow import tablerow
from .iterbotsink import iterbotsink
from .sidebandseparator import sidebandseparator
from .imagemetadata import imagemetadata
from .atcafiller import atcafiller
from .agentflagger import agentflagger
from .synthesismaskhandler import synthesismaskhandler
from .regionmanager import regionmanager
from .msmetadata import msmetadata
from .imager import imager
from .singledishms import singledishms
from .atmosphere import atmosphere
from .quanta import quanta
from .synthesisimager import synthesisimager
from .componentlist import componentlist
from .spectralline import spectralline
from casatools import ctuser as __user
from .utils import utils as __utils
import os as __os
import sys as __sys

def __find_data_path( ):

    def find_mount_point(path):
        path = __os.path.abspath(path)
        while not __os.path.ismount(path):
            path = __os.path.dirname(path)
        return path

    #potential_data_paths = ['/opt/casa/data', '/home/casa/data/master', '/home/casa/data', '/export/data_1/casa/data']
    potential_data_paths = [ ]
    casadata = [ d for d in (__os.environ['CASADATA'].split(':') if 'CASADATA' in __os.environ else [ ]) if __os.path.isdir(d) ]
    potential = [ d for d in potential_data_paths if __os.path.isdir(d) ]
    potential_local = [ d for d in potential if find_mount_point(d) == '/' ]
    potential_remote = [ d for d in potential if find_mount_point(d) != '/' ]
    used = set( )
    return [ x for x in casadata + potential_local + potential_remote if x not in used and (used.add(x) or True)]

def __find_user_data_path( ):
    def is_iter_container(v):
        try:
            _iter = iter(v)
            return not isinstance(v,str)
        except TypeError:
            return False

    if hasattr(__user,'datapath') and is_iter_container(__user.datapath):
        return list(filter(__os.path.isdir, list(map(__os.path.expanduser,__user.datapath))))
    else:
        return [ ]

def __find_user_nogui( ):
  result = False
  if (hasattr(__user,'nogui') and isinstance(__user.nogui,bool)):
     result = __user.nogui
  return result

def __find_user_agg( ):
  result = False
  if (hasattr(__user,'agg') and isinstance(__user.agg,bool)):
     result = __user.agg
  return result

def __find_user_pipeline( ):
  result = False
  if (hasattr(__user,'pipeline') and isinstance(__user.pipeline,bool)):
     result = __user.pipeline
  return result

sakura( ).initialize_sakura( )    ## sakura requires explicit initialization

ctsys = __utils( )
_distro_dpath = None
_dpath = [ ]

_user_data = None
if hasattr(__user,'rundata'):
     if not __os.path.isdir(__os.path.expanduser(__user.rundata)):
         if __sys.argv[0] != '-m':
             print("ignoring rundata setting (%s) because it is not a directory" % __user.rundata,file=__sys.stderr)
     else:
         _user_data = __os.path.expanduser(__user.rundata)

if _user_data is None:
    try:
        import casashell as __cs
        _user_data = __os.path.expanduser(__os.path.join(__cs._rcdir,'data'))
    except Exception as e:
        _user_data = __os.path.expanduser("~/.casa/data")

if __os.path.isdir(_user_data):
    _dpath = _dpath + [ _user_data ]
    _iers = __os.path.join(_user_data,'geodetic','IERSeop2000')
    if __os.path.isdir(_iers):
        _distro_dpath = _user_data

if _distro_dpath is None:
    try:
        import casadata
        _distro_dpath = casadata.datapath
        _dpath = _dpath + [ _distro_dpath ]
    except: pass

ctsys.initialize( __sys.executable, "" if _distro_dpath is None else _distro_dpath,
                  __find_user_data_path( ) + _dpath,
                  __find_user_nogui( ), __find_user_agg( ), __find_user_pipeline( ) )

if __sys.argv[0] != '-m':
    __resolved_iers = ctsys.resolve('geodetic/IERSeop2000')
    if __resolved_iers == 'geodetic/IERSeop2000':
        raise ImportError('measures data is not available, visit http://go.nrao.edu/casadata-info for more information')
    if len(ctsys.rundata( )) == 0:
        ctsys.setrundata(__resolved_iers[:-21])

from .coercetype import coerce as __coerce

__coerce.set_ctsys(ctsys)         ## used to locate files from a partial path

def version( ): return list(ctsys.toolversion( ))
def version_string( ): return ctsys.toolversion_string( )

import atexit as __atexit
__atexit.register(ctsys.shutdown) ## c++ shutdown
