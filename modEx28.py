

def reajuste_preco(precoAtual,mediaMensal):
    if mediaMensal < 500 and precoAtual < 30:
        novoPreco = precoAtual * 1.10
    elif mediaMensal >= 500 and mediaMensal < 1000 and precoAtual >= 30 and precoAtual < 80 :
        novoPreco = precoAtual * 1.15
    elif mediaMensal >= 1000 and precoAtual >= 80:
        novoPreco = precoAtual * 0.95
    else:
        novoPreco = precoAtual

    print("O novo preço será ",novoPreco,"R$")

def main():
    precoAtual = float(input("digite o preço atual "))
    mediaMensal = float(input("digite a média mensal "))

    reajuste_preco(precoAtual,mediaMensal)

if __name__ == "__main__":
    main()