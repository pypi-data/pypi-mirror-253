import matplotlib.pyplot as plt
import seaborn as sns

def gerargraficorescisao(multafgts, avisoprevio, decimoterceiro, ferias_proporcionais, valor_rescisao):
    '''Este metodo gera um grafico de barras com os valores da rescisao.
    
    ...
    
    Atributtes:
    
    multafgts: float
        Valor da multa do FGTS do funcionario.
    avisoprevio: float
        Valor do aviso previo do funcionario.
    decimoterceiro: float
        Valor do decimo terceiro do funcionario.
    ferias_proporcionais: float
        Valor das ferias proporcionais do funcionario.
    valor_rescisao: float
        Valor da rescisao do funcionario.
    
    '''
    # Cria uma lista com os nomes dos componentes da rescisão
    componentes = ['Multa FGTS', 'Aviso Prévio',
                   'Décimo Terceiro', 'Férias Proporcionais', 'Valor Rescisão']

    # Cria uma lista com os valores correspondentes
    valores = [multafgts, avisoprevio, decimoterceiro,
               ferias_proporcionais, valor_rescisao]

    # Define o estilo do gráfico usando seaborn
    sns.set(style="whitegrid")

    # Cria uma figura e um conjunto de subtramas
    fig, ax = plt.subplots()

    # Cria o gráfico de barras
    ax = sns.barplot(x=componentes, y=valores, hue=componentes, palette="viridis",legend=False)

    # Adiciona rótulos e título
    ax.set_title('Valores da Rescisão')
    ax.set_xlabel('Componentes')
    ax.set_ylabel('Valores')

    # Rotaciona os rótulos do eixo x para evitar sobreposição
    plt.xticks(rotation=45)

    # Ajusta a largura das barras para evitar sobreposição
    plt.tight_layout()

    # Salva a figura como uma imagem
    fig.savefig('rescisao.png')

    # Fecha a figura
    plt.close(fig)


def gerargraficopatrimonio(patrimonio_liquido):
    '''
    Este método gera um gráfico de linha com a evolução do patrimônio líquido ao longo do tempo.
    
    ...
    
    Atributtes:
    
    patrimonio_liquido: dict
        Dicionário com os valores do patrimônio líquido ao longo do tempo.
    
    '''
    # Criando listas para os meses e os valores do patrimônio líquido
    meses = list(patrimonio_liquido.keys())
    valores = list(patrimonio_liquido.values())

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(meses, valores, marker='o')

    # Adicionando títulos e rótulos
    plt.title('Evolução do Patrimônio Líquido ao Longo do Tempo')
    plt.xlabel('Mês')
    plt.ylabel('Patrimônio Líquido')

    # Salvando o gráfico como uma imagem
    plt.savefig('patrimonio_liquido.png')
