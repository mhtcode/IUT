from enum import Enum

tokens = []
look_ahead = ''
c = 0

rule1 = "StatementList -> Statement StatementList"
rule2 = "StatementList ->"
rule3 = "Statement -> Assignment"
rule4 = "Statement -> Conditional"
rule5 = "Statement -> Loop"
rule6 = "Assignment -> id = Expr ;"
rule7 = "Conditional -> if ( Expr ) { StatementList } else { StatementList }"
rule8 = "Loop -> while ( Expr ) { StatementList }"
rule9 = "Expr -> Factor RestExpr"
rule10 = "RestExpr -> + Factor RestExpr"
rule11 = "RestExpr ->"
rule12 = "Factor -> id"
rule13 = "Factor -> number"


class Token(Enum):
    Epsilon = ''
    Id = 'id'
    Equal = '='
    Semicolon = ';'
    LeftParen = '('
    RightParen = ')'
    LeftBrace = '{'
    RightBrace = '}'
    Plus = '+'
    Number = 'number'
    If = 'if'
    Else = 'else'
    While = 'while'

def tokenize(s: str):
    s = s.lstrip()

    if len(s) == 0:
        return Token.Epsilon
    
    for token in Token:
        if token != Token.Epsilon and s.startswith(token.value):
            return token

def get_char():
    global c      
    global look_ahead
    global tokens
    look_ahead = tokenize(tokens[c]).value
    c += 1
    if c == len(tokens):
        look_ahead = '$'
        c -= 1
    # print('----------->' + look_ahead)

first_dic = {
    'statement_list': ['if', 'while', 'id', ''],
    'statement': ['if', 'while', 'id'],
    'assignment': ['id',], 
    'conditional': ['if',],
    'loop': ['while',],
    'expr': ['id', 'number'],
    'rest_expr': ['+', ''],
    'factor': ['id', 'number'],
}

follow_dic = {
    'statement_list': ['$', '}'],
    'statement': ['if', 'while', 'id', '$', '}'],
    'assignment': ['if', 'while', 'id', '$', '}'], 
    'conditional': ['if', 'while', 'id', '$', '}'],
    'loop': ['if', 'while', 'id', '$', '}'],
    'expr': [';', ')'],
    'rest_expr': [';', ')'],
    'factor': ['+', ';', ')'],   
}


input_num = int(input())
input_lines = [input().split() for i in range(input_num)]
tokens = []
for l in input_lines:
    for i in range(len(l)):
        tokens.append(l[i])

get_char()

def statement_list():
    if look_ahead in first_dic['statement']:
        print(rule1)    
        statement()
        statement_list()
    else:
        print(rule2)


def statement():
    if look_ahead in first_dic['assignment']:
        print(rule3)
        assignment()
    elif look_ahead in first_dic['conditional']:
        print(rule4)
        conditional()
    elif look_ahead in first_dic['loop']:
        print(rule5)
        loop()


def assignment():
    print(rule6)
    get_char() # match '='
    get_char() # new look ahead
    expr()
    get_char()


def conditional():
    print(rule7)
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
    print(rule8)
    get_char() # '('
    get_char()
    expr()
    get_char() # '{' 
    get_char()
    statement_list()
    get_char() # '}'
    

def expr():
    print(rule9)
    factor()
    rest_expr()


def rest_expr():
    if look_ahead == '+':
        print(rule10)
        get_char()
        factor()
        rest_expr()
    else:
        print(rule11)
        

def factor():
    if look_ahead == 'id':
        print(rule12)
        get_char()
    else:
        print(rule13)
        get_char()

# print(tokens)
          
statement_list()   
        





