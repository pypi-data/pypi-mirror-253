import requests

from . import exceptions


class User:
    def __init__(self, username, session=None):
        self.username = username
        self.session = session
        self.id = None
        self.country = None
        self.join_date = None
        self.about_me = None
        self.wiwo = None
        if self.session:
            self._headers = self.session.headers
            self._cookies = self.session.cookies
        else:
            self._headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/75.0.3770.142 Safari/537.36",
                "x-csrftoken": "a",
                "x-requested-with": "XMLHttpRequest",
                "referer": "https://scratch.mit.edu"
            }
            self._cookies = {}

    def __str__(self):
        return str(self.username)

    def update(self):
        response = requests.get(f"https://api.scratch.mit.edu/users/{self.username}").json()
        try:
            self.id = response["id"]
        except KeyError:
            raise exceptions.UserNotFound()
        self.country = response["profile"]["country"]
        self.join_date = response["history"]["joined"]
        self.about_me = response["profile"]["bio"]
        self.wiwo = response["profile"]["status"]

    def get_follower_count(self):
        count = requests.get(
            f"https://scratch.mit.edu/users/{self.username}/followers/",
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/75.0.3770.142 Safari/537.36",
                "x-csrftoken": "a",
                "x-requested-with": "XMLHttpRequest",
                "referer": "https://scratch.mit.edu",
                "Cookie": "scratchcsrftoken=a;scratchlanguage=en;"
            }
        ).text
        count = count.split("Followers (")[1]
        count = count.split(")")[0]
        return int(count)

    def get_following_count(self):
        count = requests.get(
            f"https://scratch.mit.edu/users/{self.username}/following/",
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/75.0.3770.142 Safari/537.36",
                "x-csrftoken": "a",
                "x-requested-with": "XMLHttpRequest",
                "referer": "https://scratch.mit.edu",
                "Cookie": "scratchcsrftoken=a;scratchlanguage=en;"
            }
        ).text
        count = count.split("Following (")[1]
        count = count.split(")")[0]
        return int(count)

    def get_followers(self, limit=40, offset=0):
        if limit > 40:
            limit = 40
        response = requests.get(
            f"https://api.scratch.mit.edu/users/{self.username}/followers?limit={limit}&offset={offset}").json()
        followers = []
        for user in response:
            try:
                followers.append(User(username=user["username"]))
            except Exception:
                raise exceptions.ParseError("Failed to parse", user)
        return followers

    def get_following(self, limit=40, offset=0):
        if limit > 40:
            limit = 40
        response = requests.get(
            f"https://api.scratch.mit.edu/users/{self.username}/following?limit={limit}&offset={offset}").json()
        following = []
        for user in response:
            try:
                following.append(User(username=user["username"]))
            except Exception:
                raise exceptions.ParseError("Failed to parse", user)
        return following

    def get_project_count(self):
        text = requests.get(
            f"https://scratch.mit.edu/users/{self.username}/projects/",
            headers={
                "x-csrftoken": "a",
                "x-requested-with": "XMLHttpRequest",
                "Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
                "referer": "https://scratch.mit.edu",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/75.0.3770.142 Safari/537.36"
            },
        ).text
        text = text.split("Shared Projects (")[1]
        text = text.split(")")[0]
        return int(text)


def get_user(username):
    user = User(username=username)
    user.update()
    return user
