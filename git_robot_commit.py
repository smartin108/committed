""" git_robot_commit.py
"""

import os
import subprocess


def get_list_of_root_folders():
    """ return catalog of enumerated git repo roots
    """
    # return [r'C:\Users\Z40\Documents\git', r'C:\Users\Z40\Documents\batch',r"C:\Users\Z40\AppData\Roaming\REAPER\Effects\smartin"]
    return[r"C:\Users\Z40\Documents\git\AudioAnalysis"]


def filter_repo_subpaths():
    """ return True or False: folder is (True) considered a legitimate candidate as a repo top-level folder, or (False) not so
    """


def get_list_of_repos(root_folder:str):
    """ return a list of paths at and below <root_folder> that might contain a git repo
    """
    # return [r'C:\Users\Z40\Documents\git', r'C:\Users\Z40\Documents\batch',r"C:\Users\Z40\AppData\Roaming\REAPER\Effects\smartin"]
    result = set()
    for p, d, f in os.walk(root_folder):
        if '.git' in p:
            test = False
            # print(f'rejected: {(p,d,f)}')
        elif '.git' in d:
            test = True
            result.add(p)
            # print(f'accepted: {(p,d,f)}')
        else:
            test = False
            # print(f'rejected: {(p,d,f)}')
    # print(f'\n{result}')
    return result


def commit_repo(path_to_git_project:str, commit_message:str='"automatic commit"'):
    """
    """

    def shell_command(command_to_execute:str):
        full_shell_command = f'cmd.exe /c {command_to_execute}'
        return subprocess.run(full_shell_command, capture_output=True, text=True, shell=True)

    cd_command = f'cd {path_to_git_project}\\'
    git_add_command = 'git add .'
    git_commit_command = f'git commit -m {commit_message}'

    result = [shell_command(cd_command)]
    result.append(shell_command(git_add_command))
    result.append(shell_command(git_commit_command))
    # print(result)

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
