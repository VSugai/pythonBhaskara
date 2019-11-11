# Função que, dado uma valor para x, pergunta a resposta da equação
def func_mat2():
	# Pede x
    x = input("Insira um valor para x: ")
    x = float(x)
    print("Resolva a equação: " , x , "^ 2 + " , 2*x , "- 20")
    
	# Cácula o resultado
    res = x**2 + 2*x - 20
    
	# Pede o resultado do usuário
    userRes = input("Qual a resposta da equação? ")
    userRes = float(userRes)
    
	# Confere a resposta
    if userRes == res:
        print("Parabéns!")
    else:
        print("Essa não é bem a resposta correta, a resposta correta é: ", res)
		
# Chama a função
func_mat2()
