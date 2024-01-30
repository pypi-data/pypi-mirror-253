def calcular_debito_cardiaco(fc, vs, saida='advanced'):
    """
       Calcula o Débito Cardíaco (DC) com base na frequência cardíaca (FC) e no volume sistólico (VS).

       Parameters:
           fc (float): Frequência cardíaca (batimentos por minuto).
           vs (float): Volume sistólico (mililitros por batimento).
           saida (str, opcional): Tipo de saída desejado ('advanced' para apenas o resultado, 'simple' para resultado e classificação).

       Returns:
           float or tuple: Débito Cardíaco (mililitros por minuto) ou (Débito Cardíaco, Classificação) dependendo da saída escolhida.
       """
    dc = fc * vs

    if saida == 'simple':
        if dc < 4000:
            classificacao = "Muito baixo"
        elif 4000 <= dc < 5000:
            classificacao = "Baixo"
        elif 5000 <= dc < 6000:
            classificacao = "Normal"
        elif 6000 <= dc < 7000:
            classificacao = "Alto"
        else:
            classificacao = "Muito alto"
        return dc, classificacao
    else:
        return dc
