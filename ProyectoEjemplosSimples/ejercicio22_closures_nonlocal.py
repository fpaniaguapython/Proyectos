def generar_funcion_parametrizada_bis(parametro):
    texto = "Soy la funcion parametrizada bis con el parámetro "+parametro 
    resultado = ""
    def funcion1(parametro_extra):
        nonlocal resultado #Modificación del ámbito de la variable, tomando la del ámbito superior
        resultado = texto + " " + parametro_extra
        return(resultado)
    funcion1("Uva")
    print("El resultado es:", resultado)
    return funcion1

f1 = generar_funcion_parametrizada_bis("Pera")
retorno = f1("Manzana")
print(retorno)