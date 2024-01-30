def classificar_glicemia(glicemia):
    """
    Classifica a concentração de glicose no sangue (glicemia) em categorias.

    Attributes:
        glicemia (float): Concentração de glicose no sangue em mg/dL.

    Returns:
        str: Categoria da glicemia.
    """
    if glicemia < 70:
        return "Hipo glicemia (Muito baixa)"
    elif 70 <= glicemia < 100:
        return "Normal"
    elif 100 <= glicemia < 125:
        return "Pré-diabetes (Elevada)"
    else:
        return "Diabetes (Muito alta)"
