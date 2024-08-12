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

parse_table = {
    'StatementList':
    {
        "id": rule_StatementList_1,
        "}": rule_StatementList_2,
        "if": rule_StatementList_1,
        "while": rule_StatementList_1,
        "$": rule_StatementList_2,
    },
    'Statement':
    {
        "id": rule_Statement_1,
        "if": rule_Statement_2,
        "while": rule_Statement_3,
    },
    'Assignment': 
    {
        "id": rule_Assignment_1,
    },
    'Conditional': 
    {
        "if": rule_Conditional_1,
    },
    'Loop': 
    {
        "while": rule_Loop_1,
    },
    'Expr': 
    {
        "id": rule_Expr_1,
        "number": rule_Expr_1
    },
    'RestExpr': 
    {
        ";": rule_RestExpr_2,
        ")": rule_RestExpr_2,
        "+": rule_RestExpr_1,
        "$": rule_RestExpr_2,
    },
    'Factor': 
    {
        "id": rule_Factor_1,
        "number": rule_Factor_2,
    },
}

STACK = ['$', 'StatementList']
def tokenize(s: str):
    return [token.strip() for token in s.replace('\n', '').split()]

def get_char():
    global tokens
    global index  
    global look_ahead
    look_ahead = tokens[index]
    index += 1
    if index == len(tokens):
        look_ahead = "$"
        index -= 1


def initial():
    global tokens, start
    input_num = int(input())
    input_lines = [input() for i in range(input_num)]
    tokens = []
    for each_line in input_lines:
            tokenized_line = tokenize(each_line)
            for word in tokenized_line:
                tokens.append(word)
    get_char()


initial()

def match():
    STACK.pop()
    get_char()
    return


def parsing():
    if STACK[-1] == 'StatementList':
        if look_ahead == 'id':
            print(parse_table['StatementList']['id'])
            STACK.pop()
            STACK.append('StatementList')
            STACK.append('Statement')
        
        elif look_ahead == 'while':
            print(parse_table['StatementList']['while'])
            STACK.pop()
            STACK.append('StatementList')
            STACK.append('Statement')
        
        elif look_ahead == 'if':
            print(parse_table['StatementList']['if'])
            STACK.pop()
            STACK.append('StatementList')
            STACK.append('Statement')
        
        elif look_ahead == '}': 
            print(parse_table['StatementList']['}'])     
            STACK.pop()
        
        elif look_ahead == '$': 
            print(parse_table['StatementList']['$'])     
            STACK.pop()
        
    elif STACK[-1] == 'Statement':
        if look_ahead == 'id':
            print(parse_table['Statement']['id'])
            STACK.pop()
            STACK.append('Assignment')
        
        elif look_ahead == 'if':
            print(parse_table['Statement']['if'])
            STACK.pop()
            STACK.append('Conditional')
        
        elif look_ahead == 'while':
            print(parse_table['Statement']['while'])
            STACK.pop()
            STACK.append('Loop')
        
    elif STACK[-1] == 'Assignment' and look_ahead == 'id':
        temp = 'id = Expr ;'
        print(parse_table['Assignment']['id'])
        STACK.pop()
        STACK.extend(reversed(tokenize(temp)))      
        
    elif STACK[-1] == 'Conditional' and look_ahead == 'if':
        temp = 'if ( Expr ) { StatementList } else { StatementList }'
        print(parse_table['Conditional']['if'])
        STACK.pop()
        STACK.extend(reversed(tokenize(temp))) 

    elif STACK[-1] == 'Loop' and look_ahead == 'while':
        temp = 'while ( Expr ) { StatementList }'
        print(parse_table['Loop']['while'])
        STACK.pop()
        STACK.extend(reversed(tokenize(temp))) 
            
    elif STACK[-1] == 'Expr':
        if look_ahead == 'id':
            temp = 'Factor RestExpr'
            print(parse_table['Expr']['id'])
            STACK.pop()
            STACK.extend(reversed(tokenize(temp))) 

        elif look_ahead == 'number':
            temp = 'Factor RestExpr'
            print(parse_table['Expr']['number'])
            STACK.pop() 
            STACK.extend(reversed(tokenize(temp)))    
    elif STACK[-1] == 'RestExpr':
        if look_ahead == '+': 
            temp = '+ Factor RestExpr'
            temp_list = temp.split()
            print(parse_table['RestExpr']['+'])
            STACK.pop()
            STACK.extend(reversed(['+', 'Factor', 'RestExpr'])) 

        elif look_ahead == ';' or look_ahead == ")": 
            print(parse_table['RestExpr'][';'])
            STACK.pop()
        elif look_ahead == '$': 
            print(parse_table['RestExpr']['$'])
            STACK.pop()
        
    elif STACK[-1] == 'Factor' and look_ahead == 'id':
        print(parse_table['Factor']['id'])
        STACK.pop()
        STACK.append('id')

    elif STACK[-1] == 'Factor' and look_ahead == 'number':
        print(parse_table['Factor']['number'])
        STACK.pop()
        STACK.append('number')
    return


while len(STACK) > 1:
    if STACK[-1] in parse_table.keys():
        parsing()
    else:
        match()

