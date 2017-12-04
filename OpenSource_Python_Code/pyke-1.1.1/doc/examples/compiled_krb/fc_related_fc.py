# fc_related_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def direct_father_son(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family1', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family1', 'father_son',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def grand_father_son(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family1', 'father_son', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family1', 'father_son', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family1', 'father_son',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def great_grand_father_son(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family1', 'father_son', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family1', 'father_son', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family1', 'father_son',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_related')
  
  fc_rule.fc_rule('direct_father_son', This_rule_base, direct_father_son,
    (('family1', 'son_of',
      (contexts.variable('son'),
       contexts.variable('father'),),
      False),),
    (contexts.variable('father'),
     contexts.variable('son'),
     pattern.pattern_literal(()),))
  
  fc_rule.fc_rule('grand_father_son', This_rule_base, grand_father_son,
    (('family1', 'father_son',
      (contexts.variable('father'),
       contexts.variable('grand_son'),
       pattern.pattern_literal(()),),
      False),
     ('family1', 'father_son',
      (contexts.variable('grand_father'),
       contexts.variable('father'),
       pattern.pattern_literal(()),),
      False),),
    (contexts.variable('grand_father'),
     contexts.variable('grand_son'),
     pattern.pattern_literal(('grand',)),))
  
  fc_rule.fc_rule('great_grand_father_son', This_rule_base, great_grand_father_son,
    (('family1', 'father_son',
      (contexts.variable('parent'),
       contexts.variable('gg_child'),
       pattern.pattern_literal(()),),
      False),
     ('family1', 'father_son',
      (contexts.variable('gg_parent'),
       contexts.variable('parent'),
       pattern.pattern_tuple((contexts.variable('prefix1'),), contexts.variable('rest_prefixes')),),
      False),),
    (contexts.variable('gg_parent'),
     contexts.variable('gg_child'),
     pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('prefix1'),), contexts.variable('rest_prefixes')),))


Krb_filename = '../fc_related.krb'
Krb_lineno_map = (
    ((13, 17), (26, 26)),
    ((18, 21), (28, 28)),
    ((30, 34), (32, 32)),
    ((35, 39), (33, 33)),
    ((40, 43), (35, 35)),
    ((52, 56), (39, 39)),
    ((57, 61), (40, 40)),
    ((62, 65), (42, 43)),
)
