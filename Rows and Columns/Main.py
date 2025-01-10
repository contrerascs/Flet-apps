import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'Mi app mejorada con filas y columnas'

    texto1 = ft.Text('Texto 1', size=24, color=ft.colors.WHITE)

    texto2 = ft.Text('Texto 2', size=24, color=ft.colors.WHITE)

    texto3 = ft.Text('Texto 3', size=24, color=ft.colors.WHITE)
    
    fila_textos = ft.Row(
        controls=[texto1,texto2,texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_textos)

    btn1 = ft.FilledButton(text='Botón 1')
    btn2 = ft.FilledButton(text='Botón 2')
    btn3 = ft.FilledButton(text='Botón 3')

    fila_botones = ft.Row(
        controls=[btn1,btn2,btn3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_botones)

    textos_columnas = [
        ft.Text('Columna 1 - Fila 1', size=18, color=ft.colors.WHITE),
        ft.Text('Columna 1 - Fila 2', size=18, color=ft.colors.WHITE),
        ft.Text('Columna 1 - Fila 3', size=18, color=ft.colors.WHITE)
    ]

    columna_textos1 = ft.Column(
        controls=textos_columnas
    )

    #page.add(columna_textos1)

    textos_columnas2 = [
        ft.Text('Columna 2 - Fila 1', size=18, color=ft.colors.WHITE),
        ft.Text('Columna 2 - Fila 2', size=18, color=ft.colors.WHITE),
        ft.Text('Columna 2 - Fila 3', size=18, color=ft.colors.WHITE)
    ]

    columna_textos2 = ft.Column(
        controls=textos_columnas2
    )

    textos_columnas3 = [
        ft.Text('Columna 3 - Fila 1', size=18, color=ft.colors.WHITE),
        ft.Text('Columna 3 - Fila 2', size=18, color=ft.colors.WHITE),
        ft.Text('Columna 3 - Fila 3', size=18, color=ft.colors.WHITE)
    ]

    columna_textos3 = ft.Column(
        controls=textos_columnas3
    )

    fila_columnas = ft.Row(
        controls=[columna_textos1,columna_textos2,columna_textos3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    )

    page.add(fila_columnas)

ft.app(target=main)