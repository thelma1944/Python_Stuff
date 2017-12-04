# bc_notany_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.brothers: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.brothers: got unexpected plan from when clause 2"
                if context.lookup_data('brother1') != context.lookup_data('brother2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sisters(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.sisters: got unexpected plan from when clause 1"
            with engine.prove('family', 'daughter_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.sisters: got unexpected plan from when clause 2"
                if context.lookup_data('sister1') != context.lookup_data('sister2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brother_sister(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.brother_sister: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.brother_sister: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sister_brother(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.sister_brother: got unexpected plan from when clause 1"
            with engine.prove('family', 'daughter_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.sister_brother: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_parent(rule, arg_patterns, arg_context):
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
        notany33_worked = True
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.no_parent: got unexpected plan from when clause 1"
            notany33_worked = False
            if not notany33_worked: break
        if notany33_worked:
          notany35_worked = True
          with engine.prove('family', 'son_of', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(1),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc_notany.no_parent: got unexpected plan from when clause 2"
              notany35_worked = False
              if not notany35_worked: break
          if notany35_worked:
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_uncle_1(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.no_uncle_1: got unexpected plan from when clause 1"
            notany42_worked = True
            with engine.prove(rule.rule_base.root_name, 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.no_uncle_1: got unexpected plan from when clause 2"
                if context.lookup_data('gender') == 'brother':
                  notany42_worked = False
                if not notany42_worked: break
            if notany42_worked:
              notany45_worked = True
              with engine.prove(rule.rule_base.root_name, 'siblings', context,
                                (rule.pattern(2),
                                 rule.pattern(6),
                                 rule.pattern(4),
                                 rule.pattern(5),)) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "bc_notany.no_uncle_1: got unexpected plan from when clause 4"
                  if context.lookup_data('gender') == 'brother':
                    notany45_worked = False
                  if not notany45_worked: break
              if notany45_worked:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_uncle_2(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.no_uncle_2: got unexpected plan from when clause 1"
            notany53_worked = True
            with engine.prove(rule.rule_base.root_name, 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.no_uncle_2: got unexpected plan from when clause 2"
                if context.lookup_data('gender') == 'brother':
                  notany53_worked = False
                if not notany53_worked: break
            if notany53_worked:
              notany56_worked = True
              with engine.prove(rule.rule_base.root_name, 'siblings', context,
                                (rule.pattern(2),
                                 rule.pattern(6),
                                 rule.pattern(4),
                                 rule.pattern(5),)) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "bc_notany.no_uncle_2: got unexpected plan from when clause 4"
                  if context.lookup_data('gender') == 'brother':
                    notany56_worked = False
                  if not notany56_worked: break
              if notany56_worked:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_aunt_1(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.no_aunt_1: got unexpected plan from when clause 1"
            notany64_worked = True
            with engine.prove(rule.rule_base.root_name, 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.no_aunt_1: got unexpected plan from when clause 2"
                notany64_worked = False
                if not notany64_worked: break
            if notany64_worked:
              notany66_worked = True
              with engine.prove(rule.rule_base.root_name, 'siblings', context,
                                (rule.pattern(2),
                                 rule.pattern(6),
                                 rule.pattern(4),
                                 rule.pattern(5),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_notany.no_aunt_1: got unexpected plan from when clause 3"
                  notany66_worked = False
                  if not notany66_worked: break
              if notany66_worked:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_aunt_2(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_notany.no_aunt_2: got unexpected plan from when clause 1"
            notany73_worked = True
            with engine.prove(rule.rule_base.root_name, 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_notany.no_aunt_2: got unexpected plan from when clause 2"
                notany73_worked = False
                if not notany73_worked: break
            if notany73_worked:
              notany75_worked = True
              with engine.prove(rule.rule_base.root_name, 'siblings', context,
                                (rule.pattern(2),
                                 rule.pattern(6),
                                 rule.pattern(4),
                                 rule.pattern(5),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc_notany.no_aunt_2: got unexpected plan from when clause 3"
                  notany75_worked = False
                  if not notany75_worked: break
              if notany75_worked:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_notany')
  
  bc_rule.bc_rule('brothers', This_rule_base, 'siblings',
                  brothers, None,
                  (contexts.variable('brother1'),
                   contexts.variable('brother2'),
                   pattern.pattern_literal('brother'),
                   pattern.pattern_literal('brother'),),
                  (),
                  (contexts.variable('brother1'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('brother2'),))
  
  bc_rule.bc_rule('sisters', This_rule_base, 'siblings',
                  sisters, None,
                  (contexts.variable('sister1'),
                   contexts.variable('sister2'),
                   pattern.pattern_literal('sister'),
                   pattern.pattern_literal('sister'),),
                  (),
                  (contexts.variable('sister1'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sister2'),))
  
  bc_rule.bc_rule('brother_sister', This_rule_base, 'siblings',
                  brother_sister, None,
                  (contexts.variable('sister'),
                   contexts.variable('brother'),
                   pattern.pattern_literal('brother'),
                   pattern.pattern_literal('sister'),),
                  (),
                  (contexts.variable('sister'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('brother'),))
  
  bc_rule.bc_rule('sister_brother', This_rule_base, 'siblings',
                  sister_brother, None,
                  (contexts.variable('brother'),
                   contexts.variable('sister'),
                   pattern.pattern_literal('sister'),
                   pattern.pattern_literal('brother'),),
                  (),
                  (contexts.variable('brother'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sister'),))
  
  bc_rule.bc_rule('no_parent', This_rule_base, 'child_with_no_parent',
                  no_parent, None,
                  (contexts.variable('child'),),
                  (),
                  (contexts.variable('child'),
                   contexts.anonymous('_'),))
  
  bc_rule.bc_rule('no_uncle_1', This_rule_base, 'child_with_no_uncle',
                  no_uncle_1, None,
                  (contexts.variable('child'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('uncle1'),
                   contexts.variable('gender'),
                   contexts.anonymous('_'),
                   contexts.variable('uncle2'),))
  
  bc_rule.bc_rule('no_uncle_2', This_rule_base, 'child_with_no_uncle',
                  no_uncle_2, None,
                  (contexts.variable('child'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('uncle1'),
                   contexts.variable('gender'),
                   contexts.anonymous('_'),
                   contexts.variable('uncle2'),))
  
  bc_rule.bc_rule('no_aunt_1', This_rule_base, 'child_with_no_aunt',
                  no_aunt_1, None,
                  (contexts.variable('child'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('aunt1'),
                   pattern.pattern_literal('sister'),
                   contexts.anonymous('_'),
                   contexts.variable('aunt2'),))
  
  bc_rule.bc_rule('no_aunt_2', This_rule_base, 'child_with_no_aunt',
                  no_aunt_2, None,
                  (contexts.variable('child'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('aunt1'),
                   pattern.pattern_literal('sister'),
                   contexts.anonymous('_'),
                   contexts.variable('aunt2'),))


Krb_filename = '../bc_notany.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 29), (6, 6)),
    ((30, 37), (7, 7)),
    ((38, 38), (8, 8)),
    ((51, 55), (11, 11)),
    ((57, 64), (13, 13)),
    ((65, 72), (14, 14)),
    ((73, 73), (15, 15)),
    ((86, 90), (18, 18)),
    ((92, 99), (20, 20)),
    ((100, 107), (21, 21)),
    ((120, 124), (24, 24)),
    ((126, 133), (26, 26)),
    ((134, 141), (27, 27)),
    ((154, 158), (31, 31)),
    ((161, 168), (34, 34)),
    ((173, 180), (36, 36)),
    ((196, 200), (39, 39)),
    ((202, 209), (41, 41)),
    ((211, 219), (43, 43)),
    ((220, 220), (44, 44)),
    ((225, 233), (46, 46)),
    ((234, 234), (47, 47)),
    ((250, 254), (50, 50)),
    ((256, 263), (52, 52)),
    ((265, 273), (54, 54)),
    ((274, 274), (55, 55)),
    ((279, 287), (57, 57)),
    ((288, 288), (58, 58)),
    ((304, 308), (61, 61)),
    ((310, 317), (63, 63)),
    ((319, 327), (65, 65)),
    ((332, 340), (67, 67)),
    ((356, 360), (70, 70)),
    ((362, 369), (72, 72)),
    ((371, 379), (74, 74)),
    ((384, 392), (76, 76)),
)
