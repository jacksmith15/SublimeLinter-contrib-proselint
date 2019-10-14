#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jordan Suchow
# Copyright (c) 2015 Jordan Suchow
#
#

"""This module exports the Proselint plugin class."""

from SublimeLinter.lint import Linter


class Proselint(Linter):

    """Provides an interface to proselint."""

    # syntax = ('*')
    cmd = 'proselint'
    # executable = None
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 0.0.0'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): \S* (?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'pltmp'
    word_re = None
    defaults = {
        "selector": 'text.html.markdown, text.plain, text.tex.latex, comment'
    }
    # inline_settings = None
    # inline_overrides = None
    # comment_re = None
