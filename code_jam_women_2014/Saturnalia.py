def pretty_print(msg):
    l = len(msg)
    l1 = '+' + '-'*(l+2) + '+'
    l2 = '| ' + msg + ' |'
    l3 = '+' + '-'*(l+2) + '+'
    ans = '\n' + l1 +'\n' + l2 + '\n' + l3
    return ans
    
num_cases = int(input())
#print(num_cases)
for case in range(1, num_cases + 1):
    msg = input()
    ans = pretty_print(msg)
    print("Case #{}: {}".format(case, ans))