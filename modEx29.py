

def investimento(tipoInvest,valor):
    if tipoInvest == 1:
        novoValor = valor * 1.03
        print("Daqui um mês seu saldo de investimento na poupança será de:",novoValor)
    elif tipoInvest == 2:
        novoValor = valor * 1.05
        print("Daqui um mês seu saldo de investimento na renda fixa será de:",novoValor)
    else:
        print("Este número de operação não existe, tente novamente.")


def main():
    tipoInvest = int(input("digite o tipo de Investimento (1-Poupaça 2-Renda Fixa): "))
    valor = float(input("digite o valor do Investimento: "))


    investimento(tipoInvest,valor)
if __name__ == "__main__":
    main()