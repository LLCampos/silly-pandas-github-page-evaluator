import github3
import FilenameToLanguage
import Language
class User:

    def __init__(self, username):
        self.session = github3.GitHub()
        user = self.session.user(username)
        if type(user) is github3.users.User:
            self.username = username
            self.repositories = self.make_repos()
            self.languages = self.make_languages()
            self.issues = self.count_issues()
            self.pull_request = self.count_pull_requests()
            self.name = user.name
            self.location = user.location
            self.avatar_url = user.avatar_url
            self.follower_count = user.follower_countz
        else:
            raise ValueError('User does not exist')

    # returns all user repositories sorted by the last modified date
    def make_repos(self):
        repos = self.session.repositories_by(self.username)
        return sorted(repos, key = lambda repos: repos.last_modified)

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
                language = FilenameToLanguage.FilenameToLanguage(my_file.get('filename')).language
                if language is not None:
                    lang_repos = self.repositories(language)
                    if language not in languages:
                        languages.append(Language(language, my_file.get('additions'), my_file.get('deletions'), 1, lang_repos))
                    else:
                        languages.index(language).update_language(my_file, lang_repos)
        return languages

    # returns the repositories of the user that contain the language language
    def repositories(self, language):
        lang_repos = []
        for repo in self.repositories:
            languages = repo.languages
            if language in languages:
                lang_repos.append(dict([(repo.name, repo.url, repo.)]))
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
