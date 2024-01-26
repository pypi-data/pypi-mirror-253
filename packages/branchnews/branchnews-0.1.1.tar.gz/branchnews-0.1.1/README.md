`branchnews` helps you use branch-based file names with `towncrier`.
It is designed for use with GitHub, but can probably work with other collaboration
platforms as well.

If you are not already familiar with [towncrier](https://pypi.org/project/towncrier/),
it is a great tool for generating changelogs, based on *news fragment files*.

However, a difficulty arises if you want
to record a news fragment for a PR (pull request) that does not correspond to an
existing issue.
In such cases, it is hard to choose a name for the fragment file while preparing
the PR, because you do not know the number the PR will receive, until after it has
already been opened.

The solution provided by `branchnews` is to let you instead record the fragment
under a filename based on your GitHub username and the name of your topic branch,
like this:

```
USERNAME.BRANCHNAME.branchnews.NEWS_TYPE.txt
```

The

```commandline
$ branchnews create
```

command helps you generate this file.

Later, when you are ready to generate a changelog with `towncrier`, first use the

```commandline
$ branchnews rename
```

command to automatically rename the fragment files, so that they now incorporate
the correct PR numbers.

## Requirements

The `$ branchnews rename` command uses `git log` in order to
associate `USERNAME/BRANCHNAME` combinations
with the PR numbers that were eventually assigned. In order for this to work, you must
observe the following rules in your development process:

* Each time a PR is merged, you must accept the standard GitHub merge commit message of the form,

  ```
  Merge pull request #NUMBER from USERNAME/BRANCHNAME
  ```

* No single GitHub `USERNAME` may reuse a given `BRANCHNAME` for two or more separate
  PRs, within a given release cycle. (This is probably just good practice anyway.)


Furthermore, for the sake of simplicity, the `$ branchnews create` command requires you to
have a *configured* fragments directory, in your `towncrier` config. That is,

* Your `towncrier` config must define the `directory` key. 

See https://towncrier.readthedocs.io/en/stable/configuration.html. 


## Usage

### Configuration

`branchnews` does not currently support any configuration options of its own, but it
does rely on your `towncrier` [configuration](https://towncrier.readthedocs.io/en/stable/configuration.html).
As stated above, you must at least define the `directory` key.

Furthermore, you probably *should* define the `issue_format` key in the way
indicated [here](https://towncrier.readthedocs.io/en/stable/markdown.html), i.e.
like this:

```toml
issue_format = "[#{issue}](https://github.com/example/my-project/issues/{issue})"
```

so that issue and PR numbers link to the appropriate pages at GitHub.
(If you didn't want your  changelog entries to link to those pages, there was probably no
reason to be using `branchnews` in the first place.)

Note: The `issue_format` suggested above will work for both issues *and* PRs.
GitHub automatically redirects URLs ending with `issues/NNN` to `pull/NNN` when the number
in fact belongs to a PR, not an issue.

### Preparing a PR

When any contributor to your project is preparing a PR, they should generate a news
fragment file by invoking

```commandline
$ branchnews create
```

and then following the on-screen prompts.

The very first prompt asks if there is an associated issue number. This is so that this one
procedure can be used whether there is an issue number or not.

A session for which there *is* an associated issue number might look like this:

```
$ branchnews create
Issue number (leave blank to use branch name instead): 1234
What type of news is it?
(0): security
(1): removed
(2): deprecated
(3): added
(4): changed
(5): fixed
Type: 3
Created 1234.added.txt
Please edit the file to provide a release note.
```

(The menu of alternatives for the news *type* is generated directly from your
`towncrier` config.)

A session for which there is *not* an associated issue number might look like this:

```
$ branchnews create
Issue number (leave blank to use branch name instead): 
GitHub username: example
Branch name is fix-that-pesky-bug
What type of news is it?
(0): security
(1): removed
(2): deprecated
(3): added
(4): changed
(5): fixed
Type: 5
Created example.fix-that-pesky-bug.branchnews.fixed.txt
Please edit the file to provide a release note.
```

After generating the file, the contributor should edit it, recording the desired
news entry, and then `git commit` the file, before opening a PR.

Note that Git allows a wide variety of symbols to appear in branch names (including
slashes and dots), and this is no problem with `branchnews`.
The branch name is percent-encoded before becoming a segment of the generated filename.


### Generating a change log

Before you can generate your changelog with `towncrier`, first use

```commandline
$ branchnews rename
```

to automatically rename all the fragment files having names of the form
`USERNAME.BRANCHNAME.branchnews.NEWS_TYPE.txt`. After renaming, they will instead
have names of the form `NNN.NEWS_TYPE.txt`, where the correct PR number `NNN` has
been obtained using `git log`.

Remember, this will only work if you have followed the rules stated above,
under [Requirements](#requirements). In case there were any lapses (maybe one time
you failed to accept the standard merge commit message for a PR), then the
`branchnews rename` command will still automatically rename all the files it can,
and it will also print a list of those files that it could not rename. Using the
`USERNAME` and `BRANCHNAME` for any such files, you should be able to manually
track down the right PR numbers.

The `branchnews rename` command will also automatically *stage* the renames, but
it will not perform a commit. You should do the commit manually (maybe with a
simple commit message like, "Rename branchnews files").

After committing the renames, you can proceed to use `towncrier` as normal.
