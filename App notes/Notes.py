#App para guardar notas
import flet as ft

def main(page: ft.Page):
    page.title = 'Sticky note board'
    page.padding = 25
    page.theme_mode = 'light'
    page.bgcolor = ft.colors.BLUE_GREY_800
    note = ft.TextField(value='My first note', multiline=True)
    
    def add_note(e):
        new_note = create_note('New note')
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):
        note_content = content=ft.TextField(value=text, 
                                            multiline=True,
                                            bgcolor=ft.colors.BLUE_GREY_50)
        note = ft.Container(
            content=ft.Column([note_content, ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: delete_note(note))]),
            width=200,
            height=200,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=10,
            padding=10
        )

        return note
    
    
    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10
    )

    notes = [
    
    ]

    for note in notes:
        grid.controls.append(create_note(note))
    
    #note = create_note('My first note')
    #note2 = create_note('My second note')

    page.add(
        ft.Row([
            ft.Text('MY NOTES', size=24, weight='bold', color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.WHITE)
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN), grid
    )

ft.app(target=main)