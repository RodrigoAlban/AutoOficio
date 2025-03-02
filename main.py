from docxtpl import DocxTemplate
from tkinter import *
from tkinter import ttk
import os
import time

from Context.context import TemplateContext

# os - Dinamicamente constrói o caminho do template já existente 
template_path = os.path.join(os.path.dirname(__file__), "Templates", "my_word_template.docx")

# docxtpl - Carrega o template .docx 
doc = DocxTemplate(template_path)

class AutoOficio:
    
    def __init__(self, root):

        # tkinter - Dá um nome
        root.title("AutoOfício")

        # tkinter - Define a moldura (mainframe) da janela que vai segurar os conteúdos da UI
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # tkinter - Cria os campos (Widget) de entrada de dados
        self.NOME_SOCIAL = StringVar()
        NOME_SOCIAL_entry = ttk.Entry(mainframe, width=50, textvariable=self.NOME_SOCIAL)
        NOME_SOCIAL_entry.grid(column=1, row=1, sticky=(W, E))
        ttk.Label(mainframe, text="Nome Social").grid(column=0,row=1, sticky=W)

        self.DATA_POR_EXTENSO = StringVar()
        DATA_POR_EXTENSO_entry = ttk.Entry(mainframe, width=50, textvariable=self.DATA_POR_EXTENSO)
        DATA_POR_EXTENSO_entry.grid(column=1, row=2, sticky=(W, E))
        ttk.Label(mainframe, text="Data por Extenso").grid(column=0,row=2, sticky=W)

        # tkinter - Define o botão com a opção de gerar o .docx a partir do template
        ttk.Button(mainframe, text="Gerar", command=self.gerar).grid(column=3, row=3, sticky=W)

        # tkinter - Itera todos os widgets e adiciona um padding neles, para os campos não ficarem todos colados
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        # tkinter - Coloca o foco do cursor do teclado no primeiro widget, para que os usuários não tenham que clicar no campo para digitar
        NOME_SOCIAL_entry.focus()

        # tkinter - Se o usuário apertar enter, ele automaticamente gera o .docx
        root.bind("<Return>", self.gerar)
        
    
    # docxtpl - Substitui as variáveis do template .docx e cria um novo .docx
    def gerar(self, *args) :
        # docxtpl - Cria o contexto no template, procurando nele as variáveis para substituir
        context = TemplateContext.get_context(self)

        # os - Verifica o caminho do documento gerado, se não existir caminho, ele cria um para evitar erros
        output_dir = os.path.join(os.path.dirname(__file__), "GeneratedDocs")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, "generated_doc.docx")

        # docxtpl - Gera e armazena o documento com o contexto atualizado
        doc.render(context)
        doc.save(output_path)

        # Espera meio segundo e abre o documento gerado para visualização
        time.sleep(0.5)
        os.startfile(output_path)

# tkinter - Cria a janela principal (mainframe) da aplicação
root = Tk()

# tkinter - Chama a classe principal, mandando o mainframe de parâmetro, para fazer tudo funcionar, obviamente
AutoOficio(root)

# tkinter - Inicia o loop de eventos, que é necessário para tudo aparecer na tela e permitir que o usuário interaja
root.mainloop()

