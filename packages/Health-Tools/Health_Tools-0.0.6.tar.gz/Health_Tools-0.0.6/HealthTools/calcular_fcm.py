def calcular_fcm(idade, sexo,saida='simple'):
    """
    Calcula a Frequência Cardíaca Máxima (FCM) com base na idade e sexo.

    Attributes:
        idade (int): Idade da pessoa.
        sexo (str): Sexo da pessoa, pode ser 'masculino' ou 'feminino'.

    Returns:
        tuple: Uma tupla contendo a Frequência Cardíaca Máxima (FCM) e sua categoria de intensidade.
            O primeiro elemento é a Frequência Cardíaca Máxima (FCM) calculada.
            O segundo elemento é uma string representando a categoria de intensidade, que pode ser:
                - 'muito baixa': se a FCM estiver abaixo de 50% da FCM máxima esperada para a idade,
                - 'baixa': se a FCM estiver entre 50% e 60% da FCM máxima esperada para a idade,
                - 'normal': se a FCM estiver entre 60% e 70% da FCM máxima esperada para a idade,
                - 'alta': se a FCM estiver entre 70% e 80% da FCM máxima esperada para a idade,
                - 'muito alta': se a FCM estiver acima de 80% da FCM máxima esperada para a idade.
    """
    fcm = 220 - idade
    if sexo.lower() == 'masculino':
        referencia_muito_baixa = 0.5 * fcm
        referencia_baixa = 0.65 * fcm
        referencia_normal = 0.85 * fcm
        referencia_alta = 1.0 * fcm
        referencia_muito_alta = 1.15 * fcm
    elif sexo.lower() == 'feminino':
        referencia_muito_baixa = 0.55 * fcm
        referencia_baixa = 0.7 * fcm
        referencia_normal = 0.9 * fcm
        referencia_alta = 1.05 * fcm
        referencia_muito_alta = 1.2 * fcm
    else:
        return "Sexo não reconhecido"

    if fcm < referencia_muito_baixa:
        if saida == 'simple':
            return "Muito baixa"
        return fcm
    elif referencia_muito_baixa <= fcm < referencia_baixa:
        if saida == 'simple':
            return "Baixa"
        return fcm
    elif referencia_baixa <= fcm < referencia_normal:
        if saida == 'simple':
            return "Normal"
        return fcm
    elif referencia_normal <= fcm < referencia_alta:
        if saida == 'simple':
            return "Alta"
        return fcm
    elif referencia_alta <= fcm < referencia_muito_alta:
        if saida == 'simple':
            return "Muito alta"
        return fcm
    else:
        return fcm, "Valores extremamente altos para a idade"
