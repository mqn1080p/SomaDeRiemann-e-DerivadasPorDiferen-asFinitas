import numpy as np
import sympy as sp

def parse_funcao(str_funcao):     
    """Converte representação em string da função para função executavel."""
    try:     
        x = sp.symbols('x')
        return sp.lambdify(x, sp.sympify(str_funcao), modules=['numpy'])
    except:     
        raise ValueError("Expressão da função inválida")

def derivada_diferencas_finitas():     
    """Calcula aproximações da derivada usando diferenças finitas."""
    print("\nAproximação de Derivada por Diferenças Finitas\n")
    
    try:     
        
        str_funcao = input("f(x) = ")  #Escreva a função (ex: str_funcao = "sin(x)")
        print(f"Função escolhida: {str_funcao}")
        
        x0 = float(input("x0 = "))  #Escreva o valor de x0 (ex: x0 = 3.0)
        print(f"Valor de x0 escolhido: {x0}")
        
        h = float(input("h = "))  #Escreva o valor de h (ex: h = 0.001)
        print(f"Valor de h escolhido: {h}")
        
        if h == 0:     
            raise ValueError("h não pode ser zero")

        f = parse_funcao(str_funcao)
        
        progressiva = (f(x0 + h) - f(x0)) / h
        regressiva = (f(x0) - f(x0 - h)) / h
        centrada = (f(x0 + h) - f(x0 - h)) / (2 * h)

        #resultados
        print(f"\nResultados para f(x) = {str_funcao} em x = {x0} e com h = {h}: ")
        print(f"Diferença Progressiva:      {progressiva: .6f}")
        print(f"Diferença Regressiva:       {regressiva: .6f}")
        print(f"Diferença Centrada:         {centrada: .6f}")

    except ValueError as e:     
        print(f"Erro: {e}")
    except Exception as e:     
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":     
    derivada_diferencas_finitas()
