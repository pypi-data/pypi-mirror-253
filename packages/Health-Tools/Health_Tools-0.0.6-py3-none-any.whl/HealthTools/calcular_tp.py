def calcular_tp(tempo_protrombina, saida='advanced'):
    """
    Calcula o Tempo de Protrombina (TP) e fornece uma classificação opcional.

    Attributes:
        tempo_protrombina (float): Tempo de Protrombina em segundos.
        saida (str): Tipo de saída desejado ('advanced' para detalhes completos ou 'simple' para classificação simplificada).
                     Padrão é 'advanced'.

    Returns:
        float or tuple: Resultado do TP. Se saida='simple', retorna apenas o resultado. Se saida='advanced',
                        retorna o resultado e uma classificação opcional.
    """

    # Definir faixas de referência
    referencia_normal = (11.0, 13.0)
    referencia_baixa = 10.0
    referencia_alta = 14.0


    classificacao = None
    if tempo_protrombina < referencia_baixa:
        classificacao = "Muito baixo"
    elif referencia_baixa <= tempo_protrombina < referencia_normal[0]:
        classificacao = "Baixo"
    elif referencia_normal[0] <= tempo_protrombina <= referencia_normal[1]:
        classificacao = "Normal"
    elif referencia_normal[1] < tempo_protrombina < referencia_alta:
        classificacao = "Alto"
    else:
        classificacao = "Muito alto"

    # Retornar resultado conforme o tipo de saída
    if saida == 'simple':
        return classificacao
    else:
        return tempo_protrombina, classificacao



