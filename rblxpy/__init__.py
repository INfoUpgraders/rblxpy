import urllib.request, json

class Users:

    def __init__(self, username):
        self.username = username

    def get_user(self):
        with urllib.request.urlopen(f"http://api.roblox.com/users/get-by-username?username={self.username}") as url:
            data = json.loads(url.read().decode())
        return data

print(Users.get_user(Users("INfoUpgradersYT")))
