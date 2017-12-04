# fc_findall_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def collect_siblings(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        siblings = []
        with engine.lookup('family', 'child_of', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('sibling') != context.lookup_data('child'):
              siblings.append(context.lookup_data('sibling'))
        mark5 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                tuple(siblings)):
          context.end_save_all_undo()
          engine.assert_('family', 'siblings_of',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark5)
  finally:
    context.done()

def collect_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cousins = []
        with engine.lookup('family', 'siblings_of', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            for python_ans in \
                 context.lookup_data('father_siblings'):
              mark3 = context.mark(True)
              if rule.pattern(0).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.lookup('family', 'child_of', context, \
                                   rule.foreach_patterns(2)) \
                  as gen_2:
                  for dummy in gen_2:
                    cousins.append(context.lookup_data('cousin'))
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            for python_ans in \
                 context.lookup_data('father_siblings'):
              mark6 = context.mark(True)
              if rule.pattern(0).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.lookup('family', 'child_of', context, \
                                   rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    cousins.append(context.lookup_data('cousin'))
              else: context.end_save_all_undo()
              context.undo_to_mark(mark6)
        with engine.lookup('family', 'siblings_of', context, \
                           rule.foreach_patterns(4)) \
          as gen_4:
          for dummy in gen_4:
            for python_ans in \
                 context.lookup_data('mother_siblings'):
              mark10 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.lookup('family', 'child_of', context, \
                                   rule.foreach_patterns(5)) \
                  as gen_5:
                  for dummy in gen_5:
                    cousins.append(context.lookup_data('cousin'))
              else: context.end_save_all_undo()
              context.undo_to_mark(mark10)
            for python_ans in \
                 context.lookup_data('mother_siblings'):
              mark13 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.lookup('family', 'child_of', context, \
                                   rule.foreach_patterns(6)) \
                  as gen_6:
                  for dummy in gen_6:
                    cousins.append(context.lookup_data('cousin'))
              else: context.end_save_all_undo()
              context.undo_to_mark(mark13)
        mark16 = context.mark(True)
        if rule.pattern(2).match_data(context, context,
                tuple(cousins)):
          context.end_save_all_undo()
          print "%s has %s as cousins" % (context.lookup_data('child'), context.lookup_data('cousins'))
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark16)
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_findall')
  
  fc_rule.fc_rule('collect_siblings', This_rule_base, collect_siblings,
    (('family', 'child_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'child_of',
      (contexts.variable('sibling'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      True),),
    (contexts.variable('siblings'),
     contexts.variable('child'),))
  
  fc_rule.fc_rule('collect_cousins', This_rule_base, collect_cousins,
    (('family', 'child_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'siblings_of',
      (contexts.variable('father'),
       contexts.variable('father_siblings'),),
      True),
     ('family', 'child_of',
      (contexts.variable('cousin'),
       contexts.variable('father_sibling'),
       contexts.anonymous('_'),),
      True),
     ('family', 'child_of',
      (contexts.variable('cousin'),
       contexts.anonymous('_'),
       contexts.variable('father_sibling'),),
      True),
     ('family', 'siblings_of',
      (contexts.variable('mother'),
       contexts.variable('mother_siblings'),),
      True),
     ('family', 'child_of',
      (contexts.variable('cousin'),
       contexts.anonymous('_'),
       contexts.variable('mother_sibling'),),
      True),
     ('family', 'child_of',
      (contexts.variable('cousin'),
       contexts.variable('mother_sibling'),
       contexts.anonymous('_'),),
      True),),
    (contexts.variable('father_sibling'),
     contexts.variable('mother_sibling'),
     contexts.variable('cousins'),))


Krb_filename = '../fc_findall.krb'
Krb_lineno_map = (
    ((13, 17), (5, 5)),
    ((18, 18), (6, 6)),
    ((19, 22), (8, 8)),
    ((23, 23), (9, 9)),
    ((24, 24), (10, 10)),
    ((27, 27), (11, 11)),
    ((29, 31), (13, 13)),
    ((42, 46), (17, 17)),
    ((47, 47), (19, 19)),
    ((48, 51), (21, 21)),
    ((53, 53), (23, 23)),
    ((57, 60), (24, 24)),
    ((61, 61), (25, 25)),
    ((65, 65), (28, 28)),
    ((69, 72), (29, 29)),
    ((73, 73), (30, 30)),
    ((76, 79), (33, 33)),
    ((81, 81), (35, 35)),
    ((85, 88), (36, 36)),
    ((89, 89), (37, 37)),
    ((93, 93), (40, 40)),
    ((97, 100), (41, 41)),
    ((101, 101), (42, 42)),
    ((106, 106), (44, 44)),
    ((108, 108), (46, 46)),
)
