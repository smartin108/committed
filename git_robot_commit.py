""" git_robot_commit.py
"""

import os
import subprocess


def get_list_of_repos():
    """ returns list of paths that should have git report
    """
    return [r'C:\Users\Z40\Documents\git', r'C:\Users\Z40\Documents\batch',r"C:\Users\Z40\AppData\Roaming\REAPER\Effects\smartin"]


def commit_repo(path_to_git_project:str, commit_message:str='"automatic commit"'):
    """
    """

    def shell_command(command_to_execute:str):
        full_shell_command = f'cmd.exe /c {command_to_execute}'
        return subprocess.run(full_shell_command, capture_output=True, text=True, shell=True)

    cd_command = f'cd {path_to_git_project}\\'
    git_add_command = 'git add .'
    git_commit_command = f'git commit -m {commit_message}'

    results = [shell_command(cd_command)]
    print(results)
    results = [shell_command(git_add_command)]
    print(results)
    results.append(shell_command(git_commit_command))
    print(results)

    return results



def main():
    print('hello, world!')
    repos = get_list_of_repos()
    for r in repos:
        commit_repo(r)


if __name__ == '__main__':
    main()
