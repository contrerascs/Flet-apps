import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = 'Mi app'

    texto = ft.Text('Mi primera app con Flet',color=ft.colors.WHITE)
    
    
    texto2 = ft.Text('Este es un ejemplo para mi pagina de Instagram',color=ft.colors.WHITE)
    
    def cambiar_texto(e):
        texto2.value = 'Suscribete para más videos'
        page.update()

    boton = ft.FilledButton(text='Cambiar texto', on_click=cambiar_texto)

    page.add(texto)
    page.add(texto2)
    page.add(boton)

ft.app(target=main)