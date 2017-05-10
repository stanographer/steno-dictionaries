# TODO: Convert illegal characters to UTF8
# TODO: prevent this from happening: {{|-}^}
# TODO: Implement \cxp
# TODO: \cxds can appear in the middle of the translation
# TODO: Deal with things like {,?}
# TODO: What does ^ mean in Eclipse?
# TODO: What does #N mean in Eclipse?
# TODO: convert supported commands from Eclipse (ignore some, refuse to translate others)

from __future__ import print_function

import sys
import re
import copy
import ply.lex as lex
import ply.yacc as yacc
import json
from collections import defaultdict

class CommandToken(object):
    def __init__(self):
        self.control = None
        self.ignore_if_unrecognized = None
        self.param = None

    def __str__(self):
        prefix = '\\*' if self.ignore_if_unrecognized else ''
        param = str(self.param) if self.param else ''
        return prefix + '\\' + self.control + param

# Compute column. 
#     input is the input text string
#     token is a token instance
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

tokens = (
    'CONTROL',
    'TEXT',
)

literals = '{}'

# Not completely correct for RTF but good enough for us.
t_ignore = '\r'

def t_escapedlbrace(t):
    r'\\\{'
    t.type = 'TEXT'
    t.value = '{'
    return t
    
def t_escapedrbrace(t):
    r'\\\}'
    t.type = 'TEXT'
    t.value = '}'
    return t
    
def t_escapedslash(t):
    r'\\\\'
    t.type = 'TEXT'
    t.value = '\\'
    return t

def t_slashtilde(t):
    r'\\~'
    t.type = 'TEXT'
    t.value = ' '
    return t
    
def t_slashdash(t):
    r'\\-'
    t.type = 'TEXT'
    t.value = '-'
    return t
    
def t_slashunderscore(t):
    r'\\_'
    t.type = 'TEXT'
    t.value = '-'
    return t

def t_CONTROL(t):
    r'(?:\\\*)?\\[a-z]+(?:-?[0-9]+)?[ ]?'
    v = CommandToken()
    v.ignore_if_unrecognized = t.value.startswith(r'\*')
    s = t.value.strip('\\* ')
    v.control = re.findall(r'[a-z]+', s)[0]
    p = re.findall(r'-?[0-9]+', s)
    if p:
        v.param = int(p[0])
    else:
        v.param = None
    t.value = v
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_TEXT = r'[^\\\{\}\r\n]+'

def t_error(t):
    column = find_column(t.lexer.data, t)
    sys.stderr.write("Illegal character '%s' on line %d column %d" % 
                     (t.value[0], t.lineno, column))
    sys.exit()

lexer = lex.lex()

def shout_in_the_void(s):
    pass

class State(object):
    def __init__(self):
        self.output = shout_in_the_void
        self.report_control = shout_in_the_void

stack = []

translations = []
current_lhs = []
current_rhs = []
current_unrecognized = set()
current_keywords = set()
prefix_delete_space = False
suffix_delete_space = False
add_glue = False

unrecognized_controls = set()
skipped_translations = []

def process_delete_space():
    global prefix_delete_space
    global suffix_delete_space
    if len(current_rhs) == 0 and not prefix_delete_space:
        prefix_delete_space = True
    else:
        suffix_delete_space = True
    current_keywords.add('attach')

def glue():
    global add_glue
    add_glue = True
    current_keywords.add('glue')

def finish_translation():
    global prefix_delete_space
    global suffix_delete_space
    global add_glue

    if len(current_lhs) == 0:
        return
    lhs = ''.join(current_lhs)
    rhs = ''.join(current_rhs)
    
    if current_unrecognized:
        exp = ('because it contained unrecognized commands: ' + 
               ', '.join(current_unrecognized))
        skipped_translations.append((lhs, rhs, exp))
        unrecognized_controls.update(current_unrecognized)
    elif any((ord(c) > 0b01111111 for c in lhs + rhs)):
        exp = 'because it contained illegal characters'
        skipped_translations.append((lhs, rhs, exp))
    else:
        if prefix_delete_space or suffix_delete_space:
            split = rhs.split(' ')
            if len(split) == 1:
                # TODO: Make sure this is correct.
                if len(split[0]) == 0:
                    suffix_delete_space = True
                pa = '^' if prefix_delete_space else ''
                ps = '^' if suffix_delete_space else ''
                split[0] = '{' + pa + split[0] + ps + '}'
            else:
                if prefix_delete_space:
                    split[0] = '{^' + split[0] + '}'
                if suffix_delete_space:
                    split[-1] = '{' + split[-1] + '^}'
            rhs = ' '.join(split)
        if add_glue:
            rhs = '{&' + rhs + '}'
        translations.append((lhs, rhs, set(current_keywords)))
        
    del current_rhs[:]
    del current_lhs[:]
    current_unrecognized.clear()
    prefix_delete_space = False
    suffix_delete_space = False
    add_glue = False
    current_keywords.clear()

def output_to_lhs(s):
    current_lhs.append(s)

