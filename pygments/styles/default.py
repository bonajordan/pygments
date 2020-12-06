# -*- coding: utf-8 -*-
"""
    pygments.styles.default
    ~~~~~~~~~~~~~~~~~~~~~~~

    The default highlighting style.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class DefaultStyle(Style):
    """
    The default style (inspired by Emacs 22).
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #408080",
        Comment.Preproc:           "noitalic #BC7A00",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #FFD801", #"bold #008000", for else if elif 
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #B00040",

        Operator:                  "#FFFFFF", #666666",  + - * = 
        Operator.Word:             "bold #FFD801", #"bold #AA22FF",  in

        Name.Builtin:              "#A23BEC",   #"#008000",
        Name.Function:             "#0000FF",
        Name.Class:                "bold #0000FF",
        Name.Namespace:           "#FFFFFF", #"bold #0000FF",   from *math* import sin
        Name.Exception:            "#A23BEC",  #"bold #D2413A",  Exception AssertionError
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#A0A000",
        Name.Entity:               "bold #999999",
        Name.Attribute:            "#7D9029",
        Name.Tag:                  "bold #008000",
        Name.Decorator:            "#AA22FF",

        String:                    "bold #347C17", #"#BA2121",  strings
        String.Doc:                "italic",
        String.Interpol:           "bold #BB6688",
        String.Escape:            "bold #347C17", #"bold #BB6622", escapes within strings
        String.Regex:              "#BB6688",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#008000",
        Number:                    "#FFFFFF", #"#666666",   number; 1, 2, 3 etc...

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
