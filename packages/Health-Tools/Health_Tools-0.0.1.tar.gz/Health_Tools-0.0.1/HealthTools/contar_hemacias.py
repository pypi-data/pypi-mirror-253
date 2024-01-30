def contar_hemacias(numero_hemacias, sexo,saida):
    """
    Conta o número de hemácias no sangue e retorna uma métrica de 0 a 25.

    Attributes:
        numero_hemacias (float): Número de hemácias em milhões por microlitro (milhões/μL).
        sexo (str): Sexo da pessoa ('masculino' ou 'feminino').

    Returns:
        float: Métrica de 0 a 25 representando o número de hemácias.
    """

    # Definir faixas de referência
    referencia_muito_baixa_homens = 4.5  # Milhões/µL
    referencia_baixa_homens = 5.5
    referencia_normal_homens = 6.5
    referencia_alta_homens = 7.5
    referencia_muito_alta_homens = 10.0

    referencia_muito_baixa_mulheres = 4.0  # Milhões/µL
    referencia_baixa_mulheres = 5.0
    referencia_normal_mulheres = 6.0
    referencia_alta_mulheres = 7.0
    referencia_muito_alta_mulheres = 10.0

    if sexo.lower() == 'masculino':
        if numero_hemacias == 0:
            return "Contagem de hemacias invalida"
        elif numero_hemacias < referencia_muito_baixa_homens:
            if saida == "simple":
                print("Muito baixa")
            return 3
        elif referencia_muito_baixa_homens <= numero_hemacias < referencia_baixa_homens:
            if saida == "simple":
                print("Baixa")
            return (numero_hemacias - referencia_muito_baixa_homens) / (
                        referencia_baixa_homens - referencia_muito_baixa_homens) * 6.25
        elif referencia_baixa_homens <= numero_hemacias < referencia_normal_homens:
            if saida == "simple":
                print("Normal")
            return 6.25 + ((numero_hemacias - referencia_baixa_homens) / (
                        referencia_normal_homens - referencia_baixa_homens)) * 6.25
        elif referencia_normal_homens <= numero_hemacias < referencia_alta_homens:
            if saida == "simple":
                print("Alta")
            return 12.5 + ((numero_hemacias - referencia_normal_homens) / (
                        referencia_alta_homens - referencia_normal_homens)) * 6.25
        elif referencia_alta_homens <= numero_hemacias < referencia_muito_alta_homens:
            if saida == "simple":
                print("Muito Alta")
            return 18.75 + ((numero_hemacias - referencia_alta_homens) / (
                        referencia_muito_alta_homens - referencia_alta_homens)) * 6.25
    elif sexo.lower() == 'feminino':

        if numero_hemacias < referencia_muito_baixa_mulheres:
            if saida == "simple":
                print("Muito baixa")
            return 0
        elif referencia_muito_baixa_mulheres <= numero_hemacias < referencia_baixa_mulheres:
            if saida == "simple":
                print("Baixa")
            return (numero_hemacias - referencia_muito_baixa_mulheres) / (
                        referencia_baixa_mulheres - referencia_muito_baixa_mulheres) * 6.25
        elif referencia_baixa_mulheres <= numero_hemacias < referencia_normal_mulheres:
            if saida == "simple":
                print("Normal")
            return 6.25 + ((numero_hemacias - referencia_baixa_mulheres) / (
                        referencia_normal_mulheres - referencia_baixa_mulheres)) * 6.25
        elif referencia_normal_mulheres <= numero_hemacias < referencia_alta_mulheres:
            if saida == "simple":
                print("Alta")
            return 12.5 + ((numero_hemacias - referencia_normal_mulheres) / (
                        referencia_alta_mulheres - referencia_normal_mulheres)) * 6.25
        elif referencia_alta_mulheres <= numero_hemacias < referencia_muito_alta_mulheres:
            if saida == "simple":
                print("Muito Alta")
            return 18.75 + ((numero_hemacias - referencia_alta_mulheres) / (
                        referencia_muito_alta_mulheres - referencia_alta_mulheres)) * 6.25
    else:
        return "Sexo não reconhecido"
