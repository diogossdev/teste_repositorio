def baskara(a:float, b:float, c:float) -> float:
    delta = b**2 - 4 * a * c
    
    x1 = (-b + delta**0.5) / 2 * a
    x2 = (-b - delta**0.5) / 2 * a
    return (f'x1 = {x1} e x2 = {x2}')

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
print(f" O valor das raizes são: {baskara(a, b, c)}.")

