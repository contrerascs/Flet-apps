import yt_dlp as yt
import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = 'Download Video From Youtube'
    page.padding = 25
    page.theme_mode = 'light'
    page.bgcolor = ft.colors.BLUE_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título de la aplicación
    title = ft.Text(
        'Download video from Youtube', 
        size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_GREY_800
    )

    # Campo de texto para introducir el enlace del video
    link_field = ft.TextField(
        hint_text='Write a video link', 
        color=ft.colors.BLUE_GREY_800
    )

    # Etiqueta para mostrar la carpeta seleccionada
    folder_label = ft.Text(value="No folder selected", size=14, color=ft.colors.GREY)

    # Función para seleccionar la carpeta de destino
    def select_folder(e):
        folder_picker = ft.FilePicker(on_result=lambda result: set_folder(result.path))
        page.dialog = folder_picker
        folder_picker.get_directory_path()

    def set_folder(folder_path):
        nonlocal selected_folder
        if folder_path:
            selected_folder = folder_path
            folder_label.value = f"Selected folder: {selected_folder}"
            page.update()

    selected_folder = None  # Carpeta seleccionada, inicializada como None

    # Función para descargar el video
    def download_videos(e):
        if link_field.value and selected_folder:
            # Configurar la descarga del video con la carpeta seleccionada
            ydl_opts = {
                'format': 'best',
                'outtmpl': f"{selected_folder}/%(title)s.%(ext)s",  # Guardar en la carpeta seleccionada
            }
            try:
                with yt.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link_field.value])
                folder_label.value = "Download completed successfully!"
            except Exception as error:
                folder_label.value = f"Error: {str(error)}"
        else:
            folder_label.value = "Please provide a link and select a folder!"
        page.update()

    # Botón para seleccionar la carpeta de descarga
    btn_select_folder = ft.FilledButton('Select Folder', on_click=select_folder)

    # Botón para iniciar la descarga
    btn_download = ft.FilledButton('Download', on_click=download_videos)

    # Agregar los elementos a la página
    page.add(
        title,
        link_field,
        btn_select_folder,
        folder_label,
        btn_download
    )

ft.app(target=main)
