def back(a, b, c):
    disk = b * b - 4 * a * c
    ans = ()
    if disk > 0:
        ans = ((-b - disk ** 0.5) / 2 * a, (-b + disk ** 0.5) / 2 * a)
    if ans[1] != None:
        return f'x1 = {ans[0]}, x2 = {ans[1]}'
    else:
        return f'x = {ans[0]}'

def front():
    a, b, c = map(int, input('Введите коэффициенты при a, b и c ').split())
    print(back(a, b, c))

front()



