# web_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from web_framework.compiled_krb import web_plans

def process_retrieval(rule, arg_patterns, arg_context):
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
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'format_retrieval', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is not None, \
              "web.process_retrieval: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(3).match_data(context, context, x_1):
              raise AssertionError("web.process_retrieval: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            flag_2 = False
            with engine.prove('database', 'get_data', context,
                              (rule.pattern(0),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is not None, \
                  "web.process_retrieval: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(4).match_data(context, context, x_2):
                  raise AssertionError("web.process_retrieval: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
            if not flag_2:
              raise AssertionError("web.process_retrieval: 'when' clause 2 failed")
            context.undo_to_mark(mark1)
        if not flag_1:
          raise AssertionError("web.process_retrieval: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def format_retrieval(rule, arg_patterns, arg_context):
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
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                get_template(context.lookup_data('template_name'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  structure(context.lookup_data('template'))):
            context.end_save_all_undo()
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'render_elements', context,
                              (rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is not None, \
                  "web.format_retrieval: expected plan from when clause 3"
                mark3 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_3):
                  raise AssertionError("web.format_retrieval: plan match to $render_fn failed in when clause 3")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark3)
            if not flag_3:
              raise AssertionError("web.format_retrieval: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def render_elements(rule, arg_patterns, arg_context):
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
        needed_data = []
        render_fns = []
        forall116_worked = True
        for python_ans in \
             context.lookup_data('elements'):
          mark3 = context.mark(True)
          if rule.pattern(0).match_data(context, context, python_ans):
            context.end_save_all_undo()
            forall116_worked = False
            with engine.prove(rule.rule_base.root_name, 'render_element1', context,
                              (rule.pattern(0),
                               rule.pattern(1),)) \
              as gen_4:
              for x_4 in gen_4:
                assert x_4 is not None, \
                  "web.render_elements: expected plan from when clause 4"
                mark4 = context.mark(True)
                if not rule.pattern(2).match_data(context, context, x_4):
                  raise AssertionError("web.render_elements: plan match to $render_fn failed in when clause 4")
                context.end_save_all_undo()
                needed_data1 = context.lookup_data('needed_data1')
                if needed_data1 and needed_data1 not in needed_data:
                    needed_data.append(needed_data1)
                render_fns.append(context.lookup_data('render_fn'))
                forall116_worked = True
                context.undo_to_mark(mark4)
                if forall116_worked: break
            if not forall116_worked:
              context.undo_to_mark(mark3)
              break
          else: context.end_save_all_undo()
          context.undo_to_mark(mark3)
        if forall116_worked:
          mark6 = context.mark(True)
          if rule.pattern(3).match_data(context, context,
                  tuple(needed_data)):
            context.end_save_all_undo()
            mark7 = context.mark(True)
            if rule.pattern(4).match_data(context, context,
                    tuple(render_fns)):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield context
            else: context.end_save_all_undo()
            context.undo_to_mark(mark7)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def render_element1_del(rule, arg_patterns, arg_context):
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

def render_element1_sep(rule, arg_patterns, arg_context):
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

def render_element1_con(rule, arg_patterns, arg_context):
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
        if context.lookup_data('name').find('.') == -1:
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "web.render_element1_con: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def render_element1_con_dot(rule, arg_patterns, arg_context):
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
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                context.lookup_data('name').split('.')):
          context.end_save_all_undo()
          if context.lookup_data('index').isdigit():
            with engine.prove('special', 'claim_goal', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "web.render_element1_con_dot: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield context
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def render_element1_rep(rule, arg_patterns, arg_context):
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
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'render_elements', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is not None, \
              "web.render_element1_rep: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(2).match_data(context, context, x_1):
              raise AssertionError("web.render_element1_rep: plan match to $detail_fun failed in when clause 1")
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield context
            context.undo_to_mark(mark1)
        if not flag_1:
          raise AssertionError("web.render_element1_rep: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('web')
  
  bc_rule.bc_rule('process_retrieval', This_rule_base, 'process',
                  process_retrieval, web_plans.process_retrieval,
                  (contexts.variable('starting_tables'),
                   contexts.variable('template_name'),),
                  ('plan#1', 'plan#2',),
                  (contexts.variable('starting_tables'),
                   contexts.variable('template_name'),
                   contexts.variable('needed_data'),
                   contexts.variable('plan#1'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('format_retrieval', This_rule_base, 'format_retrieval',
                  format_retrieval, web_plans.format_retrieval,
                  (contexts.variable('starting_tables'),
                   contexts.variable('template_name'),
                   contexts.variable('needed_data'),),
                  ('template', 'render_fn',),
                  (contexts.variable('template'),
                   contexts.variable('elements'),
                   contexts.variable('needed_data'),
                   contexts.variable('render_fn'),))
  
  bc_rule.bc_rule('render_elements', This_rule_base, 'render_elements',
                  render_elements, web_plans.render_elements,
                  (contexts.variable('elements'),
                   contexts.variable('needed_data'),),
                  ('render_fns',),
                  (contexts.variable('element'),
                   contexts.variable('needed_data1'),
                   contexts.variable('render_fn'),
                   contexts.variable('needed_data'),
                   contexts.variable('render_fns'),))
  
  bc_rule.bc_rule('render_element1_del', This_rule_base, 'render_element1',
                  render_element1_del, web_plans.render_element1_del,
                  (pattern.pattern_tuple((pattern.pattern_literal('del'), contexts.anonymous('_'),), None),
                   pattern.pattern_literal(None),),
                  (),
                  ())
  
  bc_rule.bc_rule('render_element1_sep', This_rule_base, 'render_element1',
                  render_element1_sep, web_plans.render_element1_sep,
                  (pattern.pattern_tuple((pattern.pattern_literal('sep'), contexts.anonymous('_'),), None),
                   pattern.pattern_literal(None),),
                  (),
                  ())
  
  bc_rule.bc_rule('render_element1_con', This_rule_base, 'render_element1',
                  render_element1_con, web_plans.render_element1_con,
                  (pattern.pattern_tuple((pattern.pattern_literal('con'), contexts.variable('name'),), None),
                   contexts.variable('name'),),
                  ('name', 'name',),
                  ())
  
  bc_rule.bc_rule('render_element1_con_dot', This_rule_base, 'render_element1',
                  render_element1_con_dot, web_plans.render_element1_con_dot,
                  (pattern.pattern_tuple((pattern.pattern_literal('con'), contexts.variable('name'),), None),
                   contexts.variable('real_name'),),
                  ('name', 'real_name',),
                  (pattern.pattern_tuple((contexts.variable('real_name'), contexts.variable('index'),), None),))
  
  bc_rule.bc_rule('render_element1_rep', This_rule_base, 'render_element1',
                  render_element1_rep, web_plans.render_element1_rep,
                  (pattern.pattern_tuple((pattern.pattern_literal('rep'), contexts.variable('name'),), contexts.variable('children')),
                   pattern.pattern_tuple((contexts.variable('name'), pattern.pattern_literal(()),), contexts.variable('child_data')),),
                  ('name', 'detail_fun', 'name',),
                  (contexts.variable('children'),
                   contexts.variable('child_data'),
                   contexts.variable('detail_fun'),))

import sys
import StringIO
import HTMLTemplate
def renderFun(template, render_fn, data):
    render_fn(template, data)
def get_template(template_name):
    f = open(template_name)
    try:
        return HTMLTemplate.Template(renderFun, f.read())
    finally:
        f.close()
def structure(template):
    try:
        stderr_save = sys.stderr
        sys.stderr = StringIO.StringIO()
        template.structure()
        lines = sys.stderr.getvalue().split('\n')
    finally:
        sys.stderr.close()
        sys.stderr = stderr_save
    return get_info(lines, '\t')[1]
def get_info(lines, prefix, start = 0):
    '''
            Returns next_index, structure.
        '''
    ans = []
    while start < len(lines):
        line = lines[start]
        if line and not line.startswith('---') and line != 'tem:':
            if not line.startswith(prefix): break
            if len(line) > len(prefix) and line[len(prefix)] == '\t':
                start, children = get_info(lines, prefix + '\t', start)
                ans[-1] = tuple(ans[-1]) + children
                continue
            else:
                ans.append(tuple(line.strip().split(':')))
        start += 1
    return start, tuple(ans)

Krb_filename = '../web.krb'
Krb_lineno_map = (
    ((17, 21), (47, 47)),
    ((24, 36), (50, 50)),
    ((38, 49), (53, 53)),
    ((68, 72), (81, 81)),
    ((76, 76), (84, 84)),
    ((80, 80), (85, 85)),
    ((83, 94), (86, 86)),
    ((114, 118), (111, 111)),
    ((120, 120), (114, 114)),
    ((121, 121), (115, 115)),
    ((124, 124), (117, 117)),
    ((129, 139), (119, 119)),
    ((140, 143), (120, 124)),
    ((155, 155), (125, 125)),
    ((159, 159), (126, 126)),
    ((177, 181), (154, 154)),
    ((195, 199), (160, 160)),
    ((213, 217), (166, 166)),
    ((219, 219), (169, 169)),
    ((220, 225), (170, 170)),
    ((238, 242), (175, 175)),
    ((246, 246), (178, 178)),
    ((248, 248), (179, 179)),
    ((249, 254), (180, 180)),
    ((269, 273), (185, 185)),
    ((276, 287), (188, 188)),
)
