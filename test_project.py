from project import add_task, load_tasks, mark_complete, save_tasks, delete_task, list_tasks


def main():
    test_add_task()
    test_mark_complete()
    test_load_tasks_type()
    test_save_tasks()
    test_delete_task()
    test_list_tasks()


def test_add_task():
    add_task("My test task")
    tasks = load_tasks()
    assert any(task['title'] == 'My test task' for task in tasks)


def test_mark_complete():
    add_task("Mark this complete")
    tasks = load_tasks()
    index = len(tasks) - 1

    mark_complete(index)
    tasks = load_tasks()
    assert tasks[index]['completed'] is True


def test_load_tasks_type():
    tasks = load_tasks()
    assert isinstance(tasks, list)


def test_save_tasks():
    dummy_tasks = [{"title": "dummy", "completed": False}]
    save_tasks(dummy_tasks)

    tasks = load_tasks()
    assert tasks == dummy_tasks


def test_delete_task():
    add_task("Task to delete")
    tasks = load_tasks()
    index = len(tasks) - 1

    delete_task(index)
    tasks_after_delete = load_tasks()

    assert len(tasks_after_delete) == index


def test_list_tasks():
    add_task("Taskfor print test")
    list_tasks()


if __name__ == "__main__":
    main()
