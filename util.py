import requests

__author__ = 'Sam Redmond'
# Wrapper for Github Repository objects that only contain relevant fields
class Repository():
	# Expects data to be a JSON object returned by Github's Repo API
	def __init__(self, data):
		self.id = data['id']
		self.full_name = data['full_name']
		self.description = data['description']
		self.updated_at = data['updated_at']
		self.commits_url = data['commits_url']

	def __repr__(self):
		return "<Repo {0}: {1}>".format(self.id, self.full_name)

class Commit():
	def __init__(self, data):
		self.sha = data['sha']
		self.author = data['commit']['author']['name']
		self.date = data['commit']['author']['date']
		self.message = data['commit']['message']

	def __repr__(self):
		return "<Commit {0}: {1}>".format(self.sha[:8], self.message)

BASE_URL = "https://api.github.com"
REPOS_ENDPOINT = '/users/{username}/repos'
# Caps at 30 repos
def get_repos_by_username(username='sredmond'):
	url = BASE_URL + REPOS_ENDPOINT.format(username=username)
	print url
	r = requests.get(url)
	if r.status_code == 200:
		if True: # No rate limiting error TODO
			repos = r.json()
			for repodata in repos:
				repo = Repository(repodata)
				# print repo.full_name
				# print repo.description
				print repo
		else:
			pass
	else:
		print "Error: {0}".format(r.status_code)

get_repos_by_username('sredmond')
# get_repos_by_username('rkaplan')
# get_repos_by_username('google')

def get_commits()
