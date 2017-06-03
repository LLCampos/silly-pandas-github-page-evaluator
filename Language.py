from github3 import GitHub
import User


class Language:

    def __init__(self, name, additions, deletions, commits_nb, repositories):
        self.name = name
        self.additions = additions
        self.deletions = deletions
        self.commits_nb = commits_nb
        self.repositories = repositories

    def update_language(self, my_file, repositories):
        self.additions += my_file.get('additions')
        self.deletions += my_file.get('deletions')
        self.commits_nb += 1
        self.repositories = self.repositories.append(repositories)
