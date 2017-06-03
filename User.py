import github3
import FilenameToLanguage
from Language import Language


class User:

    def __init__(self, username):
        self.session = github3.GitHub()
        user = self.session.user(username)
        if type(user) is github3.users.User:
            self.username = username
            self.repositories = self.make_repos()
            self.number_repos = len(self.repositories)
            self.languages = self.make_languages()
            self.issues = self.count_issues()
            self.pull_request = self.count_pull_requests()
            self.name = user.name
            self.email = user.email
            self.location = user.location
            self.avatar_url = user.avatar_url
            self.follower_count = user.followers_count
        else:
            raise ValueError('User does not exist')

    # returns all user repositories sorted by the last modified date
    def make_repos(self):
        repos = self.session.repositories_by(self.username)
        return sorted(repos, key=lambda repos: repos.last_modified)

    # returns user commits
    def get_commits(self):
        commits = []
        for repo in self.repositories:
            repo_commits = repo.commits(author=self.username)
            for commit in repo_commits:
                commits.append(repo.commit(commit.sha))
        return commits

    # returns a list of languages associated with the given user's commits and the corresponding number of added
    # and deleted lines as well as the number of commits and repositories the language appears on
    def make_languages(self):
        commits = self.get_commits()
        languages = []
        for commit in commits:
            files = commit.files
            for my_file in files:
                language_name = FilenameToLanguage.FilenameToLanguage(my_file.get('filename')).language
                if language_name is not None:
                    if language_name not in map(lambda language: language.name, languages):
                        lang_repos = self.get_repos_using_language(language_name)
                        languages.append(Language(language_name, my_file.get('additions'), my_file.get('deletions'), lang_repos))
                    else:
                        language = filter(lambda language: language.name == language_name, languages)[0]
                        language.update_language(my_file)
        return languages

    # returns the repositories of the user that contain the language
    def get_repos_using_language(self, language):
        lang_repos = []
        for repo in self.repositories:
            languages = repo.languages()
            if language in [language_name for language_name, number_of_lines in languages]:
                lang_repos.append(dict([(repo.name, repo.url)]))
        return lang_repos

    def count_issues(self):
        issues = 0
        for repo in self.repositories:
            issues += self.count(repo.issues())
        return issues

    def count_pull_requests(self):
        pull_requests = 0
        for repo in self.repositories:
            pull_requests += self.count(repo.pull_requests())
        return pull_requests

    @staticmethod
    def count(iterator):
        return sum(1 for _ in iterator)
