import matplotlib.pyplot as plt
import seaborn as sns

multafgts = 100
avisoprevio = 200
decimoterceiro = 10
ferias_proporcionais = 300
valor_rescisao = 20


def gerargraficorescisao(multafgts, avisoprevio, decimoterceiro, ferias_proporcionais, valor_rescisao):
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
    ax = sns.barplot(x=componentes, y=valores, palette="viridis")

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
