# proyecto/services/supabase_service.py

from supabase import create_client, Client

# URL y clave de tu proyecto Supabase
url = "https://tgvyvhjqfokuxmowpeaf.supabase.co/storage/v1/s3"
key = "e49daf5a6a715e2761dc0cb52e98b645"

# Crear cliente de Supabase
supabase: Client = create_client(url, key)

def upload_file(file, ActaContitucion):
    # Subir archivo a Supabase Storage
    response = supabase.storage.from_(ActaContitucion).upload(file.name, file)
    return response

def get_file_url(ActaContitucion, file_name):
    # Obtener la URL pública del archivo
    url = supabase.storage.from_(ActaContitucion).get_public_url(file_name)
    return url
