from cx_Freeze import setup, Executable
import sys

# Caminho para o script principal Python
script = 'desbloqueador.py'

# Adiciona bibliotecas necessárias
build_exe_options = {
    "packages": ["tkinter", "selenium", "re", "time", "PIL"]
}

# Configuração do executável
setup(
    name="DemocratizadorDeInformações",
    version="1.0",
    description="Aplicativo para retirar bloqueador de notícias usando Selenium e Tkinter",
    options={"build_exe": build_exe_options},
    executables=[Executable(script, base="Win32GUI" if sys.platform == "win32" else None)]
)