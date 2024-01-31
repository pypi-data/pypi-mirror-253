def contar_plaquetas(numero_plaquetas,saida):
    """
    Conta o número de plaquetas no sangue e retorna uma métrica de 0 a 25.

    Attributes:
        numero_plaquetas (float): Número de plaquetas por microlitro (por μL).
        saida (str): Indica o tipo de saída desejada ('simple' para uma classificação simplificada).

    Returns:
        float: Métrica de 0 a 25 representando o número de plaquetas.
    """

    referencia_muito_baixa = 50000  # por μL
    referencia_baixa = 150000
    referencia_normal = 450000
    referencia_alta = 750000
    referencia_muito_alta = 1000000

    if numero_plaquetas == 0:
        return "Numero de plaquetas invalido"


    if numero_plaquetas < referencia_muito_baixa:
        if saida == "simple":
            print( "extremamente baixa")
        return 2
    elif referencia_muito_baixa <= numero_plaquetas < referencia_baixa:
        if saida == "simple":
            print( "Muito baixa")
        return 4 + (numero_plaquetas - referencia_muito_baixa) / (referencia_baixa - referencia_muito_baixa) * 6.25
    elif referencia_baixa <= numero_plaquetas < referencia_normal:
        if saida == "simple":
            print ("Baixa")
        return 6.25 + ((numero_plaquetas - referencia_baixa) / (referencia_normal - referencia_baixa)) * 6.25
    elif referencia_normal <= numero_plaquetas < referencia_alta:
        if saida == "simple":
            print( "Alta")
        return 12.5 + ((numero_plaquetas - referencia_normal) / (referencia_alta - referencia_normal)) * 14.25
    elif referencia_alta <= numero_plaquetas < referencia_muito_alta:
        if saida == "simple":
             print("Muito Alta")
        return 18.75 + ((numero_plaquetas - referencia_alta) / (referencia_muito_alta - referencia_alta)) * 6.25
    else:
        if saida == "simple":
            print( "extremamente Alta")
            return 25
