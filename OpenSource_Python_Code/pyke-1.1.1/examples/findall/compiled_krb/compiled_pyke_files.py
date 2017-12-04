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
         ('', '', 'bc_findall.krb'):
           [1388951686.593617, 'bc_findall_bc.py'],
         ('', '', 'family.kfb'):
           [1388951686.599584, 'family.fbc'],
         ('', '', 'fc_findall.krb'):
           [1388951686.669049, 'fc_findall_fc.py'],
        },
        compiler_version)

