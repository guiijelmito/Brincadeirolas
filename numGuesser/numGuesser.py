import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def adivinharNumero():

    # Limpa o label de texto da janela, o campo de entrada e o botão
    texto.pack_forget()
    input.pack_forget()
    botao.pack_forget()
    
    # O método pack_forget() remove o widget da janela
    
    # Cria um label de loading e uma barra de progresso
    loading = tk.Label(root, text="Pensando...")
    loading.pack()
    
    # O método ProgressBar() cria uma barra de progresso, horizontal, com 5 segundos de duração
    progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=100)
    progresso.pack()
    
    def atualizar_barra(loading_label=loading):
        valor_atual = progresso['value']
        if valor_atual < 100:
            progresso["value"] += 20  # Aumenta o valor em 20 a cada atualização
            root.after(1000, atualizar_barra)  # Chama a função novamente após 1000 milissegundos (1 segundo)
            
            if valor_atual > 30 and valor_atual < 50:
                loading_label['text'] = "Consultando o Guru..."
                
            if valor_atual > 60 and valor_atual < 90:
                loading_label['text'] = "Chamando o Universo..."
                
        else:
            # Quando a barra atinge 100%, esconda os elementos temporários e mostre o resultado
            loading.pack_forget()
            progresso.pack_forget()
            resultado = tk.Label(root, text="O número que você pensou é: " + input.get())
            resultado.pack()
            
            # Abre a imagem e converte para o formato PhotoImage
            imagem_feliz = Image.open("feliz.jpg")
            imagem_feliz = ImageTk.PhotoImage(imagem_feliz)
            
            # Cria um label para exibir a imagem
            label_imagem = tk.Label(root, image=imagem_feliz)
            label_imagem.image = imagem_feliz  # Mantém uma referência para evitar que a imagem seja removida pela coleta de lixo
            label_imagem.pack()

    # Inicia o processo de atualização da barra de progresso
    root.after(0, atualizar_barra)
     
# Cria uma janela 

root = tk.Tk() # Importa o módulo tkinter, com o alias tk, usando o método Tk() para criar uma janela

# Define o título da janela

root.title("Adivinhador mágico")

# Define o tamanho da janela

root.geometry("500x500")

# Cria um label
texto = tk.Label(root, text="Digite o número que você está pensando: ") 

texto.pack() # O método pack() organiza os widgets de forma que eles ocupem o menor espaço possível

input = tk.Entry(root) # Cria um campo de entrada de texto
input.pack() # Organiza o campo de entrada de texto

# Cria um botão com o texto "Adivinhar"
botao = tk.Button(root, command=adivinharNumero, text="Enviar")
botao.pack() # Organiza o botão

# Inicializa o loop principal da janela
root.mainloop()