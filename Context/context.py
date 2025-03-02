# Classe para lidar com o contexto do template
class TemplateContext:
	
	@staticmethod
	def get_context(app_instance):
		'''Pega o dicionário do contexto da instância do app

		Parâmetros:
			app_instance: Instância da classe AutoOficio

		Retorna:
			"dictionary": O dicionário do contexto da aplicação'''
						
		return {
			'NOME_SOCIAL': app_instance.NOME_SOCIAL.get(),
			'DATA_POR_EXTENSO': app_instance.DATA_POR_EXTENSO.get(),
			'NOME_DO_SEGURADO': app_instance.NOME_DO_SEGURADO.get(),
			'DATA_ADMISSÃO': app_instance.DATA_ADMISSAO.get(),
			'DATA_DEMISSÃO': app_instance.DATA_DEMISSAO.get(),
			'ENDEREÇO_SEGURADO': app_instance.ENDERECO_SEGURADO.get(),
			'BAIRRO_SEGURADO': app_instance.BAIRRO_SEGURADO.get(),
			'CIDADE_SEGURADO': app_instance.CIDADE_SEGURADO.get(),
			'UF_SEGURADO': app_instance.UF_SEGURADO.get(),
			'CEP_SEGURADO': app_instance.CEP_SEGURADO.get(),
			'TELEFONE_SEGURADO': app_instance.TELEFONE_SEGURADO.get(),
			'NOME_ADVOGADO': app_instance.NOME_ADVOGADO.get(),
			'OAB_ADVOGADO': app_instance.OAB_ADVOGADO.get()
		}
