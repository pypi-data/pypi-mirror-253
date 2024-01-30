from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF
def calcularbalanco(ativos, passivos, periodo):
    
    # Inicializando o patrimônio líquido
    patrimonio_liquido = {}

    # Para cada mês no período
    for mes in periodo:
        # Calculando o total de ativos e passivos para o mês
        total_ativos = sum(ativos[mes].values())
        total_passivos = sum(passivos[mes].values())

        # Calculando o patrimônio líquido para o mês
        patrimonio_liquido[mes] = total_ativos - total_passivos

    return patrimonio_liquido


'''ativos = {
    'janeiro': {'ativo_circulante': 10000, 'ativo_nao_circulante': 20000},
    'fevereiro': {'ativo_circulante': 15000, 'ativo_nao_circulante': 25000},
    # ...
}

passivos = {
    'janeiro': {'passivo_circulante': 5000, 'passivo_nao_circulante': 15000},
    'fevereiro': {'passivo_circulante': 6000, 'passivo_nao_circulante': 16000},
    # ...
}

periodo = ['janeiro', 'fevereiro', # ... 
]

patrimonio = calcular_balanco(ativos, passivos, periodo)

print(patrimonio)'''
multa_fgts = 0
aviso_previo = 0
decimo_terceiro = 0
ferias_proporcionais = 0


def rescisao_sem_justa_causa(salario, tempo_de_servico):

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # multa do FGTS é de 40% do saldo do FGTS
    multa_fgts = fgts * 0.4

    # aviso prévio indenizado é um salário
    aviso_previo = salario

    # decimo terceiro salário proporcional
    decimo_terceiro = (salario / 12) * tempo_de_servico

    # ferias proporcionais
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + multa_fgts + aviso_previo + \
        decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_justa_causa(salario, tempo_de_servico):

    # no caso de justa causa, o funcionário não tem direito a multa do FGTS, aviso prévio e décimo terceiro

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    valor_rescisao = fgts
    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_aposentadoria(salario, tempo_de_servico):
    # Inicializando as variáveis

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de aposentadoria, o funcionário tem direito ao FGTS, mas não à multa do FGTS
    # aviso prévio e décimo terceiro são calculados normalmente
    aviso_previo = salario
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + aviso_previo + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_falecimento(salario, tempo_de_servico):

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de falecimento, os dependentes têm direito ao FGTS, sem multa
    # aviso prévio, décimo terceiro e férias são calculados normalmente
    aviso_previo = salario
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + aviso_previo + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_demissao(salario, tempo_de_servico):

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de pedido de demissão, o funcionário não tem direito a multa do FGTS nem aviso prévio indenizado
    # décimo terceiro e férias são calculados normalmente
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_termino_de_contrato_por_experiencia(salario, tempo_de_servico):
    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de término de contrato de experiência, o funcionário não tem direito a multa do FGTS nem aviso prévio indenizado
    # décimo terceiro e férias são calculados normalmente
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def gerar_pdf_rescisao(nome, cpf, razaosocial, cnpj, tempodeservico, salario, causadoafastamento, multafgts, avisoprevio, decimoterceiro,
                       ferias_proporcionais, diadarescisao, valor_rescisao, file_name):
    # Dados da rescisão
    data = [
        ['Nome do Funcionário', nome],
        ['CPF', cpf],
        ['Razão Social da Empresa', razaosocial],
        ['CNPJ', cnpj],
        ['Tempo de Serviço', tempodeservico],
        ['Dia da Rescisão', diadarescisao],
        ['Causa do Afastamento', causadoafastamento],
        ['Salário', 'R$ ' + salario],
        ['Multa FGTS', 'R$ ' + multafgts],
        ['Aviso Prévio', 'R$ ' + avisoprevio],
        ['Décimo Terceiro', 'R$ ' + decimoterceiro],
        ['Férias Proporcionais', 'R$ ' + ferias_proporcionais],
        ['Valor da Rescisão', 'R$ ' + valor_rescisao],
    ]

    # Criar o documento PDF
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    # Cabeçalho
    from reportlab.platypus import Paragraph

    # Cabeçalho
    header = "TERMO DE RESCISÃO DO CONTRATO DE TRABALHO"
    elements.append(header)



    # Adicionar os dados da rescisão à tabela
    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Adicionar os dados da rescisão à tabela
    t = Table(data)
    t.setStyle(table_style)
    elements.append(t)

    # Adicionar as assinaturas
    elements.append("Assinatura do Funcionário: ________________________")
    elements.append("Assinatura do Empregador: ________________________")

    doc.build(elements)


