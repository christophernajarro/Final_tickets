import sys
import os
from dotenv import load_dotenv

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Añadir el directorio raíz al PYTHONPATH
sys.path.append(parent_dir)

# Construir la ruta completa al archivo .env
env_path = os.path.join(parent_dir, '.env')

# Cargar las variables de entorno desde el archivo .env
load_dotenv(dotenv_path=env_path)