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
