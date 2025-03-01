from docxtpl import DocxTemplate

# Carrega o template .docx
doc = DocxTemplate("my_word_template.docx")

# Cria o contexto, procurando as variáveis para substituir
context = {
     'NOME_SOCIAL' : "FRIMESA"
    }

# Substitui as variáveis do .docx e cria um novo .docx
doc.render(context)
doc.save("generated_doc.docx")