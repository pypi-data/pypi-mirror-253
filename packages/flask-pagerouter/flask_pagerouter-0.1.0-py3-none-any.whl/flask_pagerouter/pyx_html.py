import html
from typing import Callable

def div_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f"<div{attributes}>{html_inner_content}</div>"

    return tag


def p_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<p{attributes}>{html_inner_content}</p>"

    return tag


def a_(
    href_: str = "",
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    href_ = html.escape(href_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if href_:
        attributes += f' href="{href_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<a{attributes}>{html_inner_content}</a>"

    return tag


def img_(
    src_: str = "",
    alt_: str = "",
    class_: str = "",
    id_: str = "",
    style_: str = "",
    width_: int = 600,
    height_: int = 400,
    attributes_: dict = {}
) -> str:

    src_ = html.escape(src_)
    alt_ = html.escape(alt_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if src_:
        attributes += f' src="{src_}"'
    if alt_:
        attributes += f' alt="{alt_}"'
    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if height_:
        attributes += f' height="{height_}"'
    if width_:
        attributes += f' width="{width_}"'

    return f"<img{attributes}>"


def h1_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<h1{attributes}>{html_inner_content}</h1>"

    return tag


def h2_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<h2{attributes}>{html_inner_content}</h2>"

    return tag


def h3_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<h3{attributes}>{html_inner_content}</h3>"

    return tag


def h4_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}" '

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<h4{attributes}>{html_inner_content}</h4>"

    return tag


def h5_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<h5{attributes}>{html_inner_content}</h5>"

    return tag


def h6_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<h6{attributes}>{html_inner_content}</h6>"

    return tag

def ul_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<ul{attributes}>{html_inner_content}</ul>"

    return tag


def ol_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<ol{attributes}>{html_inner_content}</ol>"

    return tag


def li_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<li{attributes}>{html_inner_content}</li>"

    return tag


def span_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<span{attributes}>{html_inner_content}</span>"

    return tag


def button_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    type_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:

    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    type_ = html.escape(type_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if type_:
        attributes += f' type="{type_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f"<button{attributes}>{html_inner_content}</button>"

    return tag


def input_(
    type_: str = "text",
    name_: str = "",
    value_: str = "",
    class_: str = "",
    id_: str = "",
    style_: str = "",
    pattern_: str = "",
    title_: str = "",
    readonly_: bool = False,
    checked_: bool = False,
    placeholder_: str = "",
    maxlength_: int | str = "",
    min_: int | str = "",
    max_: int | str = "",
    step_: int | str = "",
    attributes_: dict = {}
) -> str:

    type_ = html.escape(type_)
    name_ = html.escape(name_)
    value_ = html.escape(value_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    pattern_ = html.escape(pattern_)
    title_ = html.escape(title_) if title_ else ""
    readonly_str = "readonly" if readonly_ else ""
    checked_str = "checked" if checked_ else ""
    placeholder_ = html.escape(placeholder_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if type_:
        attributes += f' type="{type_}"'
    if name_:
        attributes += f' name="{name_}"'
    if value_:
        attributes += f' value="{value_}"'
    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if pattern_:
        attributes += f' pattern="{pattern_}"'
    if title_:
        attributes += f' title="{title_}"'
    if readonly_str:
        attributes += f' readonly="{readonly_str}"'
    if checked_str:
        attributes += f' checked="{checked_str}"'
    if placeholder_:
        attributes += f' placeholder="{placeholder_}"'
    if maxlength_:
        attributes += f' maxlength="{maxlength_}"'
    if min_:
        attributes += f' min="{min_}"'
    if max_:
        attributes += f' max="{max_}"'
    if step_:
        attributes += f' step="{step_}"'

    return f'<input{attributes}>'


def label_(
    for_: str = "",
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    for_ = html.escape(for_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if for_:
        attributes += f' for="{for_}"'
    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<label{attributes}>{html_inner_content}</label>'

    return tag


def textarea_(
    name_: str = "",
    rows_: int = 2,
    cols_: int = 20,
    class_: str = "",
    id_: str = "",
    style_: str = "",
    placeholder_: str = "",
    readonly_: bool = False,
    attributes_: dict = {}
) -> str:
    name_ = html.escape(name_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    placeholder_ = html.escape(placeholder_)
    readonly_str = "readonly" if readonly_ else ""

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f" {key}='{value}'"

    if name_:
        attributes += f" name='{name_}'"
    if rows_:
        attributes += f" rows='{rows_}'"
    if cols_:
        attributes += f" cols='{cols_}'"
    if class_:
        attributes += f" class='{class_}'"
    if id_:
        attributes += f" id='{id_}'"
    if style_:
        attributes += f" style='{style_}'"
    if placeholder_:
        attributes += f" placeholder='{placeholder_}'"
    if readonly_str:
        attributes += f" {readonly_str}"

    return f"<textarea{attributes}>"

    
def select_(
    name_: str = "",
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    name_ = html.escape(name_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if name_:
        attributes += f' name="{name_}"'
    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<select{attributes}>{html_inner_content}</select>'

    return tag


def form_(
    action_: str = "",
    method_: str = "GET",
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    action_ = html.escape(action_)
    method_ = html.escape(method_)
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    
    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if action_:
        attributes += f' action="{action_}"'
    if method_:
        attributes += f' method="{method_}"'
    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<form{attributes}>{html_inner_content}</form>'

    return tag


def br_() -> str:
    return "<br>"


def section_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    
    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<section{attributes}>{html_inner_content}</section>'

    return tag


def option_(
    value_: str = "",
    label_: str = "",
    selected_: bool = False,
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    value_ = html.escape(value_)
    label_ = html.escape(label_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if selected_:
        attributes += " selected"
    if value_:
        attributes += f' value="{value_}"'

    def tag(inner_content: list | str = []) -> str:
        inner_content_str = "".join(inner_content)
        return f'<option {attributes}>{inner_content_str}</option>'

    return tag


def b_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<b{attributes}>{html_inner_content}</b>'

    return tag


def nav_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<nav{attributes}>{html_inner_content}</nav>'

    return tag


def footer_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<footer{attributes}>{html_inner_content}</footer>'

    return tag


def header_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<header{attributes}>{html_inner_content}</header>'

    return tag


def head_(
) -> Callable[[list[str]], str]:
    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<head>{html_inner_content}</head>'

    return tag


def body_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<body{attributes}>{html_inner_content}</body>'

    return tag


def html_(
    lang_: str = "en",
) -> Callable[[list[str]], str]:
    lang_ = html.escape(lang_)

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<html lang="{lang_}">{html_inner_content}</html>'

    return tag


def script_(
    src_: str = "",
    type_: str = "text/javascript",
    charset_: str = "",
    defer_: bool = False,
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    src_ = html.escape(src_)
    type_ = html.escape(type_)
    charset_ = html.escape(charset_)
    defer_str = "defer" if defer_ else ""

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if src_:
        attributes += f' src="{src_}"'
    if type_:
        attributes += f' type="{type_}"'
    if charset_:
        attributes += f' charset="{charset_}"'
    if defer_str:
        attributes += f' {defer_str} '

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<script{attributes}>{html_inner_content}</script>'

    return tag


def link_(
    rel_: str = "stylesheet",
    href_: str = "",
    type_: str = "text/css",
    integrity_: str = "",
    crossorigin_: bool = False,
    attributes_: dict = {}
) -> str:
    rel_ = html.escape(rel_)
    href_ = html.escape(href_)
    type_ = html.escape(type_)
    integrity_ = html.escape(integrity_)
    crossorigin_ = html.escape(crossorigin_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if rel_:
        attributes += f' rel="{rel_}"'
    if href_:
        attributes += f' href="{href_}"'
    if type_:
        attributes += f' type="{type_}"'
    if integrity_:
        attributes += f' integrity="{integrity_}"'
    if crossorigin_:
        attributes += ' crossorigin'

    return f'<link{attributes}>'


def meta_(
    charset_: str = "UTF-8",
    name_: str = "",
    content_: str = "",
    http_equiv_: str = "",
    attributes_: dict = {}
) -> str:
    charset_ = html.escape(charset_)
    name_ = html.escape(name_)
    content_ = html.escape(content_)
    http_equiv_ = html.escape(http_equiv_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if charset_:
        attributes += f' charset="{charset_}"'
    if name_:
        attributes += f' name="{name_}"'
    if content_:
        attributes += f' content="{content_}"'
    if http_equiv_:
        attributes += f' http-equiv="{http_equiv_}"'

    return f'<meta{attributes}>'


def tr_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    rowspan_: int = 1,
    colspan_: int = 1,
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if rowspan_ > 1:
        attributes += f' rowspan="{rowspan_}"'
    if colspan_ > 1:
        attributes += f' colspan="{colspan_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<tr{attributes}>{html_inner_content}</tr>'

    return tag


def th_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    rowspan_: int = 1,
    colspan_: int = 1,
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if rowspan_ > 1:
        attributes += f' rowspan="{rowspan_}"'
    if colspan_ > 1:
        attributes += f' colspan="{colspan_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<th{attributes}>{html_inner_content}</th>'

    return tag


def td_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    rowspan_: int = 1,
    colspan_: int = 1,
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if rowspan_ > 1:
        attributes += f' rowspan="{rowspan_}"'
    if colspan_ > 1:
        attributes += f' colspan="{colspan_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<td{attributes}>{html_inner_content}</td>'

    return tag


def thead_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<thead{attributes}>{html_inner_content}</thead>'

    return tag


def tbody_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<tbody{attributes}>{html_inner_content}</tbody>'

    return tag


def tfoot_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<tfoot{attributes}>{html_inner_content}</tfoot>'

    return tag


def table_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []):
        html_inner_content = "".join(inner_content)
        return f'<table{attributes}>{html_inner_content}</table>'

    return tag


def main_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<main{attributes}>{html_inner_content}</main>'

    return tag


def i_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<i{attributes}>{html_inner_content}</i>'

    return tag


def strong_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<strong{attributes}>{html_inner_content}</strong>'

    return tag


def em_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<em{attributes}>{html_inner_content}</em>'

    return tag


def fieldset_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    disabled_: bool = False,
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    disabled_ = "disabled" if disabled_ else ""

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if disabled_:
        attributes += " disabled"

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<fieldset{attributes}>{html_inner_content}</fieldset>'

    return tag


def legend_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    text_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    text_ = html.escape(text_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<legend{attributes}>{text_}{html_inner_content}</legend>'

    return tag


def iframe_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    src_: str = "",
    width_: int = 600,
    height_: int = 400,
    attributes_: dict = {}
) -> str:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)
    src_ = html.escape(src_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'
    if src_:
        attributes += f' src="{src_}"'
    if width_:
        attributes += f' width="{width_}"'
    if height_:
        attributes += f' height="{height_}"'

    return f'<iframe{attributes}></iframe>'


def hr_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> str:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    return f'<hr{attributes}>'


def blockquote_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<blockquote{attributes}>{html_inner_content}</blockquote>'

    return tag


def cite_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<cite{attributes}>{html_inner_content}</cite>'

    return tag


def code_(
    class_: str = "",
    id_: str = "",
    style_: str = "",
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    class_ = html.escape(class_)
    id_ = html.escape(id_)
    style_ = html.escape(style_)

    attributes = ""

    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    if class_:
        attributes += f' class="{class_}"'
    if id_:
        attributes += f' id="{id_}"'
    if style_:
        attributes += f' style="{style_}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<code{attributes}>{html_inner_content}</code>'

    return tag

def title_(
    attributes_: dict = {}
) -> Callable[[list[str]], str]:
    attributes = ""
    
    for key, value in attributes_.items():
        key = html.escape(key)
        value = html.escape(value)
        attributes += f' {key}="{value}"'

    def tag(inner_content: list | str = []) -> str:
        html_inner_content = "".join(inner_content)
        return f'<title{attributes}>{html_inner_content}</title>'

    return tag

