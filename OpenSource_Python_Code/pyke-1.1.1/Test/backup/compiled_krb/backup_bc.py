# backup_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def top_a(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'a', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "backup.top_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def top_b(rule, arg_patterns, arg_context):
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
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def a(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'c', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "backup.a: got unexpected plan from when clause 1"
            with engine.prove('special', 'claim_goal', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "backup.a: got unexpected plan from when clause 2"
                if False:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def c(rule, arg_patterns, arg_context):
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
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('backup')
  
  bc_rule.bc_rule('top_a', This_rule_base, 'top',
                  top_a, None,
                  (contexts.variable('a'),),
                  (),
                  (contexts.variable('a'),))
  
  bc_rule.bc_rule('top_b', This_rule_base, 'top',
                  top_b, None,
                  (contexts.anonymous('_'),),
                  (),
                  ())
  
  bc_rule.bc_rule('a', This_rule_base, 'a',
                  a, None,
                  (contexts.variable('a'),),
                  (),
                  (contexts.variable('a'),))
  
  bc_rule.bc_rule('c', This_rule_base, 'c',
                  c, None,
                  (pattern.pattern_literal(44),),
                  (),
                  ())


Krb_filename = '../backup.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 27), (6, 6)),
    ((40, 44), (9, 9)),
    ((58, 62), (13, 13)),
    ((64, 69), (15, 15)),
    ((70, 75), (16, 16)),
    ((76, 76), (17, 17)),
    ((89, 93), (21, 21)),
)
