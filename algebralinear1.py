from sympy import symbols, sympify, linsolve
from sympy.sets.sets import EmptySet

x, y = symbols("x y")


def get_expression():
    expression = input("Digite a transformação T(x,y): ")
    return sympify(expression)


def vet_null():
    return [0, 0]


def kernel_NucT(expression_list):
    # solucionar as expressões
    sol = linsolve(expression_list, x, y)

    # caso 1: não retornou solução
    if sol == EmptySet:
        return [vet_null()]

    # coletar as variáveis da solução
    s = list(sol)[0]
    vars = list(s.free_symbols)

    # caso 2: solução trivial
    if not vars:
        return [vet_null()]

    # caso 3: extrair os coeficientes das variáveis
    bases = []
    for var in vars:
        base_var = []
        for coord in s:
            base_var.append(coord.coeff(var))
        bases.append(base_var)
    return bases


def dim_NucT(kernel):
    return len(kernel) if kernel != [[0, 0]] else 0


def dim_ImT(kernel):
    return 2 - dim_NucT(kernel)


def main():
    expressions = [[x+y, x+y, x+y], [0, 0, 0], [x+y, 0, 0], [x, y, 0], [x, x, x], [x-y, y-x, 0], [x, y, x+y], [2*x+y, y, x]]
    while True:
        for i in range(8):
            print("T:ℝ² -> ℝ³")

            # expression = get_expression()
            expression = sympify(expressions[i])
            kernel = kernel_NucT(expression)
            dim = dim_NucT(kernel)
            img = dim_ImT(kernel)
            print(f"\nTransformação: {expression}\n"
                  f"Base do NucT: {kernel}\n"
                  f"Dimensão do NucT: {dim}\n"
                  f"Dimensão do ImT: {img}\n")

        # if input("Deseja encerrar?(sim/não) ").strip().lower() == "sim":
        #     break
        break


if __name__ == "__main__":
    main()
    # entrada é: transformação do R² --> R³
    # saída é: transformação, bases da transformação, dimensão do Núcleo, dimensão da Imagem