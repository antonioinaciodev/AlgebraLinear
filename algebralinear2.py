from sympy import symbols, sympify, linsolve
from sympy.sets.sets import EmptySet

x, y = symbols("x y")


def get_expression():
    expression = input("Digite a transformação T(x,y): ")
    return sympify(expression)


def matrix_t(expression_list):
    matriz = []
    vars = (x, y)

    for expressao in expression_list:
        linha_da_matriz = []
        for var in vars:
            linha_da_matriz.append(expressao.coeff(var))
        matriz.append(linha_da_matriz)
    return matriz


def main():
    expressions = [[x+y, x+y, x+y], [0, 0, 0], [x+y, 0, 0], [x, y, 0], [x, x, x], [x-y, y-x, 0], [x, y, x+y], [2*x+y, y, x]]
    while True:
        for i in range(8):
            print("T:ℝ² -> ℝ³")

            # expression = get_expression()
            expression = sympify(expressions[i])
            matrix = matrix_t(expression)
            print(f"\nTransformação: {expression}\n"
                  f"Matriz de transformação: {matrix}\n")

        # if input("Deseja encerrar?(sim/não) ").strip().lower() == "sim":
        #     break
        break


if __name__ == "__main__":
    main()
    # entrada é: transformação do R² --> R³
    # saída é: transformação, matriz de transformação na base canônica