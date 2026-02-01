import os
import subprocess
import sys


# =========================
# COLORES ANSI (limpios y contrastados)
# =========================
RESET = "\033[0m"

TITULO = "\033[96m"        # Cyan claro
SEPARADOR = "\033[94m"     # Azul
PROYECTO = "\033[95m"      # Blanco brillante

OK = "\033[92m"            # Verde
WARN = "\033[93m"          # Amarillo
ERROR = "\033[91m"         # Rojo

DETALLE = "\033[90m"       # Gris (detalle / info secundaria)

# =========================
# CONFIG
# =========================
if len(sys.argv) < 2:
    print("❌ Error: no se especificó la ruta a analizar")
    print("Uso: python main.py <ruta_proyectos>")
    sys.exit(1)

BASE_PATH = os.path.abspath(sys.argv[1])


# =========================
# ENCABEZADO
# =========================
print(f"\n{TITULO}📊 RESUMEN DE PROYECTOS{RESET}")
print(f"{SEPARADOR}{'=' * 40}{RESET}")

# =========================
# RECORRIDO DE PROYECTOS
# =========================
for nombre in os.listdir(BASE_PATH):
    ruta = os.path.join(BASE_PATH, nombre)

    if not os.path.isdir(ruta):
        continue

    print(f"\n{SEPARADOR}{'-' * 40}{RESET}")
    print(f"{PROYECTO}🔹 Proyecto:{nombre}{RESET}")

    git_dir = os.path.join(ruta, ".git")

    if not os.path.isdir(git_dir):
        print(f"{ERROR}  ❌ No es un repositorio Git{RESET}")
        continue

    print(f"{OK}  ✔ Es un repositorio Git{RESET}")

    # =========================
    # OBTENER ÚLTIMO COMMIT
    # =========================
    try:
        salida = subprocess.check_output(
            [
                "git", "-C", ruta,
                "log", "-1",
                "--pretty=format:%h|%cd|%s",
                "--date=iso"
            ],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()

        if salida:
            hash_commit, fecha_commit, mensaje_commit = salida.split("|", 2)

            print(f"{OK}  🕒 Último commit:{RESET}")
            print(f"{DETALLE}     • Hash :{RESET} {hash_commit}")
            print(f"{DETALLE}     • Fecha:{RESET} {fecha_commit}")
            print(f"{DETALLE}     • Msg  :{RESET} {mensaje_commit}")
        else:
            print(f"{WARN}  ⚠ Repositorio sin commits{RESET}")

    except Exception:
        print(f"{WARN}  ⚠ No se pudo obtener el historial Git{RESET}")
