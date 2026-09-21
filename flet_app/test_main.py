from task_logic import add_task, delete_task, clear_tasks


def test_add_task():
    tasks = []

    add_task(tasks, "Изучить Python")

    assert tasks == ["Изучить Python"]


def test_add_empty_task():
    tasks = []

    add_task(tasks, "")

    assert tasks == []


def test_delete_task():
    tasks = ["Python", "Flet"]

    delete_task(tasks, "Python")

    assert tasks == ["Flet"]


def test_clear_tasks():
    tasks = ["Python", "Flet"]

    clear_tasks(tasks)

    assert tasks == []