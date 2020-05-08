

def balancedBrackets(string):
    stack = []
    brackets = ['{', '}', '[', ']', '(', ')',"|"]
    count = 0
    for bracket in string:
        if bracket == '|':
            count += 1
        if bracket == '{' or bracket == "[" or bracket =='(':
            stack.append(bracket)
            print(stack)
        else:
            if stack == []:
                print(stack)
                return False
          
            if bracket in brackets:
               
                stack_pop = stack.pop()

                if bracket == ')' and stack_pop != '(':
                    return False

                if bracket == '}' and stack_pop != '{':
                    return False
                if bracket == ']' and stack_pop != '[':
                    return False
                # if bracket == '|' and stack_pop != '|':
                #     return False
                
                    
                
    if count % 2 != 0:
        print(count)
        return False
    if stack == []:
        return True

    else:
        return False



print(balancedBrackets("{}||"))
                











# def balancedBrackets(string):
#     # Write your code here

#     # Write your code here
#     stack = []

#     brackets = {'{': '}', '[': ']', '(': ')'}
#     match = True
#     count = 0
#     for bracket in string:
#         print(bracket)
#         if bracket == '|':
#             count += 1
#         print(count)
#         if bracket in ['}', ']', ')']:
            
#             if stack == [] or brackets[stack.pop()] != bracket :
#                 match = False
               
#             else:
#                 print(stack, "stack")
#                 stack.append(bracket)
                
#         if stack:
#             match = False

#         else:
#             match = True
#     if count % 2 != 0:
#             match = False
#     return match



# print(balancedBrackets("{{||[]|}|}"))