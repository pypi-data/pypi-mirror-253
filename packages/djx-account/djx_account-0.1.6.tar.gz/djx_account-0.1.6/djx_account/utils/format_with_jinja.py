import os
import pathlib

from jinja2 import Environment, FileSystemLoader


def format_with_jinja(data, template_src):
    base_folder = pathlib.Path(__file__).resolve().parent.parent
    with open(os.path.join(base_folder, template_src), "r", encoding="utf-8") as f:
        template = Environment(loader=FileSystemLoader(base_folder)).from_string(f.read())

    result = template.render(**data)
    return result
