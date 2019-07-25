# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at [here](https://github.com/mmphego/read_time/issues).

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Read Time could always use more documentation,
whether as an official Read Time docs,
in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue [here](https://github.com/mmphego/read_time/issues).

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up read_time for local development.

1.  Fork the read_time repo on GitHub.
2.  Clone your fork locally:
    ```bash
        $ git clone git@github.com:your_name_here/read_time.git
    ```

3.  Install your local copy into a virtualenv. Assuming you have
    `virtualenvwrapper` installed, this is how you set up your fork for
    local development:
    ```bash
        mkvirtualenv read_time
        cd read_time/
        python setup.py develop
    ```

4.  Create a branch for local development:
    ```bash
        git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass `flake8`
    and the tests, and then use `black` to format:
    ```bash
        flake8 read_time
        python setup.py test or py.test
        black -l 90 read_time
    ```
    To get `flake8` and `black`, just pip install them into your `virtualenv`.

6.  Commit your changes and push your branch to GitHub:
    ```bash
        git add .
        git commit --sign-off -m "Your detailed description of your changes."
        git push origin name-of-your-bugfix-or-feature
    ```

7.  Submit a pull request through the GitHub website.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3.  The pull request should work for Python 3.6+, and
    for PyPi. Check [travis-ci](https://travis-ci.org/mmphego/read_time/pull_requests) and make sure that the tests pass for supported Python version(s).

### Tips

To run a subset of tests:
```bash
python3 -m unittest [tests.test]()read_time
```

## Deploying

A reminder for the maintainers on how to publish. Make sure all your
changes are committed (including an entry in CHANGELOG.md).
Then run:
    ```bash
    python setup.py publish
    ```