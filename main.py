from calculos import *

if __name__ == "__main__":
    calc = Calculadora()

    comando = 'on'
    comandos = ['off', '+', '-', '/', '*', 'SQRT', '**' 'Z']

    while comando != 'off':
        comando = 'on'
        while comando not in comandos:
            comando = input("Digite um comando: ")
        
        op = None
        if comando == '+':
            op = Adicao(float(input("Digite o operador: ")))
        elif comando == '-':
            op = Subtracao(float(input("Digite o operador: ")))
        elif comando == '/':
            op = Divisao(float(input("Digite o operador: ")))
        elif comando == '*':
            op = Multiplicacao(float(input("Digite o operador: ")))
        elif comando == '':
            op = RaizQuadrada(float(input("Digite o operador: ")))
        elif comando == '**':
            op = AoQuadrado(float(input("Digite o operador: ")))
        elif comando == 'Z':
            calc.desfazer_ultima()

        if op != None:
            calc.add_operacao(op)
        try:
            calc.calcular_total()
        except Exception as e:
            calc.operacoes.pop()
            print("Alerta: a divisao por zero aconteceu e numero retornado!")

        print(calc)
    
    print("Fim do programa!")