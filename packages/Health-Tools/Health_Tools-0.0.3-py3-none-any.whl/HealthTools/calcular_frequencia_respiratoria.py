def calcular_frequencia_respiratoria(fr, idade):
    """
    Calcula a frequência respiratória e determina em qual categoria se enquadra.

    Attributes:
        fr (int): Frequência respiratória (número de respirações por minuto).
        idade (int): Idade do indivíduo.

    Returns:
        str: Categoria da frequência respiratória, que pode ser:
            - 'muito baixa': se a frequência respiratória estiver significativamente abaixo da média para a idade,
            - 'baixa': se a frequência respiratória estiver abaixo da média para a idade,
            - 'normal': se a frequência respiratória estiver dentro da faixa considerada normal para a idade,
            - 'alta': se a frequência respiratória estiver acima da média para a idade,
            - 'muito alta': se a frequência respiratória estiver significativamente acima da média para a idade.
    """
    if idade < 1:
        if 30 <= fr <= 60:
            return "normal"
        elif fr < 30:
            return "muito baixa"
        else:
            return "muito alta"
    elif 1 <= idade <= 5:
        if 20 <= fr <= 30:
            return "normal"
        elif fr < 20:
            return "muito baixa"
        else:
            return "muito alta"
    elif 6 <= idade <= 12:
        if 15 <= fr <= 25:
            return "normal"
        elif fr < 15:
            return "muito baixa"
        else:
            return "muito alta"
    elif idade > 12:
        if 12 <= fr <= 20:
            return "normal"
        elif fr < 12:
            return "muito baixa"
        else:
            return "muito alta"


