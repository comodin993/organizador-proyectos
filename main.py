import os
import subprocess

# Carpeta donde están los proyectos
BASE_PATH = os.path.abspath("..")

print("📂 Analizando proyectos en:")
print(BASE_PATH)
print("-" * 40)

for nombre in os.listdir(BASE_PATH):
    ruta = os.path.join(BASE_PATH, nombre)

    if not os.path.isdir(ruta):
        continue

    print(f"\n🔹 Proyecto: {nombre}")

    git_dir = os.path.join(ruta, ".git")

    if os.path.isdir(git_dir):
        print("  ✔ Es un repositorio Git")

        try:
            resultado = subprocess.check_output(
                ["git", "-C", ruta, "log", "-1", "--oneline"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()

            print(f"  🕒 Último commit: {resultado}")

        except Exception:
            print("  ⚠ No se pudo obtener el historial Git")

    else:
        print("  ✖ No es un repositorio Git")
