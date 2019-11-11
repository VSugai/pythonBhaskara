# Função que confere a resposta do usuário para uma equação de segundo grau
def func_mat():
	# Separa a equação em a, b e c
    import math
    a = 1
    b = 2
    c = -20
	
    # Cálculo do y
    y=(b**2)-(4*a*c)
    y=math.sqrt(y)
	
	# Cáculo das raízes
    res1 = (-b+y)/(2*a)
    res2 = (-b-y)/(2*a)
    
    res1 = round(res1, 4)
    res2 = round(res2, 4)
    
	# Conversa com o usuário
    print("Quais os valores das raízes da equação xˆ2 + 2*x - 20 ?")
    x1 = float(input("Insira um valor para x1 (com ponto e QUATRO casa após o ponto): "))
    x2 = float(input("Insira um valor para x2 (com ponto e QUATRO casa após o ponto): "))
    
	# Confere se a resposta foi certa, independente da ordem das raízes
    if x1 == res1 and x2 == res2 or x1 == res2 and x2 == res1:
        print("Parabéns!")
    else:
        print("Essa não é bem a resposta correta, os valores são: ", res1 ," e ", res2)

# Chama a função
func_mat()
