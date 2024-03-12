from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php")):
            wd.find_element_by_link_text("Manage").click()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            self.open_manage_page()
            wd.find_element_by_link_text("Manage Projects").click()


    def open_new_project_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        self.open_new_project_form()
        self.fill_project_form(project)

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        l = []
        number = len(wd.find_elements_by_xpath('//table[@class="width100"][2]//tbody//tr'))
        for n in range(3, number+1):
            id = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').get_attribute(
                'href')
            id = str(id).split("=")[1]
            name = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').text
            status = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[2]').text
            inherit_global_cat = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[3]').text
            view_status = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[4]').text
            description = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[5]').text
            l.append(Project(id=id, name=name, status=status, inherit_global_cat=inherit_global_cat,
                                    view_status=view_status, description=description))
        return list(l)

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{index+3}]//td//a').click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
