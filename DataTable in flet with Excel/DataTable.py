import flet as ft
from openpyxl import Workbook
from datetime import datetime

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'DataTable in Flet with Excel'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('DataTable in Flet', size=24, color=ft.colors.WHITE)

    data_table = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_600,
        border=ft.border.all(2,ft.colors.BLUE_GREY_200),
        vertical_lines=ft.border.BorderSide(3, ft.colors.BLUE_GREY_200),
        border_radius=10,
        columns=[
            ft.DataColumn(ft.Text('ID', color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text('Name', color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text('Age', color=ft.colors.BLUE_200)),
        ],
        rows=[]
    )

    def add_row(e):
        new_row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows)+1), color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(input_name.value, color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(input_age.value, color=ft.colors.WHITE))
            ]
        )
        data_table.rows.append(new_row)
        input_name.value = ''
        input_age.value = ''
        page.update()
    
    def save_excel(e):
        wb = Workbook()
        ws = wb.active
        ws.title = 'Data of Data Base'
        ws.append(['ID', 'Name', 'Age'])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])

            date_time = datetime.now().strftime(r'%Y&m%d_%H%M%S')
            file_name = fr'DataTable in flet with Excel/DataTable.py{date_time}_data_table.xlsx'

            wb.save(file_name)


    input_name = ft.TextField(label='Name',
                              bgcolor=ft.colors.BLUE_GREY_700,
                              color=ft.colors.WHITE)

    input_age = ft.TextField(label='Age',
                              bgcolor=ft.colors.BLUE_GREY_700,
                              color=ft.colors.WHITE)

    add_button = ft.ElevatedButton('Add', on_click=add_row,
                                    bgcolor=ft.colors.BLUE,
                                    color=ft.colors.WHITE)

    save_button = ft.ElevatedButton('Save in Excel', on_click=save_excel,
                                    bgcolor=ft.colors.GREEN,
                                    color=ft.colors.WHITE)

    input_container = ft.Row(
        controls=[input_name, input_age, add_button, save_button],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(titulo, data_table, input_container)

ft.app(target=main)