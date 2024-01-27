from . import exceptions
from . import user

import requests


class PartialProject:
    def __init__(self, project_id, session=None):
        self.id = project_id
        self.session = session
        self.project_token = None
        self.shared = None


class Project(PartialProject):
    def __init__(self, project_id, session=None):
        super().__init__(project_id, session)
        self.url = None
        self.title = None
        self.author = None
        self.created = None
        self.share_date = None
        self.instructions = None
        self.notes = None
        self.favorites = None
        self.loves = None
        self.remix_count = None
        self.views = None

    def __str__(self):
        return self.title

    def update(self):
        response = requests.get(f"https://api.scratch.mit.edu/projects/{self.id}").json()
        try:
            self.id = response["id"]
        except KeyError:
            raise exceptions.ProjectNotFound()
        self.url = "https://scratch.mit.edu/projects/" + str(self.id)
        self.title = response["title"]
        self.author = response["author"]["username"]
        self.created = response["history"]["created"]
        self.share_date = response["history"]["shared"]
        self.instructions = response["instructions"]
        self.notes = response["description"]
        self.favorites = response["stats"]["favorites"]
        self.loves = response["stats"]["loves"]
        self.remix_count = response["stats"]["remixes"]
        self.views = response["stats"]["views"]
        try:
            self.project_token = response["project_token"]
        except KeyError:
            self.project_token = None
        if "code" in list(response.keys()):
            return False
        else:
            return True

    def get_author(self):
        return user.get_user(self.author)

    def get_comments(self, limit=40, offset=0):
        comments = []
        while len(comments) < limit:
            res = requests.get(
                f"https://api.scratch.mit.edu/users/{self.author}/projects/{self.id}/comments/?limit={min(40, limit - len(comments))}&offset={offset}").json()
            if len(res) != 40:
                break
            offset += 40
            comments = comments + res
        return comments


def get_project(project_id):
    project = Project(project_id=int(project_id))
    update = project.update()
    if not update:
        project = PartialProject(project_id=int(project_id))
    return project
