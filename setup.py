import sys
import os

from cx_Freeze import setup, Executable

files = ['assets', 'controllers', 'facturacion_db.db']

exe = Executable(script="app.py", base="Win32GUI")

setup(
    name="Sistema Presupuestario TECNO SERVICIOS ROJAS",
    version="1.0",
    description="Aplicación de Sistema Presupuestario para TECNO SERVICIOS ROJAS - Diseñado y Elaborado por Goichi Kawasoe Hernández / Email: gkawasoe@gmail.com",
    author="Goichi Kawasoe Hernández",
    options={'build_exe': {'include_files': files}},
    executables=[exe]
)