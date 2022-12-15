"""
Validación utilizando la librería xmlschema

https://pypi.org/project/xmlschema/

pip install xmlschema
"""

import xmlschema
my_schema = xmlschema.XMLSchema('factura.xsd')
resultado = my_schema.is_valid("factura.xml")
if (resultado==False):
    my_schema.validate("factura.xml")
else:
    print("VALIDADO")