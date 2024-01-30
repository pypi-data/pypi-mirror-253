def teste_funcao_hepatica(ast, alt, alp, bilirrubina_total, bilirrubina_direta, bilirrubina_indireta, saida='advanced'):
    """
    Avalia a saúde do fígado com base nos níveis de enzimas hepáticas e bilirrubina no sangue.

    Attributes:
        ast (float): Nível da enzima AST (aspartato aminotransferase) no sangue em U/L.
        alt (float): Nível da enzima ALT (alanina aminotransferase) no sangue em U/L.
        alp (float): Nível da enzima ALP (fosfatase alcalina) no sangue em U/L.
        bilirrubina_total (float): Nível total de bilirrubina no sangue em mg/dL.
        bilirrubina_direta (float): Nível de bilirrubina direta no sangue em mg/dL.
        bilirrubina_indireta (float): Nível de bilirrubina indireta no sangue em mg/dL.
        saida (str): Tipo de saída desejado ('advanced' para detalhado ou 'simple' para resumido).

    Returns:
        dict or str: Se 'saida' for 'advanced', retorna um dicionário com os resultados detalhados.
                     Se 'saida' for 'simple', retorna uma classificação simplificada da função hepática.
    """

    # Definir os limites de referência para as enzimas hepáticas e bilirrubina
    limite_superior_ast = 40  # U/L
    limite_superior_alt = 56  # U/L
    limite_superior_alp = 120  # U/L
    limite_superior_bilirrubina_total = 1.2  # mg/dL
    limite_superior_bilirrubina_direta = 0.3  # mg/dL
    limite_superior_bilirrubina_indireta = 0.9  # mg/dL

    if (ast <= limite_superior_ast and alt <= limite_superior_alt and alp <= limite_superior_alp and
            bilirrubina_total <= limite_superior_bilirrubina_total and
            bilirrubina_direta <= limite_superior_bilirrubina_direta and
            bilirrubina_indireta <= limite_superior_bilirrubina_indireta):
        if saida == 'advanced':
            return {'resultado': 'Normal', 'detalhes': 'A função hepática está dentro dos limites normais.'}
        elif saida == 'simple':
            return 'Normal'
    else:
        if saida == 'advanced':
            return {'resultado': 'Anormal', 'detalhes': 'A função hepática está alterada. Consulte um médico.'}
        elif saida == 'simple':
            return 'Anormal'
