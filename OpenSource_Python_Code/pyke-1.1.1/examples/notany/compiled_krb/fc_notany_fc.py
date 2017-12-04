# fc_notany_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def brothers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('brother1') != context.lookup_data('brother2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sisters(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('sister1') != context.lookup_data('sister2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brother_sister(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'siblings',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sister_brother(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'siblings',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_uncle_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany37_worked = True
        with engine.lookup('family', 'siblings', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('gender1') == 'brother':
              notany37_worked = False
            if not notany37_worked: break
        if notany37_worked:
          notany40_worked = True
          with engine.lookup('family', 'siblings', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              if context.lookup_data('gender2') == 'brother':
                notany40_worked = False
              if not notany40_worked: break
          if notany40_worked:
            print context.lookup_data('child'), "has no uncle"
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_uncle_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany49_worked = True
        with engine.lookup('family', 'siblings', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('gender') == 'brother':
              notany49_worked = False
            if not notany49_worked: break
        if notany49_worked:
          notany52_worked = True
          with engine.lookup('family', 'siblings', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              if context.lookup_data('gender') == 'brother':
                notany52_worked = False
              if not notany52_worked: break
          if notany52_worked:
            print context.lookup_data('child'), "has no uncle"
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_aunt_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany61_worked = True
        with engine.lookup('family', 'siblings', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany61_worked = False
            if not notany61_worked: break
        if notany61_worked:
          notany63_worked = True
          with engine.lookup('family', 'siblings', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              notany63_worked = False
              if not notany63_worked: break
          if notany63_worked:
            print context.lookup_data('child'), "has no aunt"
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_aunt_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany71_worked = True
        with engine.lookup('family', 'siblings', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany71_worked = False
            if not notany71_worked: break
        if notany71_worked:
          notany73_worked = True
          with engine.lookup('family', 'siblings', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              notany73_worked = False
              if not notany73_worked: break
          if notany73_worked:
            print context.lookup_data('child'), "has no aunt"
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_notany')
  
  fc_rule.fc_rule('brothers', This_rule_base, brothers,
    (('family', 'son_of',
      (contexts.variable('brother1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother1'),
     contexts.variable('brother2'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('sisters', This_rule_base, sisters,
    (('family', 'daughter_of',
      (contexts.variable('sister1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('sister1'),
     contexts.variable('sister2'),
     pattern.pattern_literal('sister'),))
  
  fc_rule.fc_rule('brother_sister', This_rule_base, brother_sister,
    (('family', 'daughter_of',
      (contexts.variable('sister'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('sister'),
     contexts.variable('brother'),
     pattern.pattern_literal('brother'),
     pattern.pattern_literal('sister'),))
  
  fc_rule.fc_rule('sister_brother', This_rule_base, sister_brother,
    (('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother'),
     contexts.variable('sister'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('no_uncle_1', This_rule_base, no_uncle_1,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'siblings',
      (contexts.variable('father'),
       contexts.variable('uncle1'),
       contexts.variable('gender1'),
       contexts.anonymous('_'),),
      True),
     ('family', 'siblings',
      (contexts.variable('mother'),
       contexts.variable('uncle2'),
       contexts.variable('gender2'),
       contexts.anonymous('_'),),
      True),),
    ())
  
  fc_rule.fc_rule('no_uncle_2', This_rule_base, no_uncle_2,
    (('family', 'daughter_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'siblings',
      (contexts.variable('father'),
       contexts.variable('uncle1'),
       contexts.variable('gender'),
       contexts.anonymous('_'),),
      True),
     ('family', 'siblings',
      (contexts.variable('mother'),
       contexts.variable('uncle2'),
       contexts.variable('gender'),
       contexts.anonymous('_'),),
      True),),
    ())
  
  fc_rule.fc_rule('no_aunt_1', This_rule_base, no_aunt_1,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'siblings',
      (contexts.variable('father'),
       contexts.variable('aunt1'),
       pattern.pattern_literal('sister'),
       contexts.anonymous('_'),),
      True),
     ('family', 'siblings',
      (contexts.variable('mother'),
       contexts.variable('aunt2'),
       pattern.pattern_literal('sister'),
       contexts.anonymous('_'),),
      True),),
    ())
  
  fc_rule.fc_rule('no_aunt_2', This_rule_base, no_aunt_2,
    (('family', 'daughter_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'siblings',
      (contexts.variable('father'),
       contexts.variable('aunt1'),
       pattern.pattern_literal('sister'),
       contexts.anonymous('_'),),
      True),
     ('family', 'siblings',
      (contexts.variable('mother'),
       contexts.variable('aunt2'),
       pattern.pattern_literal('sister'),
       contexts.anonymous('_'),),
      True),),
    ())


Krb_filename = '../fc_notany.krb'
Krb_lineno_map = (
    ((13, 17), (5, 5)),
    ((18, 22), (6, 6)),
    ((23, 23), (7, 7)),
    ((24, 28), (9, 9)),
    ((37, 41), (13, 13)),
    ((42, 46), (14, 14)),
    ((47, 47), (15, 15)),
    ((48, 52), (17, 17)),
    ((61, 65), (21, 21)),
    ((66, 70), (22, 22)),
    ((71, 75), (24, 24)),
    ((84, 88), (28, 28)),
    ((89, 93), (29, 29)),
    ((94, 98), (31, 31)),
    ((107, 111), (36, 36)),
    ((113, 116), (38, 38)),
    ((117, 117), (39, 39)),
    ((122, 125), (41, 41)),
    ((126, 126), (42, 42)),
    ((130, 130), (44, 44)),
    ((139, 143), (48, 48)),
    ((145, 148), (50, 50)),
    ((149, 149), (51, 51)),
    ((154, 157), (53, 53)),
    ((158, 158), (54, 54)),
    ((162, 162), (56, 56)),
    ((171, 175), (60, 60)),
    ((177, 180), (62, 62)),
    ((185, 188), (64, 64)),
    ((192, 192), (66, 66)),
    ((201, 205), (70, 70)),
    ((207, 210), (72, 72)),
    ((215, 218), (74, 74)),
    ((222, 222), (76, 76)),
)
