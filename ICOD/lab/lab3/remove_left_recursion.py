def main():
    # accept the non terminals symbols

    # accept the terminal symbols 
    noOfRules=int(input())
    # Accept the rules 
    rule=dict()
    for _ in range(noOfRules):
        ruleString=list(input().split(" "))
        rule[ruleString[0]] = ruleString[2:]
    print("These are the rules you entered: ")
    print(rule) 
    newRules=dict()
    # check if left recursion is there 
    for key in rule:
        # print(key)
        # check if key is first letter of any rules 
        for item in rule[key]:
            if item[0]==key:
                # Then we have to resolve the recursion
                # create a new rule key first 
                newRuleKey=key+'\''
                # pop that item and store
                popped = rule[key].pop(rule[key].index(item))
                # create the new rule
                newRules[newRuleKey] = [popped[1:]+key,'3']
                # Now edit the old rule
                for some in rule[key]:
                    if some[0]!=key:
                        newSome=some+newRuleKey
                        rule[key].pop(rule[key].index(some))
                        rule[key].append(newSome)
                        # print(some)
    print("Following are the new rules : ")
    print(rule)
    print(newRules)
    #  if left recursion then:
        # solve 
        # Left recursion removal algorithm is :
            # if A -> A@ | # then
            #  A -> #A'
            #  A' -> @A | eps
    # print the new rules
main()

# Sample input 
"""
3
E -> E+T T
T -> T*F F
F -> (E) id

 """