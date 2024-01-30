def contar_leucocitos(numero_leucocitos,saida):
    """
    Conta o número de glóbulos brancos no sangue e retorna uma métrica de 0 a 25.

    Attributes:
        numero_leucocitos (float): Número de glóbulos brancos em milhares por microlitro (milhares/µL).
        saida (str): Define o tipo de saída desejada ('simple' para uma classificação simplificada).

    Returns:
        float: Métrica de 0 a 25 representando o número de glóbulos brancos.
    """

    if numero_leucocitos == 0:
        return "Taxa de leucócitos inválida"

    if saida == None:
        saida = "advanced"

    referencia_baixa = 4.0  # Milhares/µL
    referencia_media_baixa = 5.0
    referencia_media = 7.0
    referencia_media_alta = 9.0
    referencia_alta = 11.0
    referencia_muito_alta = 15.0
    referencia_extremamente_alta = 20.0


    if numero_leucocitos < referencia_baixa:
        if saida == "simple":
            print("Extremamente baixa")
        return 0

    elif referencia_baixa <= numero_leucocitos < referencia_media_baixa:
        if saida == "simple":
            print("muito baixa")

        return (numero_leucocitos - referencia_baixa) / (referencia_media_baixa - referencia_baixa) * 3.125

    elif referencia_media_baixa <= numero_leucocitos < referencia_media:
        if saida == "simple":
            print("Baixa")
        return 3.125 + (
                    (numero_leucocitos - referencia_media_baixa) / (referencia_media - referencia_media_baixa)) * 3.125
    elif referencia_media <= numero_leucocitos < referencia_media_alta:
        if saida == "simple":
            print("Normal")
        return 6.25 + ((numero_leucocitos - referencia_media) / (referencia_media_alta - referencia_media)) * 3.125

    elif referencia_media_alta <= numero_leucocitos < referencia_alta:
        if saida == "simple":
            print("Alta")
        return 9.375 + ((numero_leucocitos - referencia_media_alta) / (referencia_alta - referencia_media_alta)) * 3.125

    elif referencia_alta <= numero_leucocitos < referencia_muito_alta:
        if saida == "simple":
            print("Muito Alta")
        return 12.5 + ((numero_leucocitos - referencia_alta) / (referencia_muito_alta - referencia_alta)) * 3.125

    elif referencia_muito_alta <= numero_leucocitos < referencia_extremamente_alta:
        if saida == "simple":
            print("Extremamente Alta")
        return 15.625 + ((numero_leucocitos - referencia_muito_alta) / (
                    referencia_extremamente_alta - referencia_muito_alta)) * 3.125

    else:
        return 25
