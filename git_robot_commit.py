""" git_robot_commit.py
"""

import os
import subprocess
import json


def read_repo_locations():
    locations_file = './repo_location.json'
    with open(locations_file, 'r') as f:
        d = json.load(f)
    return d


def get_list_of_root_folders():
    """ return catalog of enumerated git repo roots
    """
    # return [r'C:\Users\Z40\Documents']
    # return [r'C:\Users\Z40\Documents\git', r'C:\Users\Z40\Documents\batch',r"C:\Users\Z40\AppData\Roaming\REAPER\Effects\smartin"]
    d = read_repo_locations()
    print(d)
    return(d['locations'])


def get_list_of_repos(root_folder:str):
    """ return a list of paths at and below <root_folder> that contain a git repo
    """
    result = set()
    for p, d, _ in os.walk(root_folder):
        if '.git' in p:
            pass
        elif '.git' in d:
            result.add(p)
        else:
            pass
    return result


def commit_repo(path_to_git_project:str, commit_message:str='"automatic commit"'):
    """
    """

    def shell_command(command_to_execute:str, cwd:str=path_to_git_project):
        full_shell_command = f'cmd.exe /c {command_to_execute}'
        return subprocess.run(full_shell_command, capture_output=True, text=True, shell=True, cwd=cwd)

    git_status_command = 'git status'
    git_add_command = 'git add .'
    git_commit_command = f'git commit -m {commit_message}'
    git_log_command = 'git log'

    result = [shell_command(git_add_command)]
    result.append(shell_command(git_commit_command))
    for i in result:
        print(i)

    return result



def main():
    print('hello, world!')
    root_folders = get_list_of_root_folders()
    for path_item in root_folders:
        repos = get_list_of_repos(path_item)
        if repos:
            for r in repos:
                print(r)
                commit_repo(r)


if __name__ == '__main__':
    main()
