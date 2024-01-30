def analisar_status(valor, referencia):
    """
    Analisa o status de um valor em relação a uma faixa de referência.

    Attributes:
        valor (float): O valor a ser analisado.
        referencia (list): A faixa de referência na forma [min, max].

    Returns:
        str: O status do valor em relação à faixa de referência.
    """

    if valor < referencia[0]:
        return "Muito baixo"
    elif referencia[0] <= valor <= referencia[1]:
        return "Baixo"
    elif referencia[1] < valor <= referencia[2]:
        return "Normal"
    elif referencia[2] < valor <= referencia[3]:
        return "Alto"
    else:
        return "Muito alto"

def teste_funcao_tireoidiana(tsh, t4_total, t4_livre, t3_total, t3_livre, saida='advanced'):
    """
    Avalia a função da tireoide medindo os níveis de hormônios tireoidianos no sangue.

    Attributes:
        tsh (float): Valor do hormônio estimulante da tireoide (TSH) em mIU/L.
        t4_total (float): Valor do hormônio tiroxina total (T4 Total) em nmol/L.
        t4_livre (float): Valor do hormônio tiroxina livre (T4 Livre) em ng/dL.
        t3_total (float): Valor do hormônio tri-iodotironina total (T3 Total) em nmol/L.
        t3_livre (float): Valor do hormônio tri-iodotironina livre (T3 Livre) em pg/mL.
        saida (str): Tipo de saída desejado ('advanced' ou 'simple').

    Returns:
        str or tuple: Resultado do teste de função tireoidiana. Se 'saida' for 'simple', retorna apenas o resultado. Se 'saida' for 'advanced', retorna o resultado detalhado.
    """

    referencia_tsh = [0.3, 4.0, 10.0, 20.0]
    referencia_t4_total = [60, 160, 200, 350]
    referencia_t4_livre = [0.8, 1.8, 2.5, 3.9]
    referencia_t3_total = [0.6, 2.0, 2.5, 5.7]
    referencia_t3_livre = [2.0, 4.4, 5.4, 8.7]

    if saida == 'simple':
        status_tsh = analisar_status(tsh, referencia_tsh)
        status_t4_total = analisar_status(t4_total, referencia_t4_total)
        status_t4_livre = analisar_status(t4_livre, referencia_t4_livre)
        status_t3_total = analisar_status(t3_total, referencia_t3_total)
        status_t3_livre = analisar_status(t3_livre, referencia_t3_livre)

        return f"TSH: {tsh} - Classificação: {status_tsh}\n" \
               f"T4 Total: {t4_total} - Classificação: {status_t4_total}\n" \
               f"T4 Livre: {t4_livre} - Classificação: {status_t4_livre}\n" \
               f"T3 Total: {t3_total} - Classificação: {status_t3_total}\n" \
               f"T3 Livre: {t3_livre} - Classificação: {status_t3_livre}"
    else:
        pass
