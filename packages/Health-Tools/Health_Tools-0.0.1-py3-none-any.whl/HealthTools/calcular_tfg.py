def calcular_tfg(creatinina_serica, idade, sexo='masculino', raca='não negra', output='ml/min/1.73m^2'):
    """
    Calcula a Taxa de Filtração Glomerular (TFG) utilizando a fórmula do MDRD.

    Attributes:
        creatinina_serica (float): Valor da creatinina sérica em mg/dL.
        idade (int): Idade do paciente em anos.
        sexo (str): Sexo do paciente ('masculino' ou 'feminino'). Padrão é masculino.
        raca (str): Raça do paciente ('negra' ou 'não negra'). Padrão é não negra.
        output (str): Tipo de saída desejado ('ml/min/1.73m^2' ou 'ml/min'). Padrão é ml/min/1.73m^2.

    Returns:
        float: Valor da TFG calculada.
    """

    if sexo.lower() == 'feminino':
        fator_sexo = 0.742
    else:
        fator_sexo = 1

    if raca.lower() == 'negra':
        fator_raca = 1.212
    else:
        fator_raca = 1


    tfg = 175 * (creatinina_serica ** (-1.154)) * (idade ** (-0.203)) * fator_sexo * fator_raca


    if output == 'ml/min':
        return tfg
    elif output == 'ml/min/1.73m^2':

        superficie_corporal = 1.73  # Média para adultos
        tfg_corrigida = tfg * superficie_corporal
        return tfg_corrigida
    else:
        return "Opção de saída inválida"



