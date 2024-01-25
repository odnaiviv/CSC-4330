# Vivian Do
# CSC 4330
# Homework 8
# Nov 26, 2023

import ply.lex as lex

# defining lexical tokens
tokens = (
    'ID',
    'NUM',
    'OPTR',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ASSIGN',
    'IF',
    'WHILE',
)

# reserved words
reserved = {
    'if': 'IF',
    'while': 'WHILE',
}

# defining lexer rules
# ignoring whitespaces
t_ignore = ' \t\n'
# defining regular expressions for operators
t_OPTR = r'>=|<=|==|>|<|\+|-|\*|/'
# defining regular expressions for numerical literals
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
# defining regular expressions for assignment
t_ASSIGN = r'='
# defining regular expressions for if & while statements
t_IF = r'if'
t_WHILE = r'while'


# defining regular expression for identifiers
# w/ reserved words handled separately
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'ID')
  return t


# defining regular expression for numbers
# includes integers & floating point numbers
def t_NUM(t):
  r'\d+(\.\d+)?'
  t.value = float(t.value)
  return t


# handling errors
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# creating lexer instance
lexer = lex.lex()
