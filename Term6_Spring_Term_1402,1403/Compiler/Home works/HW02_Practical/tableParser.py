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
        
row = {
    'Dollar': '',
    'Id': '',
    'Equal': '',
    'Semicolon': '',
    'LeftParen': '',
    'RightParen': '',
    'LeftBrace': '',
    'RightBrace': '',
    'Plus': '',
    'Number': '',
    'If': '',
    'Else': '',
    'While': '',
}     

parse_table = {
    'StatementList':
    {},
    'Statement': row.copy(),
    'Assignment': row.copy(),
    'Conditional': row.copy(),
    'Loop': row.copy(),
    'Expr': row.copy(),
    'RestExpr': row.copy(),
    'Factor': row.copy(),
}

def table_init():
    global parse_table
    parse_table['StatementList']['Id'] = rule1
    parse_table['StatementList']['While'] = rule1
    parse_table['StatementList']['If'] = rule1
    parse_table['StatementList']['RightBrace'] = rule2
    parse_table['StatementList']['Dollar'] = rule2
    parse_table['Statement']['Id'] = rule3
    parse_table['Statement']['If'] = rule4
    parse_table['Statement']['While'] = rule5
    parse_table['Assignment']['Id'] = rule6
    parse_table['Conditional']['If'] = rule7
    parse_table['Loop']['While'] = rule8
    parse_table['Expr']['Id'] = rule9
    parse_table['Expr']['Number'] = rule9
    parse_table['RestExpr']['Plus'] = rule10
    parse_table['RestExpr']['Semicolon'] = rule11
    parse_table['RestExpr']['RightParen'] = rule11
    parse_table['RestExpr']['Dollar'] = rule11
    parse_table['Factor']['Id'] = rule12
    parse_table['Factor']['Number'] = rule13
    
table_init()

get_char()

stack = ['$', 'StatementList']

def match():
    global stack
    if stack[-1] not in parse_table.keys():
        stack.pop()
        get_char()
    return


def expand():
    if stack[-1] == 'StatementList' and look_ahead == 'id':
        print(parse_table['StatementList']['Id'])
        stack.pop()
        stack.append('StatementList')
        stack.append('Statement')
        
    elif stack[-1] == 'StatementList' and look_ahead == 'while':
        print(parse_table['StatementList']['While'])
        stack.pop()
        stack.append('StatementList')
        stack.append('Statement')
        
    elif stack[-1] == 'StatementList' and look_ahead == 'if':
        print(parse_table['StatementList']['If'])
        stack.pop()
        stack.append('StatementList')
        stack.append('Statement')
        
    elif stack[-1] == 'StatementList' and look_ahead == '}': 
        print(parse_table['StatementList']['RightBrace'])     
        stack.pop()
        
    elif stack[-1] == 'StatementList' and look_ahead == '$': 
        print(parse_table['StatementList']['Dollar'])     
        stack.pop()
        
    elif stack[-1] == 'Statement' and look_ahead == 'id':
        print(parse_table['Statement']['Id'])
        stack.pop()
        stack.append('Assignment')
        
    elif stack[-1] == 'Statement' and look_ahead == 'if':
        print(parse_table['Statement']['If'])
        stack.pop()
        stack.append('Conditional')
        
    elif stack[-1] == 'Statement' and look_ahead == 'while':
        print(parse_table['Statement']['While'])
        stack.pop()
        stack.append('Loop')
        
    elif stack[-1] == 'Assignment' and look_ahead == 'id':
        temp = 'id = Expr ;'
        temp_list = temp.split()
        print(parse_table['Assignment']['Id'])
        stack.pop()
        for i in range(len(temp_list) - 1, -1, -1):
            stack.append(temp_list[i])
        
    elif stack[-1] == 'Conditional' and look_ahead == 'if':
        temp = 'if ( Expr ) { StatementList } else { StatementList }'
        temp_list = temp.split()
        print(parse_table['Conditional']['If'])
        stack.pop()
        for i in range(len(temp_list) - 1, -1, -1):
            stack.append(temp_list[i])

    elif stack[-1] == 'Loop' and look_ahead == 'while':
        temp = 'while ( Expr ) { StatementList }'
        temp_list = temp.split()
        print(parse_table['Loop']['While'])
        stack.pop()
        for i in range(len(temp_list) - 1, -1, -1):
            stack.append(temp_list[i])
            
    elif stack[-1] == 'Expr' and look_ahead == 'id':
        temp = 'Factor RestExpr'
        temp_list = temp.split()
        print(parse_table['Expr']['Id'])
        stack.pop()
        for i in range(len(temp_list) - 1, -1, -1):
            stack.append(temp_list[i])

    elif stack[-1] == 'Expr' and look_ahead == 'number':
        temp = 'Factor RestExpr'
        temp_list = temp.split()
        print(parse_table['Expr']['Number'])
        stack.pop()
        for i in range(len(temp_list) - 1, -1, -1):
            stack.append(temp_list[i])    
    
    elif stack[-1] == 'RestExpr' and look_ahead == '+': 
        temp = '+ Factor RestExpr'
        temp_list = temp.split()
        print(parse_table['RestExpr']['Plus'])
        stack.pop()
        for i in range(len(temp_list) - 1, -1, -1):
            stack.append(temp_list[i]) 
    
    elif stack[-1] == 'RestExpr' and look_ahead == ';': 
        print(parse_table['RestExpr']['Semicolon'])
        stack.pop()

    elif stack[-1] == 'RestExpr' and look_ahead == ')': 
        print(parse_table['RestExpr']['RightParen'])
        stack.pop()
    
    elif stack[-1] == 'RestExpr' and look_ahead == '$': 
        print(parse_table['RestExpr']['Dollar'])
        stack.pop()
        
    elif stack[-1] == 'Factor' and look_ahead == 'id':
        print(parse_table['Factor']['Id'])
        stack.pop()
        stack.append('id')

    elif stack[-1] == 'Factor' and look_ahead == 'number':
        print(parse_table['Factor']['Number'])
        stack.pop()
        stack.append('number')
    return


while len(stack) > 1:
    if stack[-1] in parse_table.keys():
        expand()
    else:
        match()



