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
         ('', '', 'family.kfb'):
           [1388951737.665984, 'family.fbc'],
         ('', '', 'example.krb'):
           [1388951737.895832, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'bc2_example.krb'):
           [1388951738.125578, 'bc2_example_bc.py'],
         ('', '', 'bc_example.krb'):
           [1388951738.308738, 'bc_example_bc.py'],
         ('', '', 'fc_example.krb'):
           [1388951738.466329, 'fc_example_fc.py'],
        },
        compiler_version)

