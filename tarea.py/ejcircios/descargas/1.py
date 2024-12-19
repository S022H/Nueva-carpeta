import yt_dlp as youtube_dl
import os

# Lista de URLs de YouTube que deseas descargar
urls = [
    'https://youtu.be/DSz3ui5Uhm8?si=VGU8xxctVIfkkLT5',
    
    # Agrega más URLs según sea necesario
]

# Carpeta de destino en el USB
usb_folder = 'D:\+300 m'

# Verificar si la carpeta del USB existe
if not os.path.exists(usb_folder):
    os.makedirs(usb_folder)

# Configurar las opciones de descarga para 720p
ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Especificar resolución máxima de 720p
    'outtmpl': os.path.join(usb_folder, '%(title)s.%(ext)s')
}

# Descargar videos
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

print("Descarga completada en 720p directamente en el USB.")


