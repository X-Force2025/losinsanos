from infix_to_postfix import infix_to_postfix

# Test 1: Simple addition
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])

# Test 2: Operator precedence
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])

# Test 3: Parentheses override precedence
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])

# Test 4: Complex expression
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])

# Test 5: Multiple operators and variables
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])
