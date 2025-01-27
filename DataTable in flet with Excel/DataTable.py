import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'DataTable in Flet with Excel'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('DataTable in Flet', size=24, color=ft.colors.WHITE)

    page.add(titulo)

ft.app(target=main)