def output_to_rhs(s):
    old = s
    new = re.sub(r'([ ]{2,})', r' {^\1^} ', old)
    if old != new:
        current_keywords.add('whitespace')
    current_rhs.append(new)

def report_unrecognized_control_in_translation(s):
    current_unrecognized.add(s)    

# TODO: Add support to plover for force lower case
ignore_controls = set(('s', 'cxa', 'cxsgsuf', 'cxsgpre', 'cxfl'))

def p_group(p):
    '''group : '{' push sequence '}'
    '''
    stack.pop()

def p_push(p):
    '''push : '''
    if stack:
        new_state = copy.deepcopy(stack[-1])
    else:
        new_state = State()
    stack.append(new_state)

def p_sequence(p):
    '''sequence : sequence element
                | element
       element : control
               | text
               | group
    '''
    pass

def p_control(p):
    '''control : CONTROL'''
    if p[1].control == 'cxs':
        finish_translation()
        
        stack[-1].output = output_to_lhs
        stack[-2].output = output_to_rhs
        stack[-2].report_control = report_unrecognized_control_in_translation
    elif p[1].control == 'cxds':
        process_delete_space()
    elif p[1].control == 'cxfc':
        stack[-1].output(' {-|}')
    elif p[1].control == 'cxfing':
        glue()
    elif p[1].control == 'cxconf':
        stack[-1].output = shout_in_the_void
    elif p[1].control == 'cxc':
        global current_lhs
        lhs = current_lhs[:]
        if current_rhs:
            print('conflict output', current_lhs, current_rhs, file=sys.stderr)
            finish_translation()
        current_lhs = lhs
        stack[-1].output = output_to_rhs
        stack[-1].report_control = report_unrecognized_control_in_translation
    elif p[1].control in ignore_controls:
        pass
    elif p[1].ignore_if_unrecognized:
        stack[-1].output = shout_in_the_void
    else:
        stack[-1].output(str(p[1]))
        stack[-1].report_control(p[1].control)

def p_text(p):
    '''text : TEXT
    '''
    stack[-1].output(p[1])

def p_error(p):
    sys.stderr.write("Syntax error in input!" + str(p) + '\n')
    sys.exit()
    
parser = yacc.yacc()

data = open(sys.argv[1]).read()
lexer.data = data  # lexer error handling depends on this
parser.parse(data, lexer=lexer)

finish_translation() # This must be called after parsing is done.

dash_chars = set(('-', 'A', 'E', 'O', 'U', '*'))
def normalize_steno(strokes_string):
    strokes = strokes_string.split('/')
    normalized = []
    for s in strokes:
        if '#' in s:
            s = s.replace('#', '')
            if not re.search('[0-9]', s):
                s = '#' + s
    
        seen_dash = False
        l1 = [c for c in s]
        l2 = []
        for c in l1:
            if c == '-':
                if seen_dash:
                    continue
            if c in dash_chars:
                seen_dash = True
            l2.append(c)
        normalized.append(''.join(l2))
    return '/'.join(normalized)

keyword_index = defaultdict(list)

multiple_transformations = []

d = {}
conflicts = defaultdict(set)
for k, v, keywords in translations:
    k = normalize_steno(k)
    if k in d and d[k] != v:
        conflicts[k].add(d[k])
    d[k] = v
    for keyword in keywords:
        keyword_index[keyword].append((k, v))
    if len(keywords) > 1:
        multiple_transformations.append((k, v))

# Time for the report.
original_entries = len(translations) + len(skipped_translations)
duplicates = len(translations) - len(d)

print('Original dictionary entries:', original_entries, file=sys.stderr)
if duplicates:
    print('Duplicates in original dictionary:', duplicates, file=sys.stderr)
if len(conflicts):
    print('Conflicts in original dictionary:', len(conflicts), file=sys.stderr)
    for k, l in conflicts.items():
        print(' ', k, 'maps to', d[k], 'but also mapped to:', ', '.join(l), file=sys.stderr)
if len(skipped_translations):
    print('Skipped translations:', len(skipped_translations), file=sys.stderr)
    for lhs, rhs, exp in skipped_translations:
        print('  Skipped', '\'' + lhs + '\'', '->', '\'' + rhs + '\'', exp, file=sys.stderr)
if unrecognized_controls:
    print('unrecognized controls in dictionary:', ', '.join(unrecognized_controls), file=sys.stderr)
if len(keyword_index):
    print('Some translations had to be converted.', file=sys.stderr)
    if len(multiple_transformations):
        print('The following translations went through multiple transformations. Please test them.', file=sys.stderr)
        for k, v in multiple_transformations:
            print(' ', k, '->', v, file=sys.stderr)
        print('', file=sys.stderr)
    print('Each of the following lists represents a type of conversion. Please test a few from each list', file=sys.stderr)
    for keyword, l in keyword_index.items():
        print('\n', keyword, file=sys.stderr)
        for k, v in l:
            print(' ', k, '->', v, file=sys.stderr)
        
print(json.dumps(d, sort_keys=True, indent=0, separators=(',', ': ')))






















