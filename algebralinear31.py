from sympy import symbols, sympify, linsolve, det, solve
from sympy import SympifyError, Matrix, Eq


def get_spaces():
    while True:
        try:
            dim_dom, dim_contra = str(input("Digite as dimensões do domínio e contradomínio: ")).strip().split(" ")
            dim_dom, dim_contra = int(dim_dom), int(dim_contra)
            break
        except ValueError:
            print("valor inválido")

    vars = []
    while True:
        vars = input(f"Digite as variáveis: ").strip().lower().split()

        if len(vars) != dim_dom:
            print("Quantidade incorreta de variáveis")
            continue

        variaveis_validas = True
        for var in vars:
            if not var.isidentifier():
                print(f"Variável inválida: {var}")
                variaveis_validas = False
                break

        if variaveis_validas:
            break

    return dim_dom, dim_contra, vars

def gerar_matriz_canonica(vars, expression):
    """Gera a matriz da transformação linear na base canônica"""
    n = len(vars)
    base_canonica = [ [1 if i == j else 0 for i in range(n)] for j in range(n) ]
    matriz = []
    sym_vars = symbols(vars)

    for vetor in base_canonica:
        imagem = [expr.subs(dict(zip(sym_vars, vetor))) for expr in expression]
        matriz.append(imagem)

    return Matrix(matriz).T

def autovalores_autovetores(matriz):
    """Calcula autovalores e autovetores de uma matriz sem usar funções prontas"""
    x = symbols('x')
    I = Matrix.eye(matriz.shape[0])
    A_menos_xI = matriz - x * I

    # Passo 1: Polinômio característico
    polinomio = det(A_menos_xI)

    # Passo 2: Resolver o polinômio característico
    autovalores = solve(Eq(polinomio, 0), x)

    resultado = []

    for lamb in autovalores:
        A_lambda_I = matriz - lamb * I
        # Passo 3: Resolver (A - λI)v = 0
        sistema = A_lambda_I.nullspace()
        autovetores = sistema if sistema else ['[vazio]']
        resultado.append((lamb, autovetores))

    return resultado

def get_expression(dim_dom, dim_contra, vars):
    while True:
        entrada = input(f"Digite as {dim_contra} coordenadas: ").strip().lower()
        expressao = [parte.strip() for parte in entrada.split(",")]

        if len(expressao) != dim_contra:
            print(f"Quantidade incorreta de coordenadas. Esperado: {dim_contra}")
            continue

        return sympify(expressao)


def vet_null(n):
    return [0] * n


def main():
    while True:
        # coleta dimensão do domínio, dimensão do contra domínio, variáveis
        dim_dom, dim_contra, vars = get_spaces()

        # coleta a transformação linear
        expression = get_expression(dim_dom, dim_contra, vars)
        
        # calcula os autovalores e autovetores
        matriz = gerar_matriz_canonica(vars, expression)
        resultados = autovalores_autovetores(matriz)
        
        # output das informações
        print(f"\nTransformação: {expression}")
        print(f"Matriz Associada: {matriz}")
        print("Autovalores e autovetores:")
        for lamb, vetores in resultados:
            print(f"Para λ = {lamb}: ", end="")
            for v in vetores:
                print(f"{v}")
        if input("Deseja encerrar?(sim/não) ").strip().lower() == "sim":
            break

if __name__ == "__main__":
    main()
