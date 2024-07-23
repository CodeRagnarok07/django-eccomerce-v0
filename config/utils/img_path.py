

def upload_path(instance, filename):
    if " " in instance.pagina.titulo_pagina:
        instance.pagina.titulo_pagina.replace(" ", "_")
    return '/'.join(['paginas',instance.pagina.titulo_pagina, filename])