def classificar_apgar(nota):
    """
    Classifica a nota do Índice de Apgar em termos de saúde do recém-nascido.

    Attributes:
        nota (int): Nota de 0 a 5 referente a um aspecto do Índice de Apgar.

    Returns:
        str: Classificação da nota em termos de saúde do recém-nascido.
    """
    if nota <= 1:
        return "muito baixa"
    elif 1 < nota <= 3:
        return "baixa"
    elif 3 < nota <= 4:
        return "aceitável"
    else:
        return "ótimo"


def calcular_indice_apgar(cor, frequencia_cardiaca, respiracao, tonus_muscular, reflexos,saida):
    """
    Calcula o Índice de Apgar com base nos critérios fornecidos.

    Attributes:
        cor (int): Nota de 0 a 5 referente à cor da pele.
        frequencia_cardiaca (int): Nota de 0 a 5 referente à frequência cardíaca.
        respiracao (int): Nota de 0 a 5 referente à respiração.
        tonus_muscular (int): Nota de 0 a 5 referente ao tônus muscular.
        reflexos (int): Nota de 0 a 5 referente aos reflexos.

    Returns:
        int: Índice de Apgar total, representando a saúde do recém-nascido no momento do nascimento.
    """
    cor = min(cor, 5)
    frequencia_cardiaca = min(frequencia_cardiaca, 5)
    respiracao = min(respiracao, 5)
    tonus_muscular = min(tonus_muscular, 5)
    reflexos = min(reflexos, 5)

    indice_apgar = (cor + frequencia_cardiaca + respiracao + tonus_muscular + reflexos) / 5
    if saida == "simple":
        return classificar_apgar(indice_apgar)

    else:
        return indice_apgar
