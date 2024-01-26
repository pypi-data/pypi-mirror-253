import subprocess

import click

from .util import get_frag_dir_and_config, percent_encode


@click.command(name='create')
def main():
    """
    Create a news fragment.

    Enter an issue number, or let the filename be based on your GitHub username and
    the current branch name.
    """
    fragments_directory, config = get_frag_dir_and_config()

    filename_parts = []

    issue_num = input("Issue number (leave blank to use branch name instead): ")

    if issue_num:
        filename_parts.append(issue_num)
    else:
        username = input("GitHub username: ")
        branch = subprocess.check_output(["git", "branch", "--show-current"]).decode().strip()
        print("Branch name is", branch)
        pct_enc_branch = percent_encode(branch)
        filename_parts.extend([username, pct_enc_branch, 'branchnews'])

    types_lookup = {i: t for i, t in enumerate(config.types)}
    print('What type of news is it?')
    for i, t in types_lookup.items():
        print(f'({i}): {t}')
    type_index = input("Type: ")
    try:
        i = int(type_index)
        news_type = types_lookup[i]
    except (ValueError, KeyError):
        raise click.UsageError('Invalid choice!')

    filename_parts.append(news_type)
    filename_parts.append('txt')

    filename = '.'.join(filename_parts)
    filepath = fragments_directory / filename
    template = "# Please replace this line with a release note."
    with open(filepath, "w") as f:
        f.write(template)

    print("Created", filename)
    print("Please edit the file to provide a release note.")


if __name__ == '__main__':
    main()
