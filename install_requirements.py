import os
import subprocess


def get_project_path():
    # Obtener la ruta del directorio actual del script
    current_script_path = os.path.abspath(__file__)

    # Obtener la ruta del directorio padre (directorio del proyecto)
    project_path = os.path.dirname(current_script_path)

    return project_path


def install_requirements():
    project_path = get_project_path()
    requirements_file = os.path.join(project_path, 'requirements.txt')

    # Comando para instalar los paquetes desde el archivo "requirements.txt"
    command = f"pip install -r {requirements_file}"

    try:
        # Ejecutar el comando en la ubicación del proyecto
        subprocess.run(command, shell=True, check=True)
        print("Paquetes instalados exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar los paquetes: {e}")


if __name__ == "__main__":
    install_requirements()
