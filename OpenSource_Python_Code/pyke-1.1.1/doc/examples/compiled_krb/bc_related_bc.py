# bc_related_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def direct_father_son(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family2', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_related.direct_father_son: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def grand_father_son(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'father_son', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_related.grand_father_son: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'father_son', context,
                              (rule.pattern(3),
                               rule.pattern(0),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_related.grand_father_son: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_grand_father_son(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'father_son', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_related.great_grand_father_son: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'father_son', context,
                              (rule.pattern(3),
                               rule.pattern(0),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_related.great_grand_father_son: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brothers(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'father_son', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_related.brothers: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'father_son', context,
                              (rule.pattern(0),
                               rule.pattern(3),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_related.brothers: got unexpected plan from when clause 2"
                if context.lookup_data('brother1') != context.lookup_data('brother2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def uncle_nephew(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'brothers', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_related.uncle_nephew: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'father_son', context,
                              (rule.pattern(1),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_related.uncle_nephew: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(4).match_data(context, context,
                        ('great',) * len(context.lookup_data('prefix1'))):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cousins(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'uncle_nephew', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_related.cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'father_son', context,
                              (rule.pattern(0),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_related.cousins: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(5).match_data(context, context,
                        min(len(context.lookup_data('prefixes1')), len(context.lookup_data('prefixes2'))) + 1):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(6).match_data(context, context,
                          abs(len(context.lookup_data('prefixes1')) - len(context.lookup_data('prefixes2')))):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_related')
  
  bc_rule.bc_rule('direct_father_son', This_rule_base, 'father_son',
                  direct_father_son, None,
                  (contexts.variable('father'),
                   contexts.variable('son'),
                   pattern.pattern_literal(()),),
                  (),
                  (contexts.variable('son'),
                   contexts.variable('father'),))
  
  bc_rule.bc_rule('grand_father_son', This_rule_base, 'father_son',
                  grand_father_son, None,
                  (contexts.variable('grand_father'),
                   contexts.variable('grand_son'),
                   pattern.pattern_literal(('grand',)),),
                  (),
                  (contexts.variable('father'),
                   contexts.variable('grand_son'),
                   pattern.pattern_literal(()),
                   contexts.variable('grand_father'),))
  
  bc_rule.bc_rule('great_grand_father_son', This_rule_base, 'father_son',
                  great_grand_father_son, None,
                  (contexts.variable('gg_father'),
                   contexts.variable('gg_son'),
                   pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('prefix1'),), contexts.variable('rest_prefixes')),),
                  (),
                  (contexts.variable('father'),
                   contexts.variable('gg_son'),
                   pattern.pattern_literal(()),
                   contexts.variable('gg_father'),
                   pattern.pattern_tuple((contexts.variable('prefix1'),), contexts.variable('rest_prefixes')),))
  
  bc_rule.bc_rule('brothers', This_rule_base, 'brothers',
                  brothers, None,
                  (contexts.variable('brother1'),
                   contexts.variable('brother2'),),
                  (),
                  (contexts.variable('father'),
                   contexts.variable('brother1'),
                   pattern.pattern_literal(()),
                   contexts.variable('brother2'),))
  
  bc_rule.bc_rule('uncle_nephew', This_rule_base, 'uncle_nephew',
                  uncle_nephew, None,
                  (contexts.variable('uncle'),
                   contexts.variable('nephew'),
                   contexts.variable('prefix'),),
                  (),
                  (contexts.variable('uncle'),
                   contexts.variable('father'),
                   contexts.variable('nephew'),
                   contexts.variable('prefix1'),
                   contexts.variable('prefix'),))
  
  bc_rule.bc_rule('cousins', This_rule_base, 'cousins',
                  cousins, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('distance'),
                   contexts.variable('removed'),),
                  (),
                  (contexts.variable('uncle'),
                   contexts.variable('cousin1'),
                   contexts.variable('prefix1'),
                   contexts.variable('cousin2'),
                   contexts.variable('prefix2'),
                   contexts.variable('distance'),
                   contexts.variable('removed'),))


Krb_filename = '../bc_related.krb'
Krb_lineno_map = (
    ((16, 20), (24, 24)),
    ((22, 28), (26, 26)),
    ((41, 45), (29, 29)),
    ((47, 54), (31, 31)),
    ((55, 62), (32, 32)),
    ((75, 79), (35, 35)),
    ((81, 88), (37, 37)),
    ((89, 96), (38, 38)),
    ((109, 113), (41, 41)),
    ((115, 122), (43, 43)),
    ((123, 130), (44, 44)),
    ((131, 131), (45, 45)),
    ((144, 148), (48, 48)),
    ((150, 156), (50, 50)),
    ((157, 164), (51, 51)),
    ((167, 167), (52, 52)),
    ((183, 187), (55, 55)),
    ((189, 196), (57, 57)),
    ((197, 204), (58, 58)),
    ((207, 207), (59, 59)),
    ((211, 211), (60, 60)),
)
