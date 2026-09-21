import flet as ft


def main(page: ft.Page):
    page.title = "Мои задачи"

    title = ft.Text(
        "Мои задачи",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    task_input = ft.TextField(
        label="Введите задачу",
        expand=True
    )

    tasks = ft.Column()


    def add_task(e):
        text = task_input.value.strip()

        if text == "":
            return

        checkbox = ft.Checkbox(label=text)

        task_row = ft.Row(
            controls=[
                checkbox,
                ft.Button(
                    "Удалить",
                    on_click=lambda e: delete_task(task_row)
                )
            ]
        )

        tasks.controls.append(task_row)

        task_input.value = ""

        page.update()


    def delete_task(task_row):
        tasks.controls.remove(task_row)
        page.update()


    def clear_tasks(e):
        tasks.controls.clear()
        page.update()


    add_button = ft.Button(
        "Добавить",
        on_click=add_task
    )

    clear_button = ft.Button(
        "Очистить всё",
        on_click=clear_tasks
    )


    page.add(
        title,

        ft.Row(
            controls=[
                task_input,
                add_button
            ]
        ),

        tasks,

        clear_button
    )


ft.run(main)