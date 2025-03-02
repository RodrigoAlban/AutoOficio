from tkinter import *
from tkinter import ttk

class FormBuilder:
    def __init__(self, parent, app_instance):
        """
        Inicializa o FormBuilder
        
        Parâmetros:
            parent: Recebe a moldura pai aonde os campos (widgets) vão ser colocados
            app_instance: Recebe o "contexto" da aplicação, que possibilita a leitura da informação posta pelo usuário
        """
        self.parent = parent
        self.app = app_instance
        self.row = 1  # Primeira Row do Grid do mainframe

    def add_text_field(self, label_text, var_name, width=50):
        """Cria o Text Field dentro da Label"""
        # Cria a StringVar e armazena na app (app_instance)
        setattr(self.app, var_name, StringVar())
        var = getattr(self.app, var_name)
        
        # Cria o entry widget, o primeiro campo do aplicativo, aonde vai ser o foco do cursor, 
        # pro usuário poder digitar sem precisar clicar no campo
        entry = ttk.Entry(self.parent, width=width, textvariable=var)
        entry.grid(column=1, row=self.row, sticky=(W, E))
        
        # Cria a Label e atribui qual vai ser o pai, o texto, e o local aonde ela vai ficar no Grid
        ttk.Label(self.parent, text=label_text).grid(column=0, row=self.row, sticky=W)
        
        self.row += 1  # Incrementa a Row pra se preparar pro próximo campo
        return entry
    
    def add_button(self, label, command, column=3):
        """Adiciona o Button"""
        btn = ttk.Button(self.parent, text=label, command=command)
        btn.grid(column=column, row=self.row, sticky=W)
        return btn
    
    def apply_padding(self, padx=5, pady=5):
        """Itera entre todos os Widgets criados, pra aplicar um padding em todos os filhos da moldura pai"""
        for child in self.parent.winfo_children():
            child.grid_configure(padx=padx, pady=pady)
    
    def build_form(self):
        """Constrói todos os campos e aplica todos os métodos da classe FormBuilder"""
        # Adiciona todos os campos
        nome_social_entry = self.add_text_field("Nome Social", "NOME_SOCIAL")
        self.add_text_field("Data por Extenso", "DATA_POR_EXTENSO")
        self.add_text_field("Nome do Segurado", "NOME_DO_SEGURADO")
        self.add_text_field("Data Admissão", "DATA_ADMISSAO")
        self.add_text_field("Data Demissão", "DATA_DEMISSAO")
        self.add_text_field("Endereço Segurado", "ENDERECO_SEGURADO")
        self.add_text_field("Bairro Segurado", "BAIRRO_SEGURADO")
        self.add_text_field("Cidade Segurado", "CIDADE_SEGURADO")
        self.add_text_field("UF Segurado", "UF_SEGURADO")
        self.add_text_field("CEP Segurado", "CEP_SEGURADO")
        self.add_text_field("Telefone Segurado", "TELEFONE_SEGURADO")
        self.add_text_field("Nome Advogado", "NOME_ADVOGADO")
        self.add_text_field("OAB Advogado", "OAB_ADVOGADO")
        
        # Adicionar o botão de gerar o documento .docx
        self.add_button("Gerar", self.app.gerar)
        
        # Aplica o padding em todos os Widgets
        self.apply_padding()
        
        return nome_social_entry  # Retorna o primeiro widget pra ser o foco do cursor (preciso modificar isso pra ele entender automaticamente qual seria o primeiro)