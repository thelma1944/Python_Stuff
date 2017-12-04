# plan_example_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from doc.examples.compiled_krb import plan_example_plans

def transfer1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'withdraw', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "plan_example.transfer1: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(1).match_data(context, context, x_1):
              raise AssertionError("plan_example.transfer1: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            with engine.prove(rule.rule_base.root_name, 'deposit', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "plan_example.transfer1: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("plan_example.transfer1: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def transfer2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'transfer_ach', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "plan_example.transfer2: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(2).match_data(context, context, x_1):
              raise AssertionError("plan_example.transfer2: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield context
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def withdraw(rule, arg_patterns, arg_context):
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
        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def deposit(rule, arg_patterns, arg_context):
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
        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def transfer_ach1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'withdraw', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "plan_example.transfer_ach1: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(1).match_data(context, context, x_1):
              raise AssertionError("plan_example.transfer_ach1: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            with engine.prove(rule.rule_base.root_name, 'deposit', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "plan_example.transfer_ach1: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("plan_example.transfer_ach1: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def transfer_ach2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'get_ach', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "plan_example.transfer_ach2: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(1).match_data(context, context, x_1):
              raise AssertionError("plan_example.transfer_ach2: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            with engine.prove(rule.rule_base.root_name, 'withdraw', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "plan_example.transfer_ach2: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("plan_example.transfer_ach2: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                with engine.prove(rule.rule_base.root_name, 'deposit', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is not None, \
                      "plan_example.transfer_ach2: expected plan from when clause 3"
                    mark3 = context.mark(True)
                    if not rule.pattern(5).match_data(context, context, x_3):
                      raise AssertionError("plan_example.transfer_ach2: plan match to $plan#3 failed in when clause 3")
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield context
                    context.undo_to_mark(mark3)
                context.undo_to_mark(mark2)
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_ach(rule, arg_patterns, arg_context):
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
        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('plan_example')
  
  bc_rule.bc_rule('transfer1', This_rule_base, 'transfer',
                  transfer1, plan_example_plans.transfer1,
                  (contexts.variable('from_acct'),
                   contexts.variable('to_acct'),),
                  ('plan#1', 'plan#2',),
                  (contexts.variable('from_acct'),
                   contexts.variable('plan#1'),
                   contexts.variable('to_acct'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('transfer2', This_rule_base, 'transfer',
                  transfer2, plan_example_plans.transfer2,
                  (contexts.variable('from_acct'),
                   contexts.variable('to_acct'),),
                  ('plan#1',),
                  (contexts.variable('from_acct'),
                   contexts.variable('to_acct'),
                   contexts.variable('plan#1'),))
  
  bc_rule.bc_rule('withdraw', This_rule_base, 'withdraw',
                  withdraw, plan_example_plans.withdraw,
                  (pattern.pattern_tuple((contexts.variable('who'), contexts.variable('acct_type'),), None),),
                  ('who', 'acct_type',),
                  ())
  
  bc_rule.bc_rule('deposit', This_rule_base, 'deposit',
                  deposit, plan_example_plans.deposit,
                  (pattern.pattern_tuple((contexts.variable('who'), contexts.variable('acct_type'),), None),),
                  ('who', 'acct_type',),
                  ())
  
  bc_rule.bc_rule('transfer_ach1', This_rule_base, 'transfer_ach',
                  transfer_ach1, plan_example_plans.transfer_ach1,
                  (contexts.variable('from_acct'),
                   pattern.pattern_tuple((contexts.variable('bank'), contexts.variable('who'), contexts.variable('acct_type'),), None),),
                  ('bank', 'who', 'acct_type', 'plan#1', 'plan#2',),
                  (contexts.variable('from_acct'),
                   contexts.variable('plan#1'),
                   pattern.pattern_literal(('central_accts', 'ach_send_acct',)),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('transfer_ach2', This_rule_base, 'transfer_ach',
                  transfer_ach2, plan_example_plans.transfer_ach2,
                  (contexts.variable('from_acct'),
                   contexts.variable('to_acct'),),
                  ('plan#1', 'plan#2', 'plan#3',),
                  (contexts.variable('from_acct'),
                   contexts.variable('plan#1'),
                   pattern.pattern_literal(('central_accts', 'ach_recv_acct',)),
                   contexts.variable('plan#2'),
                   contexts.variable('to_acct'),
                   contexts.variable('plan#3'),))
  
  bc_rule.bc_rule('get_ach', This_rule_base, 'get_ach',
                  get_ach, plan_example_plans.get_ach,
                  (pattern.pattern_tuple((contexts.variable('bank'), contexts.variable('who'), contexts.variable('acct_type'),), None),),
                  ('bank', 'who', 'acct_type',),
                  ())


Krb_filename = '../plan_example.krb'
Krb_lineno_map = (
    ((17, 21), (24, 24)),
    ((23, 32), (26, 26)),
    ((33, 42), (28, 28)),
    ((57, 61), (32, 32)),
    ((63, 73), (34, 34)),
    ((87, 91), (38, 38)),
    ((105, 109), (43, 43)),
    ((123, 127), (48, 48)),
    ((129, 138), (50, 50)),
    ((139, 148), (52, 52)),
    ((163, 167), (58, 58)),
    ((169, 178), (60, 60)),
    ((179, 188), (62, 62)),
    ((189, 198), (64, 64)),
    ((214, 218), (68, 68)),
)
