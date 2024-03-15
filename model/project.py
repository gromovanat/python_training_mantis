from sys import maxsize


class Project:

    def __init__(self, name=None, id=None, status=None, inherit_global_cat=None, view_status=None, description=None, enabled=None ):
        self.name = name
        self.status = status
        self.inherit_global_cat = inherit_global_cat
        self.view_status = view_status
        self.description = description
        self.id = id
        self.enabled = enabled

    def __repr__(self):
        return "%s:%s; %s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
