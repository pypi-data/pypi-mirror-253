def calcular_ttpa(tempo_tromboplastina, saida='advanced'):
    """
    Calcula o Tempo de Tromboplastina Parcial Ativada (TTPA) e fornece uma classificação opcional.

    Attributes:
        tempo_tromboplastina (float): Tempo de Tromboplastina Parcial Ativada em segundos.
        saida (str): Tipo de saída desejado ('advanced' para detalhes completos ou 'simple' para classificação simplificada).
                     Padrão é 'advanced'.

    Returns:
        float or tuple: Resultado do TTPA. Se saida='simple', retorna apenas o resultado. Se saida='advanced',
                        retorna o resultado e uma classificação opcional.
    """

    # Definir faixas de referência
    referencia_muito_baixa = 24.0  # Muito baixo em segundos
    referencia_baixa = (24.0, 26.0)  # Baixo em segundos
    referencia_normal = (26.0, 35.0)  # Normal em segundos
    referencia_alta = (35.0, 36.0)  # Alto em segundos
    referencia_muito_alta = 36.0  # Muito alto em segundos


    classificacao = None
    if tempo_tromboplastina < referencia_muito_baixa:
        classificacao = "Muito baixo"
    elif referencia_muito_baixa <= tempo_tromboplastina < referencia_baixa[0]:
        classificacao = "Baixo"
    elif referencia_baixa[0] <= tempo_tromboplastina <= referencia_baixa[1]:
        classificacao = "Baixo"
    elif referencia_baixa[1] < tempo_tromboplastina < referencia_normal[0]:
        classificacao = "Baixo"
    elif referencia_normal[0] <= tempo_tromboplastina < referencia_normal[1]:
        classificacao = "Normal"
    elif referencia_normal[1] <= tempo_tromboplastina < referencia_alta[0]:
        classificacao = "Alto"
    elif referencia_alta[0] <= tempo_tromboplastina < referencia_alta[1]:
        classificacao = "Alto"
    else:
        classificacao = "Muito alto"


    if saida == 'simple':
        return classificacao
    else:
        return tempo_tromboplastina



