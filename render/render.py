#!/usr/bin/env python

from StringIO import StringIO
from exceptions import Exception

import yaml
import sys


def render_attr(attr):
    buffer = StringIO()
    req = "*" if attr.get("required") else ""
    specific = attr.get("specific for")
    specific = ', '.join(specific) if isinstance(specific, list) else specific
    sp = " <i><small>specific for " + specific + "</small></i>" if specific else ""
    buffer.write("{}{}{}".format(attr["name"], req, sp))

    children = attr.get("children")
    if children:
        buffer.write("<ul>")
        for ch in children:
            buffer.write("<li>{}</li>\n".format(render_attr(ch)))
        buffer.write("</ul>\n")
    return buffer.getvalue()


def render_sl(sl):
    return """<a href="{ref}">{name}</a>""".format(**sl)


def render_ont(ont):
    abbrs = ont.get("abbr")
    abbr = ", {}".format(abbrs) if abbrs else ""
    return """<a href="{}">{}{}</a>""".format(ont["ref"], ont["name"], abbr)


def render_html(doc):
    buffer = StringIO()
    buffer.write("<tr style='border-bottom: 1px solid #ddd;'>\n")
    buffer.write("<td>{}</td>\n".format(doc["section name"]))

    buffer.write("<td style='padding-top: 15px'><ul>\n")
    for attr in doc["attributes"]:
        buffer.write("<li>{}</li>\n".format(render_attr(attr)))
    buffer.write("</ul></td>")

    buffer.write("<td><ul>")
    for sl in doc["source list"]:
        buffer.write("<li>{0}</li>\n".format(render_sl(sl)))
    buffer.write("</ul></td>\n")

    buffer.write("<td><ul>")
    for ont in doc["recommended ontologies"]:
        buffer.write("<li>{0}</li>\n".format(render_ont(ont)))
    buffer.write("</ul></td>\n")

    buffer.write("</tr>\n")
    return buffer.getvalue()


def main(filename):
    with open(filename, "r") as f:
        docs = yaml.load(f)
        print "<table style='border-collapse:collapse'>"
        print "<tr><th>Section</th><th>Attributes</th><th>Source list</th><th>Recommended ontologies</th></tr>\n"
        for doc in docs["sections"]:
            print render_html(doc)
        print "</table>"


if __name__=='__main__':
    if len(sys.argv)> 1:
        main(sys.argv[1])
    else:
        raise Exception("Input argument missing. Please provide a name of the yaml file to render, e.g.\n > python render.py miappe.yaml")
