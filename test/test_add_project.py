from model.project import Project
import random
import string


def test_add_project(app):
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_project_list()
    project = Project(name=random_string("Тест проект", 15), description="Новый проект для тестирования")
    app.project.create(project)
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


