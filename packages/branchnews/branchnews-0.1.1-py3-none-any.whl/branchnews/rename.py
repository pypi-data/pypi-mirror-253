import argparse
import subprocess

import click

from .util import get_frag_dir_and_config, percent_decode


@click.command(name='rename')
@click.option('--dry', is_flag=True, help="Dry run. Just say what would happen.")
def main(dry=False):
    """
    Rename news fragment files.

    Rename news fragment files, changing names like USER.BRANCH.bug.branchnews.txt
    to instead be of the form 12345.bug.txt, where the number denotes the
    PR in which this branch was merged.
    """
    fragments_directory, _ = get_frag_dir_and_config()
    filepaths = list(fragments_directory.iterdir())

    no_match = []
    planned_renames = []
    for filepath in filepaths:
        filename = filepath.name
        parts = filename.split('.')
        if len(parts) != 5 or parts[2] != 'branchnews':
            continue

        username, pct_enc_branch, _, news_type, ext = parts
        branch = percent_decode(pct_enc_branch)

        regex = rf'Merge pull request #\d+ from {username}/{branch}$'
        cmd = f'git log -P --format=%s --max-count=1 --grep="{regex}"'
        commit_title = subprocess.check_output(cmd, shell=True).decode().strip()
        if not commit_title:
            no_match.append(filename)
            continue

        PR = commit_title.split()[3][1:]
        newname = f'{PR}.{news_type}.{ext}'
        newpath = fragments_directory/newname
        planned_renames.append((filepath, newpath))

    print(
        f'Found {len(no_match) + len(planned_renames)} fragment files that should be renamed.\n'
        f'Of these, found PR numbers for '
        f'{f"only {len(planned_renames)}" if no_match else f"all {len(planned_renames)}"}.'
    )

    if planned_renames:
        print(f'Planned renames:' if dry else 'Renaming...')
        for oldpath, newpath in planned_renames:
            action = f'Rename {oldpath.name} --> {newpath.name}'
            print(action)
            if not dry:
                oldpath.rename(newpath)

    if no_match:
        print(f'Could not find PR number for {len(no_match)} files:')
        for filename in no_match:
            print('  ', filename)

    if planned_renames and not dry:
        # Stage the changes, but leave the commit to the user.
        subprocess.call(['git', 'add', str(fragments_directory)])
        print('\n*** Remember to commit the changes before running towncrier!\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rename release notes files.')
    parser.add_argument('-d', '--dry', help='do a dry run', action='store_true')
    args = parser.parse_args()
    main(dry=args.dry)
