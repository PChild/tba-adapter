import tbapy
import git
import os


class TBAA:
    def __init__(self, data_path ='../'):
        self.tba = tbapy.TBA(os.getenv("TBA_KEY"))
        self.data_path = data_path
        self.repo_location = self.data_path + 'the-blue-alliance-data/'
        self.repo = self.get_repo()

    def create_repo(self, force=False):
        if force and os.path.exists(self.repo_location):
            os.remove(self.repo_location)
        elif os.path.exists(self.repo_location):
            print('Repo already exists, skipping creation.')
        else:
            print('Cloning git repo, this may take a bit.')
            git.Git(self.data_path).clone('https://github.com/the-blue-alliance/the-blue-alliance-data.git')

    def get_repo(self):
        if not os.path.exists(self.repo_location):
            self.create_repo()
        return git.Repo(self.repo_location)

    def update_repo(self, force=False):
        if force:
            self.repo.git.clean('-xdf')
            self.repo.git.pull()
        if len(self.repo.untracked_files) == 0:
            self.repo.git.pull()




if __name__ == '__main__':
    tbaa = TBAA()

    tbaa.create_repo()
    test = tbaa.get_repo()
    print(test.remotes)

