import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_100
    page.title = 'To Do List'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text('My To Do List With Flet', 
                     size=30, weight=ft.FontWeight,color=ft.colors.INDIGO_500)

    def add_task(e):
        if task_field.value:
            task = ft.ListTile(
                title=ft.Text(task_field.value),
                leading=ft.Checkbox(on_change=select_task)
            )
            tasks.append(task)
            task_field.value = ''
            update_list()

    def select_task(e):
        selected = [t.title.value for t in tasks if t.leading.value]
        selected_task.value = 'Selected task: '+', '.join(selected)
        page.update()

    def update_list():
        task_list.controls.clear()
        task_list.controls.extend(tasks)
        page.update()

    task_field = ft.TextField(hint_text='Write a new task', color=ft.colors.INDIGO_500)
    
    btn_add = ft.FilledButton('Add task', on_click=add_task)
    
    task_list = ft.ListView(expand=1, spacing=3)

    tasks = []

    selected_task = ft.Text('', size=20, weight=ft.FontWeight.BOLD)
    
    
    page.add(title, task_field,btn_add,task_list,selected_task)

ft.app(target=main)