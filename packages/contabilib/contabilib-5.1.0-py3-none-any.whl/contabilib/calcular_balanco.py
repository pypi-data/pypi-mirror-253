def calcularbalanco(ativos, passivos, periodo):
    
    '''Este metodo calcula o balanco patrimonial de uma empresa.
    
    ...
    
    Atributtes: 
    
    ativos: dict
        Dicionario contendo os ativos da empresa.
    passivos: dict
        Dicionario contendo os passivos da empresa.
    periodo: list
        Lista contendo os meses do periodo.
        
    Returns:
    
        patrimonio_liquido: dict
            Dicionario contendo o patrimonio liquido da empresa.
            
    '''
    
    patrimonio_liquido = {}# Inicializando o patrimônio líquido

    # Para cada mês no período
    for mes in periodo:
        # Calculando o total de ativos e passivos para o mês
        total_ativos = sum(ativos[mes].values())
        total_passivos = sum(passivos[mes].values())

        # Calculando o patrimônio líquido para o mês
        patrimonio_liquido[mes] = total_ativos - total_passivos

    return patrimonio_liquido
