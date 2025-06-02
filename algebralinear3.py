from sympy import symbols, sympify, linsolve, Matrix
from sympy import SympifyError


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


def get_expression(dim_dom, dim_contra, vars):
    while True:
        entrada = input(f"Digite as {dim_contra} coordenadas da transformação (separadas por vírgulas): ").strip().lower()
        expressao = [parte.strip() for parte in entrada.split(",")]

        if len(expressao) != dim_contra:
            print(f"Quantidade incorreta de coordenadas. Esperado: {dim_contra}")
            continue

        return sympify(expressao)


def autovalores_autovetores(expression, vars):
    dim = len(vars)
    sym_vars = symbols(vars)

    # Base canônica
    base_canonica = [[1 if i == j else 0 for i in range(dim)] for j in range(dim)]

    # Matriz da transformação
    colunas = []
    for vetor in base_canonica:
        imagem = [expr.subs(dict(zip(sym_vars, vetor))) for expr in expression]
        colunas.append(imagem)

    matriz = Matrix(colunas).T

    # Cálculo de autovalores e autovetores
    autovalores = matriz.eigenvals()
    autovetores = matriz.eigenvects()

    return matriz, autovalores, autovetores


def main():
    while True:
        dim_dom, dim_contra, vars = get_spaces()

        if dim_dom != dim_contra:
            print("A transformação deve ser quadrada para ter autovalores e autovetores.")
            continue

        expression = get_expression(dim_dom, dim_contra, vars)

        matriz, autovalores, autovetores = autovalores_autovetores(expression, vars)

        print(f"\nTransformação: {expression}")
        print(f"Matriz da transformação na base canônica:\n{matriz}")

        print("\nAutovalores:")
        for val, mult in autovalores.items():
            print(f"  {val} (multiplicidade: {mult})")

        print("\nAutovetores:")
        for val, mult, vetores in autovetores:
            print(f"\n  Para λ = {val}:")
            for v in vetores:
                print(f"    {v}")

        if input("\nDeseja encerrar? (sim/não): ").strip().lower() == "sim":
            break


if __name__ == "__main__":
    main()
