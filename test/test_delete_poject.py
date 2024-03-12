from model.project import Project
from random import randrange
import string
import random


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name=random_string("Тест проект", 15), description="Новый проект для тестирования"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index+1] = []
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
