import numpy as np
from sympy import sympify, lambdify, Symbol
from typing import Callable, Tuple

class IntegralRiemann:
    """
    Classe para calcular somas de Riemann para integração numérica.
    """
    
    def __init__(self):
        self.func = None
        self.func_str = ""
        self.a = 0
        self.b = 0
        self.n = 0
        self.dx = 0
        
    def analisar_funcao(self, func_str: str) -> Callable:
        try:
            x = Symbol('x')
            expr = sympify(func_str)
            return lambdify(x, expr, modules=['numpy'])
        except Exception as e:
            raise ValueError(f"Formato de função inválido: {e}")

    def validar_entradas(self, a: float, b: float, n: int) -> None:
        if a >= b:
            raise ValueError("O limite superior deve ser maior que o limite inferior")
        if n <= 0:
            raise ValueError("O número de subintervalos deve ser positivo")

    def calcular_somas_riemann(self) -> Tuple[float, float, float]:
        x = np.linspace(self.a, self.b, self.n + 1)
        
        soma_esquerda = sum(self.func(xi) for xi in x[:-1]) * self.dx
        soma_direita = sum(self.func(xi) for xi in x[1:]) * self.dx
        
        pontos_medio = [(x[i] + x[i+1]) / 2 for i in range(self.n)]
        soma_meio = sum(self.func(xi) for xi in pontos_medio) * self.dx
        
        return soma_esquerda, soma_direita, soma_meio

    def calcular_integral(self) -> None:
        try:
            print("\nCálculo da Integral por Soma de Riemann\n")
            
            self.func_str = "x**3 + x**2 - x*4" #escreva a função (ex: self.func_str = "x**3 + x**2 - x*4")
            self.func = self.analisar_funcao(self.func_str)
            print(f"Função escolhida: {self.func_str}")
            
            self.a = -1 #escreva o limite inferior (ex: self.a = -1)
            self.b = 4 #escreva o limite superior (ex: self.b = 4)
            self.n = 20 #escreva o número de subintervalos (ex: self.n = 20)
            print(f"Limite inferior 'a' escolhido: {self.a}")
            print(f"Limite superior 'b' escolhido: {self.b}")
            print(f"Número de subintervalos 'n' escolhido: {self.n}")
            
            self.validar_entradas(self.a, self.b, self.n)
            
            self.dx = (self.b - self.a) / self.n
            
            soma_esquerda, soma_direita, soma_meio = self.calcular_somas_riemann()
            
            print(f"\nResultados para f(x) = {self.func_str} no intervalo [{self.a}, {self.b}]:")
            print(f"Integral - Soma à Esquerda:     {soma_esquerda:.6f}")
            print(f"Integral - Soma à Direita:      {soma_direita:.6f}")
            print(f"Integral - Soma do Meio:        {soma_meio:.6f}")
            
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def main():
    calculadora = IntegralRiemann()
    calculadora.calcular_integral()

if __name__ == "__main__":
    main()
