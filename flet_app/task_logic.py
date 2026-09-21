def add_task(tasks, task):
    task = task.strip()

    if task == "":
        return tasks

    tasks.append(task)

    return tasks


def delete_task(tasks, task):
    if task in tasks:
        tasks.remove(task)

    return tasks


def clear_tasks(tasks):
    tasks.clear()

    return tasks