histórico = []
class calculadora:
    def soma(n1, n2):
        resultado = n1 + n2
        return resultado
    def subtração(n1, n2):
        resultado = n1 - n2
        return resultado
    def multiplicação(n1, n2):
        resultado = n1 * n2
        return resultado
    def divisão(n1, n2):
        if n2 == 0:
            resultado = "pode não man"
        else:
            resultado = n1 / n2
        return resultado
    def mostrar_histórico():
        print("Histórico: {}".format(histórico))
    
while True:
    calculo = int(input("""
    qual o calculo
    [1] - soma
    [2] - subtração
    [3] - multiplicação
    [4] - divisão
    [5] - mostrar histórico
    [6] - limpar
    > """))
    
    if calculo <= 3:
        n1 = float(input("n1 > "))
        n2 = float(input("n2 > "))
        ListaDeCalculos = [calculadora.soma(n1, n2),calculadora.subtração(n1, n2),calculadora.multiplicação(n1, n2),calculadora.divisão(n1, n2),calculadora.mostrar_histórico()]
        print(ListaDeCalculos[calculo])
        histórico.append(ListaDeCalculos[calculo])
    elif calculo == 4:
        calculadora.mostrar_histórico()
    elif calculo == 5:
         histórico.clear()
    else:
        print("escolha uma opção válida")
        