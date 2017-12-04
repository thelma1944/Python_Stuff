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
         ('', '', 'bc_notany.krb'):
           [1388951688.792042, 'bc_notany_bc.py'],
         ('', '', 'family.kfb'):
           [1388951688.799718, 'family.fbc'],
         ('', '', 'fc_notany.krb'):
           [1388951688.888896, 'fc_notany_fc.py'],
        },
        compiler_version)

