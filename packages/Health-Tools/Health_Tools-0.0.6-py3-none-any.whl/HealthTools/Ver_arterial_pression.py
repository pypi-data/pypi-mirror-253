def medir_pressão_arterial(sistólica, diastólica):
    """
    Classifica a pressão arterial com base nos valores da pressão sistólica e diastólica.

    Attributes:
        sistolica (int): Valor da pressão arterial sistólica.
        diastolica (int): Valor da pressão arterial diastólica.

    Returns:
        str: Classificação da pressão arterial, que pode ser 'Pressão arterial normal', 'Pressão arterial elevada', 'Pressão arterial de estágio 1' ou 'Pressão arterial de estágio 2'.
    """
    if sistólica < 90 and diastólica < 60:
        return "Pressão arterial baixa"
    elif sistólica < 120 and diastólica < 80:
        return "Pressão arterial normal"
    elif 120 <= sistólica < 130 and diastólica < 80:
        return "Pressão arterial elevada"
    elif 130 <= sistólica < 140 or 80 <= diastólica < 90:
        return "Pressão arterial de estágio 1"
    elif sistólica >= 140 or diastólica >= 90:
        return "Pressão arterial de estágio 2"
    else:
        return "Pressão Anormal"

def Ver_arterial_pression(sistólica, diastólica, sexo, idade, saida='simple'):
    """
    Verifica a pressão arterial e fornece uma classificação baseada nos valores da pressão sistólica e diastólica, sexo e idade.

    Attributes:
        sistolica (int): Valor da pressão arterial sistólica.
        diastolica (int): Valor da pressão arterial diastólica.
        sexo (str): Sexo da pessoa ('masculino' ou 'feminino').
        idade (int): Idade da pessoa em anos.
        saida (str): Tipo de saída desejado ('simple' para apenas o valor da classificação ou 'advanced' para a descrição completa).

    Returns:
        str or float: Se 'saida' for 'simple', retorna a classificação da pressão arterial (muito baixa, baixa, normal, elevada, estágio 1 ou estágio 2).
                      Se 'saida' for 'advanced', retorna o valor da classificação de acordo com a faixa de referência.
    """

    if sexo.lower() == 'masculino':
        idade_referência = 45
        if idade < idade_referência:
            if sistólica < 120 and diastólica < 80:
                if saida == 'simple':
                    return 12.5
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 120 <= sistólica < 130 and diastólica < 80:
                if saida == 'simple':
                    return 15
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 130 <= sistólica < 140 or 80 <= diastólica < 90:
                if saida == 'simple':
                    return 18
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif sistólica >= 140 or diastólica >= 90:
                if saida == 'simple':
                    return 25
                else:
                    return medir_pressão_arterial(sistólica,diastólica)

        else:
            if sistólica < 120 and diastólica < 80:
                if saida == 'simple':
                    return 12.5
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 120 <= sistólica < 130 and diastólica < 80:
                if saida == 'simple':
                    return 15
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 130 <= sistólica < 140 or 80 <= diastólica < 90:
                if saida == 'simple':
                    return 18
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif sistólica >= 140 or diastólica >= 90:
                if saida == 'simple':
                    return 25
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
    elif sexo.lower() == 'feminino':
        idade_referência = 55
        if idade < idade_referência:
            if sistólica < 120 and diastólica < 80:
                if saida == 'simple':
                    return 12.5
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 120 <= sistólica < 130 and diastólica < 80:
                if saida == 'simple':
                    return 15
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 130 <= sistólica < 140 or 80 <= diastólica < 90:
                if saida == 'simple':
                    return 18
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif sistólica >= 140 or diastólica >= 90:
                if saida == 'simple':
                    return 25
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
        else:
            if sistólica < 120 and diastólica < 80:
                if saida == 'simple':
                    return 12.5
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 120 <= sistólica < 130 and diastólica < 80:
                if saida == 'simple':
                    return 15
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif 130 <= sistólica < 140 or 80 <= diastólica < 90:
                if saida == 'simple':
                    return 18
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
            elif sistólica >= 140 or diastólica >= 90:
                if saida == 'simple':
                    return 25
                else:
                    return medir_pressão_arterial(sistólica,diastólica)
    else:
        return "Sexo não reconhecido"
