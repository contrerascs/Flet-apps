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

    products = [
        make_product('Product 1', 19.99, ft.colors.BLUE_500),
        make_product('Product 2', 29.99, ft.colors.GREEN_500),
        make_product('Product 3', 39.99, ft.colors.ORANGE_500),
        make_product('Product 4', 49.99, ft.colors.PURPLE_500)
    ]

    gallery = ft.ResponsiveRow(
        [ft.Container(product, col={'sm':12,'md':6,'lg':3}) for product in products],
        run_spacing=20,
        spacing=20
    )

    page.add(titulo, gallery)

ft.app(target=main)