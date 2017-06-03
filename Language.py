class Language:

    def __init__(self, name, additions, deletions, repositories):
        self.name = name
        self.safe_name = name.replace(' ', '_')
        self.additions = additions
        self.deletions = deletions
        self.commits_number = 1
        self.repositories = repositories

    def update_language(self, my_file):
        self.additions += my_file.get('additions')
        self.deletions += my_file.get('deletions')
        self.commits_number += 1
