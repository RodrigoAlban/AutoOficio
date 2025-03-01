from docxtpl import DocxTemplate

# Carrega o template .docx
doc = DocxTemplate("my_word_template.docx")

# Cria o contexto, procurando as variáveis para substituir
context = {
     'NOME_SOCIAL' : "FRIMESA" ,
     'NOME_DO_SEGURADO' : "RODRIGO ALBAN",
     'DATA_POR_EXTENSO' : "01 de março de 2025",
     'NOME_ADVOGADO' : "Dr. Auzio",
     'DATA_ADMISSÃO' : "01/01/1999",
     'DATA_DEMISSÃO' : "",
     'ENDEREÇO_SEGURADO' : "Avenida Brasil, 1010",
     'BAIRRO_SEGURADO' : "Centro",
     'CIDADE_SEGURADO' : "Medianeira",
     'UF_SEGURADO' : "Paraná",
     'CEP_SEGURADO' : "85884-000",
     'TELEFONE_SEGURADO' : "45 9999-9999",
     'OAB_ADVOGADO' : "123.456"
    }

# Substitui as variáveis do template .docx e cria um novo .docx
doc.render(context)
doc.save("generated_doc.docx")