# Exemplo de chamada da função
gerar_pdf_rescisao("João Silva", "123.456.789-00", "Empresa XYZ LTDA", "12.345.678/0001-90", "5 anos", "5000.00",
                   "Rescisão sem justa causa", "1000.00", "2000.00", "3000.00", "250.00", "01/01/2024", "7000.00",
                   "termo_de_rescisao.pdf")

def gerar_pdf_balanco(ativos, passivos, periodo, file_name):
    # Preparar os dados para o balanço patrimonial
    data = []
    patrimonio_liquido_total = 0
    for mes in periodo:
        ativo_circulante = ativos[mes]['ativo_circulante']
        ativo_nao_circulante = ativos[mes]['ativo_nao_circulante']
        passivo_circulante = passivos[mes]['passivo_circulante']
        passivo_nao_circulante = passivos[mes]['passivo_nao_circulante']
        patrimonio_liquido = ativo_circulante + ativo_nao_circulante - \
            passivo_circulante - passivo_nao_circulante
        patrimonio_liquido_total += patrimonio_liquido

        data.append([f"Ativo Circulante ({mes})", f"R$ {ativo_circulante}"])
        data.append(
            [f"Ativo Não Circulante ({mes})", f"R$ {ativo_nao_circulante}"])
        data.append(
            [f"Passivo Circulante ({mes})", f"R$ {passivo_circulante}"])
        data.append(
            [f"Passivo Não Circulante ({mes})", f"R$ {passivo_nao_circulante}"])
        data.append(
            [f"Patrimônio Líquido ({mes})", f"R$ {patrimonio_liquido}"])
        data.append(["", ""])  # Adicionar linha em branco entre os meses

    data.append(["Patrimônio Líquido Total", f"R$ {patrimonio_liquido_total}"])

    # Criar o documento PDF do balanço patrimonial
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    # Cabeçalho
    header = "BALANÇO PATRIMONIAL"
    elements.append(header)

    # Definir o estilo da tabela
    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Adicionar os dados do balanço patrimonial à tabela
    t = Table(data)
    t.setStyle(table_style)  # Aplicar o estilo à tabela
    elements.append(t)

    doc.build(elements)


# Exemplo de chamada das funções
ativos = {
    'janeiro': {'ativo_circulante': 10000, 'ativo_nao_circulante': 20000},
    'fevereiro': {'ativo_circulante': 15000, 'ativo_nao_circulante': 25000},
    # ...
}

passivos = {
    'janeiro': {'passivo_circulante': 5000, 'passivo_nao_circulante': 15000},
    'fevereiro': {'passivo_circulante': 6000, 'passivo_nao_circulante': 16000},
    # ...
}

periodo = ['janeiro', 'fevereiro',  ...]

# Gerar PDF de rescisão
gerar_pdf_rescisao("João Silva", "123.456.789-00", "Empresa XYZ LTDA", "12.345.678/0001-90", "5 anos", "5000.00",
                   "Rescisão sem justa causa", "1000.00", "2000.00", "3000.00", "250.00", "01/01/2024", "7000.00",
                   "termo_de_rescisao.pdf")

# Gerar PDF de balanço patrimonial
gerar_pdf_balanco(ativos, passivos, periodo, "balanco_patrimonial.pdf")
