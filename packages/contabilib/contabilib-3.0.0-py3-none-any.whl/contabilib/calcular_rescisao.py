multa_fgts = 0
aviso_previo = 0
decimo_terceiro = 0
ferias_proporcionais = 0


def rescisao_sem_justa_causa(salario, tempo_de_servico):
    '''Este metodo calcula a rescisao de um funcionario sem justa causa.
    
    ...
    
    Atributtes:
    
    salario: float
        Salario do funcionario.
    tempo_de_servico: int
        Tempo de servico do funcionario.
        
    Returns:
    
        valor_rescisao: float
            Valor da rescisao do funcionario.
        fgts: float
            Valor do FGTS do funcionario.
        multa_fgts: float
            Valor da multa do FGTS do funcionario.
        aviso_previo: float
            Valor do aviso previo do funcionario.
        decimo_terceiro: float
            Valor do decimo terceiro do funcionario.
        ferias_proporcionais: float
            Valor das ferias proporcionais do funcionario.
            
'''

    # calculo do FGTS
    fgts = salario * 0.08 * (tempo_de_servico / 12)

    # multa do FGTS é de 40% do saldo do FGTS
    multa_fgts = fgts * 0.4

    # aviso prévio indenizado é um salário
    aviso_previo = salario

    # decimo terceiro salário proporcional
    decimo_terceiro = (salario / 12) * (tempo_de_servico / 12)

    # ferias proporcionais
    ferias_proporcionais = (salario / 12) * (tempo_de_servico / 12)

    valor_rescisao = fgts + multa_fgts + aviso_previo + \
        decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_justa_causa(salario, tempo_de_servico):
    '''Este metodo calcula a rescisao de um funcionario com justa causa.
    
    ...
    
    Atributtes:
    
    salario: float
        Salario do funcionario.
    tempo_de_servico: int
        Tempo de servico do funcionario.
    
    Returns:
    
        valor_rescisao: float
            Valor da rescisao do funcionario.
        fgts: float
            Valor do FGTS do funcionario.
            
    '''

    # no caso de justa causa, o funcionário não tem direito a multa do FGTS, aviso prévio e décimo terceiro

    # calculo do FGTS
    fgts = salario * 0.08 * (tempo_de_servico / 12)

    valor_rescisao = fgts
    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_aposentadoria(salario, tempo_de_servico):
    '''Este metodo calcula a rescisao de um funcionario por aposentadoria.
    
    ...
    
    Atributtes:
    
    salario: float
        Salario do funcionario.
    tempo_de_servico: int
        Tempo de servico do funcionario.
        
    Returns:
    
        valor_rescisao: float
            Valor da rescisao do funcionario.
        fgts: float
            Valor do FGTS do funcionario.
        multa_fgts: float
            Valor da multa do FGTS do funcionario.
        aviso_previo: float
            Valor do aviso previo do funcionario.
        decimo_terceiro: float
            Valor do decimo terceiro do funcionario.
        ferias_proporcionais: float
            Valor das ferias proporcionais do funcionario.
            
    '''
    # Inicializando as variáveis

    # calculo do FGTS
    fgts = salario * 0.08 * (tempo_de_servico / 12)

    # no caso de aposentadoria, o funcionário tem direito ao FGTS, mas não à multa do FGTS
    # aviso prévio e décimo terceiro são calculados normalmente
    aviso_previo = salario
    decimo_terceiro = (salario / 12) * (tempo_de_servico / 12)

    ferias_proporcionais = (salario / 12) * (tempo_de_servico / 12)

    valor_rescisao = fgts + aviso_previo + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_falecimento(salario, tempo_de_servico):
    '''Este metodo calcula a rescisao de um funcionario por falecimento.
    
    ...
    
    Atributtes:
        salario: float
            Salario do funcionario.
        tempo_de_servico: int
            Tempo de servico do funcionario.
        
    
    Returns:
            
        valor_rescisao: float
            Valor da rescisao do funcionario.
        fgts: float
            Valor do FGTS do funcionario.
        multa_fgts: float
            Valor da multa do FGTS do funcionario.
        aviso_previo: float
            Valor do aviso previo do funcionario.
        decimo_terceiro: float
            Valor do decimo terceiro do funcionario.
        ferias_proporcionais: float
            Valor das ferias proporcionais do funcionario.'''

    fgts = salario * 0.08 * (tempo_de_servico / 12)

    # no caso de falecimento, os dependentes têm direito ao FGTS, sem multa
    # aviso prévio, décimo terceiro e férias são calculados normalmente
    aviso_previo = salario
    decimo_terceiro = (salario / 12) * (tempo_de_servico / 12)

    ferias_proporcionais = (salario / 12) * (tempo_de_servico / 12)

    valor_rescisao = fgts + aviso_previo + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_demissao(salario, tempo_de_servico):
    '''Este metodo calcula a rescisao de um funcionario por demissao.
    
    ...
    
    Atributtes:
            
        salario: float
            Salario do funcionario.
        tempo_de_servico: int
            Tempo de servico do funcionario.
            
    Returns:
            
        valor_rescisao: float
            Valor da rescisao do funcionario.
        fgts: float
            Valor do FGTS do funcionario.
        decimo_terceiro: float
            Valor do decimo terceiro do funcionario.
        ferias_proporcionais: float
            Valor das ferias proporcionais do funcionario.'''

    # calculo do FGTS
    fgts = salario * 0.08 * (tempo_de_servico / 12)

    # no caso de pedido de demissão, o funcionário não tem direito a multa do FGTS nem aviso prévio indenizado
    # décimo terceiro e férias são calculados normalmente
    decimo_terceiro = (salario / 12) * (tempo_de_servico / 12)

    ferias_proporcionais = (salario / 12) * (tempo_de_servico / 12)

    valor_rescisao = fgts + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_termino_de_contrato_por_experiencia(salario, tempo_de_servico):
    '''Este metodo calcula a rescisao de um funcionario por termino de contrato de experiencia.
    
    ...
    
    Atributtes:
    
        salario: float 
            Salario do funcionario.
        tempo_de_servico: int
            Tempo de servico do funcionario.
            
    Returns:
            
        valor_rescisao: float
            Valor da rescisao do funcionario.
        fgts: float
            Valor do FGTS do funcionario.
        decimo_terceiro: float
            Valor do decimo terceiro do funcionario.
        ferias_proporcionais: float
            Valor das ferias proporcionais do funcionario.
            
    '''
    # calculo do FGTS
    fgts = salario * 0.08 * (tempo_de_servico / 12)

    # no caso de término de contrato de experiência, o funcionário não tem direito a multa do FGTS nem aviso prévio indenizado
    # décimo terceiro e férias são calculados normalmente
    decimo_terceiro = (salario / 12) * (tempo_de_servico / 12)

    ferias_proporcionais = (salario / 12) * (tempo_de_servico / 12)

    valor_rescisao = fgts + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais
