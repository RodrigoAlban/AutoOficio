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
        '''Inicializa o aplicativo, criando a Árvore de Widgets, chamando os pais e seus filhos'''

        # tkinter - Dá um nome
        root.title("AutoOfício")

        # tkinter - Define a moldura (mainframe) da janela que vai segurar os conteúdos da UI
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Importa o FormBuilder somente agora, pra evitar erros circulares
        from UI.form_builder import FormBuilder

        # Constrói os campos (widgets) na tela, chamando o FormBuilder
        form_builder = FormBuilder(mainframe, self)
        first_field = form_builder.build_form()
    
        # tkinter - Foca cursor no primeiro campo
        first_field.focus()

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

        # Espera 0.2s (para evitar erros) e abre o documento
        time.sleep(0.2)
        os.startfile(output_path)

# tkinter - Cria a janela principal (mainframe) da aplicação, que no caso é arbitrariamente chamada de root (pattern do tkinter)
root = Tk()

# tkinter - Chama a classe principal, mandando o mainframe de parâmetro, para fazer tudo funcionar, obviamente
AutoOficio(root)

# tkinter - Inicia o loop de eventos, que é necessário para tudo aparecer na tela e permitir que o usuário interaja
root.mainloop()

