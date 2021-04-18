def pop_rep(A, B, alpha, beta):

    K = min(A, B)
    babies = int(K*0.02)
    a_babies = int((alpha * babies)/100)
    b_babies = int((beta * babies)/100)
    rem = babies - a_babies - b_babies

    if rem % 2 == 0:
        a_babies = a_babies + rem/2
        b_babies = b_babies + rem/2

    else:
        a_babies = a_babies + (rem-1)/2
        b_babies = b_babies + (rem-1)/2 + 1

    return int(a_babies), int(b_babies)

def pop_dec(A, B):

    a_die = int(A*0.01)
    b_die = int(B*0.01)

    return a_die, b_die

def cal_population(data):
    A_i, B_i, alpha, beta, years = data[0], data[1], data[2], data[3], data[4]
    A = A_i
    B = B_i

    for i in range(years):
        a_babies, b_babies = pop_rep(A, B, alpha, beta)
        A_d, B_d = pop_dec(A, B)

        #update the population
        A = A + a_babies - A_d
        B = B + b_babies - B_d

    return A, B

num_cases = int(input())
# print(num_cases)
for case in range(1, num_cases + 1):
    data = input().split()
    data = list(map(int, data))
    acr, bou = cal_population(data)
    print("Case #{}: {} {}".format(case, acr, bou))