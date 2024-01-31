from typing import Any, Callable

from flask import render_template_string


def render_pyx(**context: Any)->Callable[[list[str]], str]:
    """
    A utility function to convert and render HTML PYX with Jinja support using Flask's render_template_string.

    Parameters:
    - context (dict): A dictionary containing variables to be used with Jinja.

    Returns:
    - callable: A function that takes a list of content PYX elements and renders them into HTML.

    Example Usage:
    ```python
    return render_pyx(color="Blue")(
        div_(class_="container")(
            h1_(class_="title")("The color is {{color}}")
            )
        )
    ```

    Notes:
    - This function returns a callable that can be used to render HTML content.
    - The `context` parameter allows passing variables to the template.
    - The returned callable takes a list of content strings and renders them into HTML.
    - It uses Flask's `render_template_string` for rendering.

    """
    def inner_content(content: list[str] = [])->str:
        template_content = ''.join(content)
        return render_template_string(template_content, **context)
    
    return inner_content