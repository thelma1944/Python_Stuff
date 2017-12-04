# plan_example_plans.py

pyke_version = '1.1.1'
compiler_version = 1

def transfer1(context, amount):
  (context['plan#1'])(amount)
  (context['plan#2'])(amount)

def transfer2(context, amount):
  (context['plan#1'])(amount)

def withdraw(context, amount):
  print "withdraw", amount, "from", (context['who']), (context['acct_type'])

def deposit(context, amount):
  print "deposit", amount, "to", (context['who']), (context['acct_type'])

def transfer_ach1(context, amount):
  (context['plan#1'])(amount)
  (context['plan#2'])(amount)
  print "send", amount, "to bank", (context['bank']), "acct", (context['who']), (context['acct_type'])

def transfer_ach2(context, amount):
  (context['plan#1'])(amount)
  (context['plan#2'])(amount)
  (context['plan#3'])(amount)

def get_ach(context, amount):
  print "get", amount, "from bank", (context['bank']), "acct", (context['who']), (context['acct_type'])


Krb_filename = '../plan_example.krb'
