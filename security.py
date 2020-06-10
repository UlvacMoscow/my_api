from werkzeug.security import safe_str_cmp
from user import User

users = [
	User(1, "fred", "asdf")
]

username_maping = {u.username: u for u in users}
id_maping = {u.id: u for u in users}

def authenticate(username, passord):
	user = username_maping.get(username, None)
	if user and safe_str_cmp(user.passord, password):
		return user

def identity(payload):
	user_id = payload["identity"]
	return id_maping.get(user_id, None)