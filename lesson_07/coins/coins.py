user_input = int(input('Please enter an amount in cents less than a dollar.'))
if 0 <= user_input <= 99:
    quarters = user_input // 25
    q_leftover = user_input % 25
    dimes = q_leftover // 10
    d_leftover = q_leftover % 10
    nickels = d_leftover // 5
    n_leftover = d_leftover % 5
    penny = n_leftover
    print(f'Q: {quarters} D: {dimes} N: {nickels} P: {penny}')
else:
    print('not a valid amount')

