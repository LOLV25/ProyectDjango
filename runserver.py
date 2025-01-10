import webbrowser
import os
import sys
from django.core.management import execute_from_command_line

def runserver():
    # Abre el navegador automáticamente
    webbrowser.open("http://127.0.0.1:8000/")
    
    # Ejecuta el servidor Django
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whatsapp.settings")
    runserver()
