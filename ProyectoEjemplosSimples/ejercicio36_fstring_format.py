novio = "Ramón"
novia = "Lourdes"
cadena = f"Estamos encantados de invitarles al compromiso de {novio} y {novia}"
print(cadena)

frase_celebre = ("El padre de {} se llama {}").format("Luke","Darth Vader")
print(frase_celebre)
frase_celebre = ("El padre de {0} se llama {1}. Me cae mejor {1}.").format("Luke","Darth Vader")
print(frase_celebre)
frase_celebre = ("El padre de {hijo} se llama {padre}. Me cae mejor {padre}.").format(hijo="Luke",padre="Darth Vader")
print(frase_celebre)
