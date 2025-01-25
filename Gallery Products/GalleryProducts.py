import flet as ft
import os
import base64 

path = r"D:\Sam Contreras\Documents\Programacion\Python\Flet-apps\Gallery Products\assets\Producto1.png"
print("Existe:", os.path.exists(path))

def main(page: ft.Page):
    page.title = 'Gallery of products'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_900
    
    def make_product(name,price,color, imagen_nombre):
        imagen_path = os.path.join(os.path.dirname(__file__), 'assets', imagen_nombre)
        try:
            with open(imagen_path, 'rb') as image_file:
                imagen_bytes = base64.b64encode(image_file.read()).decode()
        except FileNotFoundError:
            print(f'Advertencia: La imagen {imagen_nombre} no existe en {imagen_path}')
            imagen_bytes = None
        return ft.Container(
            content=ft.Column([
                ft.Image(
                    src_base64=imagen_bytes,
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,
                    error_content=ft.Text('Imagen no encontrada') if imagen_bytes else ft.Text('Imageno no encontrada')
                ),
                ft.Text(f'{name}', size=16, weight=ft.FontWeight.BOLD),
                ft.Text(f'{price}', size=14),
                ft.ElevatedButton('Add to car', color=ft.colors.WHITE)
            ]),
            bgcolor=color,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center
        )
        

    products = [
        make_product('Product 1', 19.99, ft.colors.BLUE_500,"Producto1.png"),
        make_product('Product 2', 29.99, ft.colors.GREEN_500,"Producto2.png"),
        make_product('Product 3', 39.99, ft.colors.ORANGE_500,"Producto3.png"),
        make_product('Product 4', 49.99, ft.colors.PURPLE_500,"Producto4.png"),
        make_product('Product 5', 19.99, ft.colors.BLUE_500,"Producto5.png"),
        make_product('Product 6', 29.99, ft.colors.GREEN_500,"Producto6.png"),
        make_product('Product 7', 39.99, ft.colors.ORANGE_500,"Producto7.png"),
        make_product('Product 8', 49.99, ft.colors.PURPLE_500,"Producto8.png")
    ]

    gallery = ft.ResponsiveRow(
        [ft.Container(product, col={'sm':12,'md':6,'lg':3}) for product in products],
        run_spacing=20,
        spacing=20
    )

    contenido = ft.Column([
        ft.Text('Product Gallery', size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.colors.WHITE24),
        gallery
    ], scroll=ft.ScrollMode.AUTO, expand=True)

    page.add(contenido)

ft.app(target=main)