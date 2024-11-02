import re

def lexico(curp):
    pattern = r"([A-Z]{2})([A-Z]{1})([A-Z]{1})(\d{6})([HM])([A-Z]{2})([A-Z]{3})([A-Z\d]{1})(\d{1})"
    match = re.match(pattern, curp)
    
    if match:
        components = {
            'Apellido Paterno': match.group(1),
            'Apellido Materno': match.group(2),
            'Nombre': match.group(3),
            'Fecha de Nacimiento': match.group(4),
            'Género': match.group(5),
            'Estado': match.group(6),
            'Consonantes Internas': match.group(7),
            'Homoclave': match.group(8),
            'Dígito Verificador': match.group(9)
        }
        return components
    else:
        return None
