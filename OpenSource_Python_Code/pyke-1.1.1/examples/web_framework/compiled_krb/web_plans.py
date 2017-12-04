# web_plans.py

pyke_version = '1.1.1'
compiler_version = 1

def process_retrieval(context, db_connection, db_cursor, starting_keys):
  data = (context['plan#2'])(db_cursor, starting_keys)
  return (context['plan#1'])(db_connection, data)

def format_retrieval(context, db_connection, data):
  db_connection.commit()
  return '200 OK', [('Content-Type', 'text/html')], \
                 ((context['template']).render((context['render_fn']), data),)

def render_elements(context, template, data):
  for render_fn in (context['render_fns']): render_fn(template, data)

def render_element1_del(context, template, data):
  pass

def render_element1_sep(context, template, data):
  pass

def render_element1_con(context, template, data):
  getattr(template, (context['name'])).content = str(data[(context['name'])])

def render_element1_con_dot(context, template, data):
  getattr(template, (context['name'])).content = str(data[(context['real_name'])])

def render_element1_rep(context, template, data):
  getattr(template, (context['name'])).repeat((context['detail_fun']), data[(context['name'])])


Krb_filename = '../web.krb'
