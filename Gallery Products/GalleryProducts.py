import flet as ft

def main(page: ft.Page):
    page.title = 'Gallery of products'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_900
    titulo = ft.Text('Gallery of products', size=32, weight=ft.FontWeight.BOLD)
    
    def make_product(name,price,color):
        return ft.Container(
            content=ft.Column([
            ft.Text(f'{name}', size=16, weight=ft.FontWeight.BOLD),
            ft.Text(f'{price}', size=14),
            ft.ElevatedButton('Add to car', color=ft.colors.WHITE)
        ],
        bgcolor=color,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center)
    )

    page.add(titulo)

ft.app(target=main)