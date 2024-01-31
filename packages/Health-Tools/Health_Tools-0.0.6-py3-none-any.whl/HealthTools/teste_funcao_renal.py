def teste_funcao_renal(creatinina, ureia, saida):
    """
    Avalia a saúde dos rins com base nos níveis de creatinina e ureia no sangue.

    Attributes:
        creatinina (float): Nível de creatinina no sangue em mg/dL.
        ureia (float): Nível de ureia no sangue em mg/dL.
        saida (str): Tipo de saída desejado ('advanced' para detalhado ou 'simple' para resumido).

    Returns:
        dict or str: Se 'saida' for 'advanced', retorna um dicionário com os resultados detalhados.
                     Se 'saida' for 'simple', retorna uma classificação simplificada da função renal.
    """

    limite_superior_creatinina = 1.2  # mg/dL
    limite_superior_ureia = 40  # mg/dL


    if creatinina <= limite_superior_creatinina and ureia <= limite_superior_ureia:
        if saida == 'simple':
            return {'resultado': 'Normal', 'detalhes': 'A função renal está dentro dos limites normais.'}
        elif saida == 'advanced':
            return 'Normal'
    elif creatinina > limite_superior_creatinina or ureia > limite_superior_ureia:
        if saida == 'simple':
            return {'resultado': 'Anormal', 'detalhes': 'A função renal está alterada. Consulte um médico.'}
        elif saida == 'advanced':
            return 'Anormal'
