# error_test_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def rule1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'goal2', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "error_test.rule1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def rule2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'goal3', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "error_test.rule2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def rule3(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'goal4', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "error_test.rule3: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def rule4(rule, arg_patterns, arg_context):
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
        if context.lookup_data('bar') > 0:
          rule.rule_base.num_bc_rule_successes += 1
          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('error_test')
  
  bc_rule.bc_rule('rule1', This_rule_base, 'goal',
                  rule1, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('rule2', This_rule_base, 'goal2',
                  rule2, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('rule3', This_rule_base, 'goal3',
                  rule3, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('rule4', This_rule_base, 'goal4',
                  rule4, None,
                  (),
                  (),
                  ())


Krb_filename = '../error_test.krb'
Krb_lineno_map = (
    ((16, 20), (24, 24)),
    ((22, 27), (26, 26)),
    ((40, 44), (29, 29)),
    ((46, 51), (31, 31)),
    ((64, 68), (34, 34)),
    ((70, 75), (36, 36)),
    ((88, 92), (39, 39)),
    ((94, 94), (41, 41)),
)
