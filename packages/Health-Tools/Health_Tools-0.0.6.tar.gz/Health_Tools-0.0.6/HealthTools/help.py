import HealthTools
def help():
    """Exibe informações de ajuda para as funções do módulo HealthTools."""

    functions = [
        "Ver_arterial_pression",
        "verifica_imc",
        "calcular_tfg",
        "contar_hemacias",
        "contar_leucocitos",
        "contar_plaquetas",
        "calcular_fcm",
        "calcular_frequencia_respiratoria",
        "calcular_debito_cardiaco",
        "calcular_tp",
        "calcular_ttpa",
        "calcular_indice_apgar",
        "classificar_pvc",
        "classificar_glicemia",
        "classificar_spo2",
        "calcular_debito_urinario",
        "classificar_espirometria",
        "teste_capacidade_anaerobica",
        "teste_funcao_renal",
        "teste_funcao_hepatica",
        "teste_funcao_tireoidiana",
    ]

    print("Funções disponíveis no módulo HealthTools:")
    print("----------------------------------------")

    for function_name in functions:
        function = getattr(HealthTools.__init__, function_name, None)
        if function:
            print(f"\n{function_name}:")
            print(function.__doc__)
        else:
            print(f"\n{function_name}: Função não encontrada.")



