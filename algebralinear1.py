from sympy import symbols, sympify, linsolve
from sympy.sets.sets import EmptySet


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
            print("quantidade incorreta de variáveis")
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
    allowed_vars = set(vars)

    while True:
        entrada = input(f"Digite as {dim_contra} coordenadas: ").strip().lower()
        expressao = [parte.strip() for parte in entrada.split(",")]

        if len(expressao) != dim_contra:
            print(f"Quantidade incorreta de coordenadas. Esperado: {dim_contra}")
            continue

        return sympify(expressao)


def vet_null(n):
    return [0] * n


def kernel_NucT(expression_list, vars):
    # definir variáveis
    sym_vars = symbols(vars)

    # solucionar as expressões
    sol = linsolve(expression_list, sym_vars)

    # caso 1: não retornou solução
    if sol == EmptySet:
        return [vet_null(len(expression_list))]

    # coletar as variáveis da solução
    s = list(sol)[0]
    vars = list(s.free_symbols)

    # caso 2: solução trivial
    if not vars:
        return [vet_null(len(expression_list))]

    # caso 3: extrair os coeficientes das variáveis
    bases = []
    for var in vars:
        base_var = []
        for coord in s:
            base_var.append(coord.coeff(var))
        bases.append(base_var)
    return bases


def dim_NucT(kernel):
    return len(kernel) if kernel != [vet_null(len(kernel[0]))] else 0


def dim_ImT(kernel, dim_contra):
    return dim_contra - dim_NucT(kernel)


def main():
    while True:
        # coleta dimensão do domínio, dimensão do contra domínio, variáveis
        dim_dom, dim_contra, vars = get_spaces()

        # coleta a transformação linear
        expression = get_expression(dim_dom, dim_contra, vars)

        # calcula a base do núcleo da transformação
        kernel = kernel_NucT(expression, vars)

        # calcula a dimensão do núcleo e da imagem
        dim = dim_NucT(kernel)
        img = dim_ImT(kernel, dim_contra)

        # output das informações
        print(f"\nTransformação: {expression}\n"
              f"Base do NucT: {kernel}\n"
              f"Dimensão do NucT: {dim}\n"
              f"Dimensão do ImT: {img}\n")
        if input("Deseja encerrar?(sim/não) ").strip().lower() == "sim":
            break


if __name__ == "__main__":
    main()
