import re

def returnNextState(token):
  state = "q0"

  transitions = {
    ('q0', re.compile(r'^[a-zA-Z]+$')): 'q1',
    ('q1', re.compile(r'^[a-zA-Z0-9]+$')): 'q1',
    ('q0', re.compile(r'^[0-9]+$')): 'q3',
    ('q3', re.compile(r'^[0-9]+$')): 'q3',
    ('q3', re.compile(r'^[^0-9\.]+$')): 'q4',
    ('q3', re.compile(r'^\.$')): 'q5',
    ('q5', re.compile(r'^[0-9]+$')): 'q6',
    ('q6', re.compile(r'^[0-9]+$')): 'q6',
    ('q0', re.compile(r'^\"$')): 'q8',
    ('q8', re.compile(r'^[^\"]+$')): 'q8',
    ('q8', re.compile(r'^\"$')): 'q9',
    ('q8', re.compile(r'^\\n$')): 'q42',
    ('q0', re.compile(r'^\/$')): 'q10',
    ('q10', re.compile(r'^\/$')): 'q11',
    ('q11', re.compile(r'^[^\/]+$')): 'q11',
    ('q11', re.compile(r'^\\n$')): 'q12',
    ('q10', re.compile(r'^[^\.]+$')): 'q13',
    ('q0', re.compile(r'^\+$')): 'q14',
    ('q0', re.compile(r'^\-$')): 'q15',
    ('q0', re.compile(r'^\*$')): 'q16',
    ('q0', re.compile(r'^\%$')): 'q17',
    ('q0', re.compile(r'^\=$')): 'q18',
    ('q18', re.compile(r'^\=$')): 'q19',
    ('q18', re.compile(r'^[^\=]$')): 'q20',
    ('q0', re.compile(r'^\!$')): 'q21',
    ('q21', re.compile(r'^\=$')): 'q22',
    ('q21', re.compile(r'^[^\!]$')): 'q23',
    ('q0', re.compile(r'^\<$')): 'q24',
    ('q24', re.compile(r'^\=$')): 'q25',
    ('q24', re.compile(r'^[^\<]$')): 'q26',
    ('q0', re.compile(r'^\>$')): 'q27',
    ('q27', re.compile(r'^\=$')): 'q28',
    ('q27', re.compile(r'^[^\>]$')): 'q29',
    ('q0', re.compile(r'^\|$')): 'q30',
    ('q30', re.compile(r'^\|$')): 'q31',
    ('q0', re.compile(r'^\&$')): 'q32',
    ('q32', re.compile(r'^\&$')): 'q33',
    ('q0', re.compile(r'^\,$')): 'q34',
    ('q0', re.compile(r'^\;$')): 'q35',
    ('q0', re.compile(r'^\($')): 'q36',
    ('q0', re.compile(r'^\)$')): 'q37',
    ('q0', re.compile(r'^\[$')): 'q38',
    ('q0', re.compile(r'^\]$')): 'q39',
    ('q0', re.compile(r'^\{$')): 'q40',
    ('q0', re.compile(r'^\}$')): 'q41',
  }

  finish_states = {
    'q1': 'ID',
    'q3': 'NUMINT',
    'q6': 'NUMDEC',
    'q9': 'TEXT',
    'q42': 'ERROR',
    'q12': 'COMMENT',
    'q13': '/',
    'q14': '+',
    'q15': '-',
    'q16': '*',
    'q17': '%',
    'q19': '==',
    'q20': '=',
    'q22': '!=',
    'q23': '!',
    'q25': '>=',
    'q26': '>',
    'q28': '<=',
    'q29': '<',
    'q31': '||',
    'q33': '&&',
    'q34': ',',
    'q35': ';',
    'q36': '(',
    'q37': ')',
    'q38': '[',
    'q39': ']',
    'q40': '{',
    'q41': '}'
  }

  for char in token:
    for (current_state, regex_pattern), next_state in transitions.items():
      if state == current_state and regex_pattern.match(str(char)):
        state = next_state
      
  if state in finish_states:
    if finish_states[state] != "ERROR":
      return finish_states[state]
    else:
      return False
  else:
    return False