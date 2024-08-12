pars = dict()
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
pars['StatementList']['Id'] = rule_StatementList_1

print(pars)