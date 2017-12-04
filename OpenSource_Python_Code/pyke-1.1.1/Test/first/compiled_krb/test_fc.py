# test_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def test1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        first1_worked = False
        with engine.lookup('family', 'son_of', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('child') != context.lookup_data('brother'):
              first1_worked = True
              engine.assert_('family', 'brothers',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
            if first1_worked: break
  finally:
    context.done()

def test2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    first0_worked = False
    with engine.lookup('family', 'cousins', context, \
                       rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        first0_worked = True
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'nephew_of',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
        if first0_worked: break
  finally:
    context.done()

def test3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'brothers', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        first1_worked = False
        with engine.lookup('family', 'son_of', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            first1_worked = True
            first2_worked = False
            with engine.lookup('family', 'son_of', context, \
                               rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                first2_worked = True
                engine.assert_('family', 'cousins',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
                if first2_worked: break
            if first1_worked: break
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('test')
  
  fc_rule.fc_rule('test1', This_rule_base, test1,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      True),),
    (contexts.variable('child'),
     contexts.variable('brother'),))
  
  fc_rule.fc_rule('test2', This_rule_base, test2,
    (('family', 'cousins',
      (contexts.variable('a'),
       contexts.variable('c'),),
      True),
     ('family', 'son_of',
      (contexts.variable('a'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('c'),
     contexts.variable('father'),
     contexts.variable('mother'),))
  
  fc_rule.fc_rule('test3', This_rule_base, test3,
    (('family', 'brothers',
      (contexts.variable('a'),
       contexts.variable('b'),),
      False),
     ('family', 'son_of',
      (contexts.variable('c1'),
       contexts.variable('a'),
       contexts.anonymous('_'),),
      True),
     ('family', 'son_of',
      (contexts.variable('c2'),
       contexts.variable('b'),
       contexts.anonymous('_'),),
      True),),
    (contexts.variable('c1'),
     contexts.variable('c2'),))


Krb_filename = '../test.krb'
Krb_lineno_map = (
    ((13, 17), (5, 5)),
    ((19, 22), (7, 7)),
    ((23, 23), (8, 8)),
    ((25, 27), (10, 10)),
    ((38, 41), (15, 15)),
    ((43, 47), (16, 16)),
    ((48, 51), (18, 18)),
    ((61, 65), (22, 22)),
    ((67, 70), (24, 24)),
    ((73, 76), (26, 26)),
    ((78, 80), (28, 28)),
)
