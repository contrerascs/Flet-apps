import flet as ft
import random

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'Tabs in Flet'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Ejemplo de Tabs in Flet', size=24, color=ft.colors.WHITE)

    def generar_tareas():
        tareas = ['Hacer la compra', 'Llamar al médico', 'Estudiar para el examen',
                  'Hacer ejercicio', 'Leer un libro', 'Preparar la cena']
        return random.sample(tareas,4)
    
    lista_tareas = ft.ListView(spacing=10, padding=20)

    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea, color = ft.colors.WHITE))
        page.update()

    actualizar_tareas()

    btn_actualizar = ft.ElevatedButton('Actualizar Tareas', on_click=lambda _: actualizar_tareas())

    contenido_tareas = ft.Column([lista_tareas, btn_actualizar])

    #Contenido para pestaña de Perfil
    campo_nombre = ft.TextField(label='Nombre', bgcolor=ft.colors.BLUE_GREY_700)
    campo_email = ft.TextField(label='Email', bgcolor=ft.colors.BLUE_GREY_700)
    btn_guadar = ft.ElevatedButton('Guardar Perfil')
    contenido_perfil = ft.Column([campo_nombre, campo_email, btn_guadar])
    
    #Contenido para pestaña de Configuracion
    switch_notificaciones = ft.Switch(label='Notificaciones', value=True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label='Volumen')
    contenido_config = ft.Column([switch_notificaciones, slider_volumen])

    tabs = ft.Tabs(
        selected_index=0, 
        animation_duration=300,
        tabs=[
            ft.Tab(text='Tareas', icon=ft.icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text='Perfil', icon=ft.icons.PERSON, content=contenido_perfil),
            ft.Tab(text='Configuración', icon=ft.icons.SETTINGS, content=contenido_config)
        ],
        expand=1
    )

    page.add(titulo,tabs)

ft.app(target=main)