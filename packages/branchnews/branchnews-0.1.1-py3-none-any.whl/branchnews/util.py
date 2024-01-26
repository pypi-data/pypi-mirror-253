import pathlib
import urllib.parse

import click

from towncrier.create import load_config_from_options


def get_frag_dir_and_config():
    """
    Get the fragments directory and towncrier config object.

    :return: pair (pathlib.Path, towncrier config object)
    """
    base_directory, config = load_config_from_options(None, None)
    if not config.directory:
        raise click.UsageError(
            "A configured towncrier directory is required."
            " See https://towncrier.readthedocs.io/en/stable/tutorial.html#configuration"
        )
    fragments_directory = pathlib.Path(base_directory) / config.directory
    return fragments_directory, config


def percent_encode(text):
    """
    The `quote` functions in `urllib.parse` never encode the chars '_.-~'
    Of these, we don't want dots or tildes in filenames, so we take care to
    percent-encode these manually.
    """
    no_dots_or_tildes = text.replace('.', '%2E').replace('~', '%7E')
    return urllib.parse.quote_plus(no_dots_or_tildes)


def percent_decode(text):
    """
    Reverse the action of `percent_encode()`.
    """
    unquoted = urllib.parse.unquote_plus(text)
    return unquoted.replace('%2E', '.').replace('%7E', '~')
