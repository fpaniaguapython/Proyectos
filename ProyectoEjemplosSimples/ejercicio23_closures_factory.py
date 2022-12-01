IMPRESORA_ASTERISCOS = 1
IMPRESORA_MASES = 2

def get_impresora(tipo_impresora):
    def impresora1(texto):
        print("****",texto,"****")
    def impresora2(texto):
        print("++++",texto,"++++")
    if tipo_impresora==IMPRESORA_ASTERISCOS:
        return impresora1
    elif (tipo_impresora==IMPRESORA_MASES):
        return impresora2

impresora = get_impresora(IMPRESORA_ASTERISCOS)
impresora("Ex machina")