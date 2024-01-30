def teste_capacidade_anaerobica(tempo_em_minutos):
    """
    Avalia a capacidade anaeróbica com base no tempo de realização do teste de correr 1 km.

    Attributes:
        tempo_em_minutos (float): Tempo em minutos que a pessoa levou para realizar o teste.

    Returns:
        str: Classificação do desempenho (muito baixo, baixo, normal, alto, muito alto).
    """

    if tempo_em_minutos < 8:
        return "Excelente"
    elif 8 <= tempo_em_minutos < 10:
        return "Bom"
    elif 10 <= tempo_em_minutos < 12:
        return "normal"
    elif 12 <= tempo_em_minutos < 14:
        return "Lento"
    else:
        return "Muito Lento"

