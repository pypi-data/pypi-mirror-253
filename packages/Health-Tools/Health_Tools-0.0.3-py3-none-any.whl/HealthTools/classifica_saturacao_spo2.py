def classificar_spo2(spo2):
    """
    Classifica a saturação de oxigênio (SpO2) em categorias.

    Attributes:
        spo2 (float): Saturação de oxigênio em porcentagem (%).

    Returns:
        str: Categoria da saturação de oxigênio.
    """

    if spo2 < 90:
        return "Baixa saturação de oxigênio"
    elif 90 <= spo2 < 95:
        return "Saturação de oxigênio normal baixa"
    elif 95 <= spo2 <= 100:
        return "Saturação de oxigênio normal"
    else:
        return "Valor inválido"
