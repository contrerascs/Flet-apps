import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'DataTable in Flet with Excel'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('DataTable in Flet', size=24, color=ft.colors.WHITE)

    data_table = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_600,
        border=ft.border.all(2,ft.colors.BLUE_GREY_200),
        border_radius=10,
        columns=[
            ft.DataColumn(ft.Text('ID', color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text('Name', color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text('Age', color=ft.colors.BLUE_200)),
        ],
        rows=[]
    )

    page.add(titulo, data_table)

ft.app(target=main)