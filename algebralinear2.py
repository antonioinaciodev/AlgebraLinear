from sympy import symbols, sympify, linsolve
from sympy import SympifyError, Matrix


def get_spaces():
    while True:
        try:
            dim_dom, dim_contra = str(
                input("Digite as dimensões do domínio e contradomínio: ")).strip().split(" ")
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
    while True:
        entrada = input(
            f"Digite as {dim_contra} coordenadas: ").strip().lower()
        expressao = [parte.strip() for parte in entrada.split(",")]

        if len(expressao) != dim_contra:
            print(f"Quantidade incorreta de coordenadas. Esperado: {dim_contra}")
            continue

        return sympify(expressao)


def vet_null(n):
    return [0] * n


def get_base(nome_base, dimensao):
    print(f"\nDigite os vetores da base {nome_base}: ")
    base = []

    for i in range(dimensao):
        while True:
            try:
                entrada = input(f"  Vetor {i+1} (separado por vírgulas): ").strip()
                coords = [sympify(x.strip()) for x in entrada.split(",")]

                if len(coords) != dimensao:
                    print(f"Vetor deve ter {dimensao} coordenadas.")
                    continue

                base.append(coords)
                break
            except (ValueError, SympifyError):
                print("Entrada inválida. Tente novamente.")
    return base


def matriz_relativa_bases(expression, vars, base_alpha, base_beta):
    sym_vars = symbols(vars)

    resultado = []
    for vetor in base_alpha:
        imagem = [expr.subs(dict(zip(sym_vars, vetor))) for expr in expression]

        coeficientes = symbols(f'c0:{len(base_beta)}')

        sistema = []
        # para cada coordenada dos vetores da base
        for i in range(len(base_beta[0])):
            soma = 0
            # soma será a equação composta pela soma dos coeficientes
            for j in range(len(base_beta)):
                # soma recebe coeficiente * coordenada atual
                soma += coeficientes[j] * base_beta[j][i]
            # no final, soma será a equação composta pela soma dos coeficientes da coordenada atual
            eq = soma - imagem[i]
            sistema.append(eq)

        solucao = linsolve(sistema, coeficientes)
        sol_vector = list(solucao)[0]
        resultado.append(sol_vector)

    # Usar Matrix do SymPy para transpor o resultado e converter para lista
    matriz_final = Matrix(resultado).T.tolist()

    return matriz_final


def main():
    while True:
        # coleta dimensão do domínio, dimensão do contra domínio, variáveis
        dim_dom, dim_contra, vars = get_spaces()

        # coleta a transformação linear
        expression = get_expression(dim_dom, dim_contra, vars)

        # coleta as bases
        base_dominio = get_base("base_dominio", dim_dom)
        base_contradominio = get_base("base_contradominio", dim_contra)

        # calcula a matriz
        matrix = matriz_relativa_bases(expression, vars, base_dominio, base_contradominio)

        # output das informações
        print(f"\nTransformação: {expression}\n"
              f"Base do domínio: {base_dominio}\n"
              f"Base do contradomínio: {base_contradominio}\n"
              f"Matriz transformação: \n{matrix}")
        if input("Deseja encerrar?(sim/não) ").strip().lower() == "sim":
            break


if __name__ == "__main__":
    main()
