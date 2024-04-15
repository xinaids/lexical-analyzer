import re

def returnNextState(state, text):

  transitions = {
    ('q0', re.compile(r'^[a-zA-Z]+$')): 'q1',
    ('q1', re.compile(r'^[a-zA-Z0-9]+$')): 'q1',
    ('q1', re.compile(r'^$')): 'q2',
    ('q0', re.compile(r'^[0-9]+$')): 'q3',
    ('q3', re.compile(r'^[0-9]+$')): 'q3',
    ('q3', re.compile(r'^$')): 'q4',
    ('q3', re.compile(r'^[0-9]+$')): 'q4',
    ('q3', re.compile(r'^\.$')): 'q5',
    ('q5', re.compile(r'^[0-9]+$')): 'q6',
    ('q6', re.compile(r'^[0-9]+$')): 'q6',
    ('q6', re.compile(r'^$')): 'q7',
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

  for (current_state, regex_pattern), next_state in transitions.items():
    if state == current_state and regex_pattern.match(str(text)):
        return next_state

  return None