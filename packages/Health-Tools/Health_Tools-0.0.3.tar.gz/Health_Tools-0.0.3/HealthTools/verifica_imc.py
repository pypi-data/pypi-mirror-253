def verifica_imc(peso, altura, sexo, saida):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Attributes:
        peso (float): Peso da pessoa em quilogramas (kg).
        altura (float): Altura da pessoa em metros (m).
        sexo (str): Sexo da pessoa ('masculino' ou 'feminino').
        saida (str): Tipo de saída desejado ('simple' ou outro valor para saída avançada).

    Returns:
        float or dict: Valor do IMC calculado. Se 'saida' for 'simple', retorna apenas o valor do IMC.
                       Se 'saida' for outro valor, retorna um dicionário com o IMC e uma classificação do estado de peso.
    """

    if saida == "simple":
        if sexo.lower() == 'masculino':
            imc = peso / (altura ** 2)
            if altura == 1.50:
                imcf = int(imc)
                if 22 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 29:
                    return "sobrepeso"
                elif 30 <= imcf <= 39:
                    return "obesidade"
                elif 40 <= imcf <= 53:
                    return "obesidade morbida"
                else:
                    return "peso invalido"
            elif altura == 1.60:
                imcf = int(imc)
                if 24 <= imcf <= 26:
                    return "normal"
                elif 27 <= imcf <= 31:
                    return "sobrepeso"
                elif 32 <= imcf <= 41:
                    return "obesidade"
                elif 42 <= imcf <= 56:
                    return "obesidade morbida"
                else:
                    return "peso invalido"
            elif altura == 1.70:
                imcf = int(imc)
                if 27 <= imcf <= 29:
                    return "normal"
                elif 30 <= imcf <= 34:
                    return "sobrepeso"
                elif 35 <= imcf <= 44:
                    return "obesidade"
                elif 45 <= imcf <= 60:
                    return "obesidade morbida"
                else:
                    return "peso invalido"


            elif altura == 1.80:
                imcf = int(imc)
                if 20 <= imcf <= 23:
                    return "normal"
                elif 24 <= imcf <= 30:
                    return "sobrepeso"
                elif 31 <= imcf <= 37:
                    return "obesidade"
                elif 38 <= imcf <= 64:
                    return "obesidade morbida"
                else:
                    return "peso invalido"

            elif altura == 1.90:
                imcf = int(imc)
                if 21 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 29:
                    return "sobrepeso"
                elif 30 <= imcf <= 33:
                    return "obesidade"
                elif 34 <= imcf <= 68:
                    return "obesidade morbida"
                else:
                    return "peso invalido"

            elif altura == 2.00:
                imcf = int(imc)
                if 20 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 29:
                    return "sobrepeso"
                elif 30 <= imcf <= 33:
                    return "obesidade"
                elif 34 <= imcf <= 72:
                    return "obesidade morbida"
                else:
                    return "peso invalido"

            elif altura == 2.10:
                imcf = int(imc)
                if 20 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 27:
                    return "sobrepeso"
                elif 28 <= imcf <= 35:
                    return "obesidade"
                elif 36 <= imcf <= 75:
                    return "obesidade morbida"
                else:
                    return "peso invalido"
            else:
                return "altura não suportada"


        elif sexo.lower() == 'feminino':
            imc = peso / ((altura - 0.4) ** 2)
            if altura == 1.50:
                imcf = int(imc)
                if 22 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 29:
                    return "sobrepeso"
                elif 30 <= imcf <= 39:
                    return "obesidade"
                elif 40 <= imcf <= 53:
                    return "obesidade morbida"
                else:
                    return "peso invalido"
            elif altura == 1.60:
                imcf = int(imc)
                if 24 <= imcf <= 26:
                    return "normal"
                elif 27 <= imcf <= 31:
                    return "sobrepeso"
                elif 32 <= imcf <= 41:
                    return "obesidade"
                elif 42 <= imcf <= 56:
                    return "obesidade morbida"
                else:
                    return "peso invalido"
            elif altura == 1.70:
                imcf = int(imc)
                if 27 <= imcf <= 29:
                    return "normal"
                elif 30 <= imcf <= 34:
                    return "sobrepeso"
                elif 35 <= imcf <= 44:
                    return "obesidade"
                elif 45 <= imcf <= 60:
                    return "obesidade morbida"
                else:
                    return "peso invalido"


            elif altura == 1.80:
                imcf = int(imc)
                if 20 <= imcf <= 23:
                    return "normal"
                elif 24 <= imcf <= 30:
                    return "sobrepeso"
                elif 31 <= imcf <= 37:
                    return "obesidade"
                elif 38 <= imcf <= 64:
                    return "obesidade morbida"
                else:
                    return "peso invalido"

            elif altura == 1.90:
                imcf = int(imc)
                if 21 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 29:
                    return "sobrepeso"
                elif 30 <= imcf <= 33:
                    return "obesidade"
                elif 34 <= imcf <= 68:
                    return "obesidade morbida"
                else:
                    return "peso invalido"

            elif altura == 2.00:
                imcf = int(imc)
                if 20 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 29:
                    return "sobrepeso"
                elif 30 <= imcf <= 33:
                    return "obesidade"
                elif 34 <= imcf <= 72:
                    return "obesidade morbida"
                else:
                    return "peso invalido"

            elif altura == 2.10:
                imcf = int(imc)
                if 20 <= imcf <= 24:
                    return "normal"
                elif 25 <= imcf <= 27:
                    return "sobrepeso"
                elif 28 <= imcf <= 35:
                    return "obesidade"
                elif 36 <= imcf <= 75:
                    return "obesidade morbida"
                else:
                    return "peso invalido"
            else:
                return "altura não suportada"

    else:
        if sexo.lower() == 'masculino':
            imc = peso / (altura ** 2)
        elif sexo.lower() == 'feminino':
            imc = peso / ((altura - 0.4) ** 2)
        else:
            return "Sexo não reconhecido"

        return imc
