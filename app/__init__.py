"""
Este archivo convierte el directori en donde se encuenta en un paquete de Python.
Esto permite:
    - Importat modilos del directorio usando la notacion de puntos
        (from app.routers import #####)
    -Hacer que Python reconozca que ese deirectorio contien còdifo reutilzable
        y organizado
    - definir configuraciones de inicializacion si se necesita, pero también puede
        estar vacio.
Sin __init__.py, Python no trata a app/ como un módulo, lo cual interfiere con muchas
importaciones internas.
"""
