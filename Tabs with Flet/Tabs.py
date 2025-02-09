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
        return [random.sample(tareas) for _ in range(5)]
    
    lista_tareas = ft.ListView(spacing=10, padding=20)

    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text, color = ft.colors.WHITE)

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text='Tareas', icon=ft.icons.LIST_ALT),
            ft.Tab(text='Perfil', icon=ft.icons.PERSON),
            ft.Tab(text='Configuración', icon=ft.icons.SETTINGS)
        ],
        expand=1
    )

    page.add(titulo,tabs)

ft.app(target=main)