def classificar_espirometria(fe_v1, cvf, sexo, idade):
    """
    Analisa os resultados de uma espirometria e fornece uma avaliação básica.

    Attributes:
        fe_v1 (float): Volume Expiratório Forçado no Primeiro Segundo (em litros).
        cvf (float): Capacidade Vital Forçada (em litros).
        sexo (str): Sexo da pessoa ('masculino' ou 'feminino').
        idade (int): Idade da pessoa (em anos).

    Returns:
        str: Uma string indicando a avaliação básica dos resultados.
    """

    fev1_cvf_ratio = fe_v1 / cvf * 100  # Calcula a relação FEV1/CVF em porcentagem

    if fev1_cvf_ratio < 70:
        return "Possível obstrução das vias aéreas."
    elif fev1_cvf_ratio > 80:
        return "Valores normais."
    else:
        return "Possível restrição pulmonar."


