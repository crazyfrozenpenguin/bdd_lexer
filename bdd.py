# -*- coding: utf-8 -*-
"""
    pygments.lexers.bdd
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for BDD features and stories.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ['BDDLexer']

class BDDLexer(RegexLexer):
    """
    For BDD stories or features.
    """
    name = 'BDD'
    aliases = ['bdd','feature','story', 'stories']
    filenames = ['*.bdd', '*.story', '*.feature', '*.stories']

    tokens = {
        'root': [
            (r'^(\s*(?:Feature|Scenario|Scenario Outline|Background|Examples):)(.*)$', bygroups(Generic.Deleted, Text)),
            (r'^\s*Meta:$', Generic.Heading),
            (r'^(\s*@verifies )(.*)$', bygroups(Generic.Inserted, Text)),
            (r'^(\s*(?:Given|When|Then|And|On|It should|Should))', Generic.Subheading, 'rule'),
            (r'^(.*)( should )(.*)$', bygroups(Text, Generic.Subheading, Text)),
            (r'.*\n', Text),
        ],
        'rule': [
            (r'(.*)(\<\w+\>)(.*)', bygroups(Text, Generic.Subheading, Text)),
            (r'(.*)(\$\w+)(.*)', bygroups(Text, Generic.Subheading, Text)),
            (r'.*\n', Text, '#pop'),
        ]
    }

