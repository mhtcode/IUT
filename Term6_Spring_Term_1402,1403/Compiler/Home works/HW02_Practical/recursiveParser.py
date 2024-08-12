from enum import Enum

tokens = []
look_ahead = ''
index = 0

rule_StatementList_1 = "StatementList -> Statement StatementList"
rule_StatementList_2 = "StatementList ->"
rule_Statement_1 = "Statement -> Assignment"
rule_Statement_2 = "Statement -> Conditional"
rule_Statement_3 = "Statement -> Loop"
rule_Assignment_1 = "Assignment -> id = Expr ;"
rule_Conditional_1 = "Conditional -> if ( Expr ) { StatementList } else { StatementList }"
rule_Loop_1 = "Loop -> while ( Expr ) { StatementList }"
rule_Expr_1 = "Expr -> Factor RestExpr"
rule_RestExpr_1 = "RestExpr -> + Factor RestExpr"
rule_RestExpr_2 = "RestExpr ->"
rule_Factor_1 = "Factor -> id"
rule_Factor_2 = "Factor -> number"


def tokenize(s: str):
    return [token.strip() for token in s.replace('\n', '').split()]

def get_char():
    global index      
    global look_ahead
    global tokens
    look_ahead = tokens[index]
    index += 1
    if index == len(tokens):
        look_ahead = '$'
        index -= 1

FIRST = {
    'statement_list': ['if', 'while', 'id', ''],
    'statement': ['if', 'while', 'id'],
    'assignment': ['id',], 
    'conditional': ['if',],
    'loop': ['while',],
    'expr': ['id', 'number'],
    'rest_expr': ['+', ''],
    'factor': ['id', 'number'],
}

FOLLOW = {
    'statement_list': ['$', '}'],
    'statement': ['if', 'while', 'id', '$', '}'],
    'assignment': ['if', 'while', 'id', '$', '}'], 
    'conditional': ['if', 'while', 'id', '$', '}'],
    'loop': ['if', 'while', 'id', '$', '}'],
    'expr': [';', ')'],
    'rest_expr': [';', ')'],
    'factor': ['+', ';', ')'],   
}

def statement_list():
    if look_ahead in FIRST['statement']:
        print(rule_StatementList_1)    
        statement()
        statement_list()
    else:
        print(rule_StatementList_2)


def statement():
    if look_ahead in FIRST['assignment']:
        print(rule_Statement_1)
        assignment()
    elif look_ahead in FIRST['conditional']:
        print(rule_Statement_2)
        conditional()
    elif look_ahead in FIRST['loop']:
        print(rule_Statement_3)
        loop()


def assignment():
    if look_ahead in FIRST['assignment']:
        print(rule_Assignment_1)
        get_char() # for '='
        get_char()
        expr()
        get_char()


def conditional():
    if look_ahead in FIRST['conditional']:
        print(rule_Conditional_1)
        get_char() # '(' 
        get_char() # new look ahead
        expr()
        get_char() # '{'
        get_char()
        statement_list()
        get_char() # 'else'
        get_char() # '{'
        get_char()
        statement_list()
        get_char() # '}'

        
def loop():
    if look_ahead in FIRST['loop']:
        print(rule_Loop_1)
        get_char() # '('
        get_char()
        expr()
        get_char() # '{' 
        get_char()
        statement_list()
        get_char() # '}'

def expr():
    if look_ahead in FIRST['expr']:
        print(rule_Expr_1)
        factor()
        rest_expr()


def rest_expr():
    if look_ahead == '+':
        print(rule_RestExpr_1)
        get_char()
        factor()
        rest_expr()
    else:
        print(rule_RestExpr_2)
        

def factor():
    if look_ahead == 'id':
        print(rule_Factor_1)
        get_char()
    else:
        print(rule_Factor_2)
        get_char()




def initial():
    global tokens
    input_num = int(input())
    input_lines = [input() for i in range(input_num)]
    tokens = []
    for each_line in input_lines:
            tokenized_line = tokenize(each_line)
            for word in tokenized_line:
                tokens.append(word)
    print(tokens)

    get_char()
    statement_list()

initial()

