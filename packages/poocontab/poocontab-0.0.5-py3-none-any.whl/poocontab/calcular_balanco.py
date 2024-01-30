def calcular_balanco(ativos, passivos, periodo):
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



