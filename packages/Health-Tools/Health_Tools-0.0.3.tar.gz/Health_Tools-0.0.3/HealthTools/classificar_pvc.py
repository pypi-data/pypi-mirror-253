def classificar_pvc(pvc):
    """
    Classifica a Pressão Venosa Central (PVC) em categorias.

    Attributes:
        pvc (float): Pressão Venosa Central em mmHg.

    Returns:
        str: Categoria da PVC.
    """

    if pvc < 3:
        return "Muito baixa"
    elif 3 <= pvc <= 5:
        return "Baixa"
    elif 6 <= pvc <= 12:
        return "Normal"
    elif 13 <= pvc <= 18:
        return "Alta"
    else:
        return "Muito alta"
