# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('Test.CanNotProve', '', 'rules.krb'):
           [1388951653.570782, 'rules_bc.py'],
         ('Test.CanNotProve', '', 'facts.kfb'):
           [1388951653.613548, 'facts.fbc'],
        },
        compiler_version)

