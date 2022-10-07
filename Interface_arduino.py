import serial   # Importando a biblioteca que faz a comunicação entre python e a porta serial
from tkinter import *  # Importando a biblioteca responsável pela interface gráfica.

valor_led = 1  # Variável para definir apenas o estado inicial dos Leds
valor_led2 = 1

arduino = serial.Serial('COM9', 9600)  # Função que está definindo com qual porta serial o código irá se comunicar e o baud rate. Ambos foram definidos no arduino IDE


def funcao_botao():
    global valor_led  # Variavel global de valor_led para retornar com o valor = 1 que já foi definido antes
    global arduino

    if valor_led == 1:  # quando o botão é acionado, ele está com o valor "1" atribuído a ele
        valor_led = 0   # Para que, quando o botão for acionado de novo o estado do led mude, é necessário atribuir outro valor para a variável
        arduino.write(b'1')  # Quando acionado, o valor '1' é enviado para a porta serial do arduino, fazendo com que a ledVermelha Ligue. Isso está especificado no código no arduino IDE.
        label_estado_led["text"] = "  LIGADO "  # a caixa de texto da interface irá mostrar a palavra "ligado" para representar o estado do led.
        label_estado_led["foreground"] = "black"  # Essa função representa a cor da letra da caixa de texto
    else:
        valor_led = 1
        arduino.write(b'0')  # o 'b' é necessário para que o arduino identifique o número em questão em binário, fazendo assim a correta leitura do valor recebido na porta serial.
        label_estado_led["text"] = "DESLIGADO"
        label_estado_led["foreground"] = "black"

def funcao_botao2():
    global valor_led2
    global arduino

    if valor_led2 == 1:
        valor_led2 = 0
        arduino.write(b'2')
        label_estado_led2["text"] = "  LIGADO "
        label_estado_led2["foreground"] = "black"
    else:
        valor_led2 = 1
        arduino.write(b'3')
        label_estado_led2["text"] = "DESLIGADO"
        label_estado_led2["foreground"] = "black"



janela = Tk()

label_1 = Label(janela, text="LED VERMELHA", font="Arial 22",background="yellow",foreground="red")
label_1.place(x=300,y=50)

label_estado_led = Label(janela,text="",font="Arial 15",background="red")
label_estado_led.place(x=360,y=140)

botao_1 = Button(janela, width=20, text="ENVIAR", command=funcao_botao ,background="yellow")
botao_1.place(x=350, y=300)

janela.geometry("600x400+0+0")
janela.configure(background="black")


label_2 = Label(janela, text="LED AZUL    ", font="Arial 22",background="yellow",foreground="blue")
label_2.place(x=50,y=50)

label_estado_led2 = Label(janela,text="",font="Arial 15",background="blue")
label_estado_led2.place(x=70,y=140)

botao_2 = Button(janela, width=20, text="ENVIAR", command=funcao_botao2 ,background="yellow")
botao_2.place(x=50, y=300)

janela.mainloop()