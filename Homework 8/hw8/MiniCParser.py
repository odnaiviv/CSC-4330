# Vivian Do
# CSC 4330
# Homework 8
# Nov 26, 2023

import ply.yacc as yacc
# importing tokens from MiniCLexer
from MiniCLexer import tokens


# defining parsing rules
# for statements & operators
def p_stmt_assign(p):
  'stmt : ID ASSIGN expr SEMICOLON'
  p[0] = [p[1], '=', p[3]]


def p_stmt_block(p):
  'stmt : LBRACE stmtlist RBRACE'
  p[0] = p[2]


# for if & while statments
def p_stmt_if(p):
  'stmt : IF LPAREN expr RPAREN stmt'
  p[0] = ('if', p[3], p[5])


def p_stmt_while(p):
  'stmt : WHILE LPAREN expr RPAREN stmt'
  p[0] = ('while', p[3], p[5])


# defining parsing rules for statement lists
# for sngle & multiple statements
def p_stmtlist_single(p):
  'stmtlist : stmt'
  p[0] = [p[1]]


def p_stmtlist_multiple(p):
  'stmtlist : stmtlist stmt'
  p[0] = p[1] + [p[2]]


# defining parsing rules for expressions
# for identifiers, numbers, operators, & binary operations
def p_expr_id(p):
  'expr : ID'
  p[0] = ('id', p[1])


def p_expr_num(p):
  'expr : NUM'
  p[0] = ('num', p[1])


def p_expr_optr(p):
  'expr : expr OPTR expr'
  p[0] = (p[1], 'optr', p[2], p[3])


# handling errors
def p_error(p):
  print("Syntax error in input!")


# creating parser instance
parser = yacc.yacc()

# testing parser with input from question
input_text = "if(x > 9) { x = 0; y = y + 1; }"
parse_tree = parser.parse(input_text)
print(parse_tree)
