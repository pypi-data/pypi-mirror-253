import json
import warnings

import requests

from . import exceptions, user


class Session:
    def __init__(self, username, session_id):
        self.username = username
        self.session_id = session_id
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/75.0.3770.142 Safari/537.36",
            "x-csrftoken": "a",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://scratch.mit.edu"
        }
        self.cookies = {
            "scratchsessionsid": self.session_id,
            "scratchcsrftoken": "a",
            "scratchlanguage": "en"
        }

        self._add_csrftoken()
        self._add_xtoken()

    def get_current_user(self):
        user.get_user(self.username)

    def _add_csrftoken(self):
        headers = requests.get("https://scratch.mit.edu/csrf_token/").headers
        csrftoken = headers["Set-Cookie"].split("scratchcsrftoken=")[1].split(";")[0]

        self.headers["x-csrftoken"] = csrftoken
        self.cookies["scratchcsrftoken"] = csrftoken

    def _add_xtoken(self):
        try:
            response = requests.post("https://scratch.mit.edu/session", headers=self.headers,
                                     cookies=self.cookies).json()
            self.username = response["user"]["username"]
            self.xtoken = response["user"]["token"]
            self.email = response["user"]["email"]
            self.new_scratcher = response["permissions"]["new_scratcher"]
            self.banned = response["user"]["banned"]

            self.headers["X-Token"] = self.xtoken

            if self.banned:
                warnings.warn(f"Warning: The account {self.username} is banned!")
        except KeyError:
            warnings.warn("Warning: Cannot fetch XToken!")


def login(username, password):
    data = json.dumps({"username": username, "password": password})
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/75.0.3770.142 Safari/537.36",
        "x-csrftoken": "a",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://scratch.mit.edu",
        "Cookie": "scratchcsrftoken=a;scratchlanguage=en;"
    }
    response = requests.post("https://scratch.mit.edu/login/", data=data, headers=headers)
    session_id = response.headers["Set-Cookie"]
    quote_pos = session_id.find('"')

    if quote_pos == -1:
        raise exceptions.LoginError(
            "Incorrect username or password. If you're using replit.com or other online IDE, Scratch has probably "
            "banned their IP address.")

    session_id = session_id[quote_pos + 1:session_id.find('"', quote_pos + 1)]
    return Session(username, session_id)
