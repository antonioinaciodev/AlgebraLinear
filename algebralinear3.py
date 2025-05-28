from sympy import symbols, sympify, linsolve, Matrix
from sympy.sets.sets import EmptySet

x, y, z = symbols("x y z")


def get_expression():
    expression = input("Digite a transformação T(x,y,z): ")
    return sympify(expression)


def vet_null():
    return [0, 0, 0]


def matrix_t(expression_list):
    matriz = []
    vars = (x, y, z)
    
    for expressao in expression_list:
        linha_da_matriz = []
        for var in vars:
            linha_da_matriz.append(expressao.coeff(var))
        matriz.append(linha_da_matriz)
    return Matrix(matriz)


def exibir_autoval_autovet(lista_expressoes):
    matriz_A = matrix_t(lista_expressoes)
    print(f"Matriz de Transformação A:\n{matriz_A}\n")

    if not matriz_A.is_square:
        print("Autovalores e autovetores são definidos apenas para matrizes quadradas.")
        return

    try:
        # eigenvects() retorna uma lista de tuplas: (autovalor, multiplicidade_alg, [autovetores_base])
        autoval_autovet_data = matriz_A.eigenvects()
    except Exception as e:
        print(f"Erro ao calcular autovalores/autovetores: {e}")
        return

    if not autoval_autovet_data:
        print("Não foram encontrados autovalores/autovetores (ou a matriz é tal que o método não os retorna).")
        return

    for autoval, multiplicidade, vetores_base_matrix_list in autoval_autovet_data:
        print(f"Autovalor: {autoval} (Multiplicidade Algébrica: {multiplicidade})")
        
        autovetores_formatados = []
        for vetor_matrix in vetores_base_matrix_list:
            autovetores_formatados.append(list(vetor_matrix))
        print(f"Autovetores: (base para o autoespaço): {autovetores_formatados}")


def dim_NucT(kernel):
    return len(kernel) if kernel != [[0, 0, 0]] else 0


def dim_ImT(kernel):
    return 3 - dim_NucT(kernel)


def main():
    expressions = [[x, y, z], [0, 0, 0], [x, 2*y, 3*z], [x-y, y-z, z-x], [x+y+z, 0, 0]]
    while True:
        for i in range(5):
            print("T:ℝ³ -> ℝ³")
            
            # expression = get_expression()
            expression = sympify(expressions[i])
            
            
            
            print(f"\nTransformação: {expression}\n")
            exibir_autoval_autovet(expression)
            print()

        # if input("Deseja encerrar?(sim/não) ").strip().lower() == "sim":
        #     break
        break


if __name__ == "__main__":
    main()
    # entrada é: transformação do R³ --> R³
    # saída é: autovalores, autovetores