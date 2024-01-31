def calcular_debito_urinario(volume_urina_Litro, tempo_Hora,saida):
    """
    Calcula o débito urinário e fornece uma classificação.

    Attributes:
        volume_urina (float): Volume de urina produzido em mililitros.
        tempo (float): Tempo decorrido para a produção de urina em minutos.

    Returns:
        tuple: Uma tupla contendo o débito urinário calculado em mililitros por minuto e sua classificação.
            O primeiro elemento é o débito urinário calculado.
            O segundo elemento é uma string representando a classificação do débito urinário, que pode ser:
                - 'muito baixo': se o débito urinário for menor que 0.5 ml/min,
                - 'baixo': se o débito urinário estiver entre 0.5 e 1.0 ml/min,
                - 'normal': se o débito urinário estiver entre 1.0 e 2.0 ml/min,
                - 'alto': se o débito urinário estiver entre 2.0 e 3.0 ml/min,
                - 'muito alto': se o débito urinário for maior que 3.0 ml/min.
    """

    if tempo_Hora <= 0:
        return "Tempo inválido", "Classificação indeterminada"


    if volume_urina_Litro < 0:
        return "Volume de urina inválido", "Classificação indeterminada"


    debito_urinario = volume_urina_Litro / tempo_Hora

    # Classificar a produção de urina
    if debito_urinario < 0.5:
        classificacao = "Produção de urina muito baixa"
    elif 0.5 <= debito_urinario < 1.5:
        classificacao = "Produção de urina baixa"
    elif 1.5 <= debito_urinario < 2.5:
        classificacao = "Produção de urina normal"
    else:
        classificacao = "Produção de urina muito alta"
    if saida == "simple":
        return debito_urinario, classificacao

    return debito_urinario
