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
         ('doc.examples', '', 'bc_related0.krb'):
           [1388951699.713373, 'bc_related0_bc.py'],
         ('doc.examples', '', 'family2.kfb'):
           [1388951699.724251, 'family2.fbc'],
         ('doc.examples', '', 'bc_related.krb'):
           [1388951699.77856, 'bc_related_bc.py'],
         ('doc.examples', '', 'plan_example.krb'):
           [1388951699.819822, 'plan_example_plans.py', 'plan_example_bc.py'],
         ('doc.examples', '', 'family1.kfb'):
           [1388951699.822666, 'family1.fbc'],
         ('doc.examples', '', 'user_questions.kqb'):
           [1388951699.849841, 'user_questions.qbc'],
         ('doc.examples', '', 'fc_related.krb'):
           [1388951699.87074, 'fc_related_fc.py'],
         ('doc.examples', '', 'error_test.krb'):
           [1388951699.893737, 'error_test_bc.py'],
        },
        compiler_version)

