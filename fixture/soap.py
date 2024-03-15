from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
            l = []
            for i in range(len(projects)):
                    id = projects[i].id
                    name = projects[i].name
                    status = projects[i].status.name
                    enabled = projects[i].enabled
                    view_status = projects[i].view_state.name
                    description = projects[i].description
                    l.append(Project(id=id, name=name, status=status, enabled=enabled, view_status=view_status,
                                     description=description))
            return l
        except WebFault as fault:
            print(fault)
            return False
