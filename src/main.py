# Inicio del programa.

import sys

from .archivos import c_archivos
from .reportes import c_reportes
from .sistema import c_sistema

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    archivos = c_archivos()
    reportes = c_reportes(archivos)
    sistema = c_sistema(archivos, reportes)

    try:
        sistema.ejecutar()
    except (OSError, ValueError, KeyError) as error:
        print(f"Error al ejecutar el programa: {error}")
    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")

if __name__ == "__main__":
    main()
