from controlador import Controlador
import datetime

if __name__ == "__main__":
    sessao = Controlador()
    while True:
        print("-----########################-----")
        print("Olá, seja Bem vindo ao Controlador de Gastos, o que deseja fazer hoje?")
        print("1 - Adicionar Gasto")
        print("2 - Visualizar Gastos do mês")
        print("3 - Visualizar Gastos do ano")
        print("4 - Fechar e Salvar")
        escolha = input()
        match escolha:
            case "1":
                print("Gasto foi realizado hoje? (s/n)")
                hoje = input()
                if hoje == "s" or hoje == "S":
                    data = datetime.datetime.today()
                else:
                    numero_valido = True
                    while numero_valido:
                        try:
                            print("Qual foi o dia?")
                            dia = int(input())
                            print("Qual foi o mês?")
                            mes = int(input())
                            print("Qual foi o ano?")
                            ano = int(input())
                            data = datetime.datetime(ano, mes, dia)
                            numero_valido = False
                        except:
                            print("Número inválido")
                print("É um gasto recorrente? (s/n)")
                recorrente = input()
                if recorrente == "s" or recorrente == "S":
                    recorrente = "Sim"
                else:
                    recorrente = "Não"

                print("Qual é o tipo?")
                tipo = input()

                numero_valido = True
                while numero_valido:
                    try:
                        print(
                            'Qual foi o valor? (utilizar "." para separa as casas decimais) '
                        )
                        valor = float(input())
                        print(valor)
                        numero_valido = False
                    except:
                        print("Número Inválido")
                sessao.registrar_gasto(data, tipo, recorrente, valor)
                print("Registrado com Sucesso")
            case "2":
                numero_valido = True
                while numero_valido:
                    try:
                        print("Qual ano deseja visualizar?")
                        ano = int(input())
                        print("Qual mês deseja visualizar?")
                        mes = int(input())
                        if mes > 12 or mes < 1:
                            raise Exception()
                        numero_valido = False
                    except:
                        print("Número Inválido")
                sessao.grafico_mes(mes, ano)
            case "3":
                numero_valido = True
                while numero_valido:
                    try:
                        print("Qual ano deseja visualizar?")
                        ano = int(input())
                        numero_valido = False
                    except:
                        print("Número Inválido")
                sessao.grafico_ano(ano)
            case "4":
                sessao.salvar_tabela()
                exit()
            case _:
                print("Opção Incorreta, selecione novamente")
