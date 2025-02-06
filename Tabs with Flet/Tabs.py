import flet as ft
import random

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'Tabs in Flet'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Ejemplo de Tabs in Flet', size=24, color=ft.colors.WHITE)

    tabs = ft.Tabs(
        selected_index=0,
        
    )

    page.add(titulo)

ft.app(target=main)