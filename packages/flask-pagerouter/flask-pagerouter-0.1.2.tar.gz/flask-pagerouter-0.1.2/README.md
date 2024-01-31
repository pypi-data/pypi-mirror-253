# FlaskPageRouter

FlaskPageRouter is a lightweight Python library designed to streamline the page routing process in Flask applications. It provides an intuitive approach to efficiently organize and handle routes for various pages within your Flask project, drawing inspiration from the NextJS Pages Router.

In addition, FlaskPageRouter introduces Python HTML (PYX), offering a simplified method for incorporating HTML directly into your page views using python functions. This capability is facilitated through the `render_pyx` function, allowing seamless integration with Jinja 2 templating.



## Installation

Install PageRouter using `pip`:

```bash
pip install flask-pagerouter

```



## Usage

```python
from flask import Flask
from flask_pagerouter import PageRouter

app = Flask(__name__)
PageRouter(app)
```

Define your pages in a "pages" directory within your project. Each page should be a Python file containing a function starting with "page".

```python
def page_home():
    return ...
```

Run your Flask application, and PageRouter will automatically add routes for your pages.



### Optional Method Specification

To specify the supported methods for a page, simply include a list named page_methods at the end of your Python file. 

```python
def page_home():
    return ...

page_methods = ["GET", "POST"]
```

It is not required to add the page_methods list; in the absence of this list, the default method will be assumed to be GET.



### Routing

Define your pages and foldes in a "pages" directory within your project. Each page should be a Python file containing a function starting with "page". The file named "index.py" corresponds to the root path ("/").

**Exemple 1**

path : pages/index.py 

url : yourdomain.com

**Exemple 2**

path : pages/level1/index.py

url : yourdomain.com/level1

**Exemple 3**

path : pages/level1/home.py

url : yourdomain.com/level1/home


You can use placeholders like "[data]" in your filenames or foldernames to pass parameters to your pages. For example, a file named "[username].py" can corresponds to a route like "/user/john"

**Exemple 1**

path : pages/user/[username].py

url : yourdomain.com/user/john

```python
# You can retrieve the property in the function parameter.

def page_user(username):
    return f"<h1>Hello, {username}!</h1>"
```

**Exemple 2**

path : pages/user/[user]/[id].py

url : yourdomain.com/user/john/2

```python
def page_user_id(username, id):
    return f"<h1>Hello, {username}! your id is {id}</h1>"
```



### Python HTML PYX

FlaskPageRouter seamlessly integrates with Python HTML (PYX), allowing you to write HTML directly in your Python code. This integration is facilitated by the render_pyx utility function, which supports Jinja 2 for template rendering.

Note:

    - By convention, all PYX tag and tags attributes functions in FlaskPageRouter end with an underscore (_).
    
    - This convention is adopted to avoid conflicts with Python keywords and built-in functions.
    
    - It also provides clarity and consistency in the usage of PYX tags.
    
    - Example: tag(`h1_`, `h2_`, `div_` etc) tag attibutes(`class_`, `id_`, `src_` etc).
    

Example:
    - Correct: `h1_("Hello, World!")`
    - Incorrect: `h1("Hello, World!")`


```python
from flask-pagerouter import h1_

# PYX function for creating an <h1> element.
h1_(class_="title", id_="title1")("Hello, World!")

# The first set of parentheses in the function call is for attributes.
# The second set of parentheses in the function call is for the inner content.

# tag_name_(attribute1=value1, attribute2=value2, ...)("Content goes here")
```

Note: 

    - You have the option to use a list or not in the second set of parentheses.
    
    - Using list provides flexibility in constructing structures but is not necessary for simple cases.
    
    - Using a list in the second set of parentheses is optional and depends on the complexity of the structure the user wants to build.

```python
# In this case both will yield the same result. 
h1_(class_="title", id_="title1")("Hello, World!")
h1_(class_="title", id_="title1")(["Hello, World!"])
```

```html
<h1 class="title" id="title1">Hello, world</h1>
```

**The second set of parentheses can be left empty when you need an empty tag and must be omitted in cases where the tag does not require content, such as the `<input>` tag.**

```python
# In this case both will yield the same result. 
div_(class_="container")()
input_(type_="text", name_="greetings", placeholder_="Hello World")
h1_()()
```

```html
<div class="container"></div>
<input type="text" name="greetings" placeholder="Hello World">
<h1></h1>
```

For each HTML tag in PYX, the most commonly used attributes are conveniently accessible as parameters, allowing for quick and straightforward specification.

In cases where the desired attributes are not directly available as parameters, you have the option to pass a dictionary to the attributes parameter containing the desired attributes. This provides a flexible way to handle less common or custom attributes.

```python
div_(class_="block" attributes_={"data-role":"main"})()
```

```html
<h1 class="block" data-role="main">Hello, world</h1>
```



### PYX complex structures

With FlaskPageRouter, you can combine PYX tags using list to create more complex HTML structures. Simply nest the tags inside each other to build the desired hierarchy.

```python
div_(class_="container")([
    h1_(class_="title")("Welcome to FlaskPageRouter!"),
    p_()("FlaskPageRouter is a Python library for easy page routing in Flask applications."),
    div_(class_="content")(
        p_("Explore the documentation to learn more about using FlaskPageRouter.")
    )
])
```

```html
<div class="container">
    <h1 class="title">Welcome to FlaskPageRouter!</h1>
    <p>FlaskPageRouter is a Python library for easy page routing in Flask applications.</p>
    <div class="content">
        <p>Explore the documentation to learn more about using FlaskPageRouter.</p>
    </div>
</div>
```


### PYX and Jinja

With PYX in FlaskPageRouter, you can leverage the power of Jinja to make your HTML dynamic and programmable. The render_pyx function acts as a bridge between PYX and Jinja. In the first set of parentheses is for the context, and the second set of parentheses provide the inner content. This allows you to create dynamic and data-driven HTML content seamlessly.

**Exemple 1**

```python
from flask_pagerouter import render_pyx, div_, h1_, p_

def page_greetings():
    users = ["John", "Bob", "Eva"]
    return render_pyx(users=users)(
        div_(class_="container")([
            "{% for user in users %}",
            p_(class_="user")("hello {{user}}"),
            "{% endfor %}"
        ])
    )
```

```html
<div class="container">
        <p>Hello John</p>
        <p>Hello Bob</p>
        <p>Hello Eva</p>
</div>
```

**Exemple 2**

```python
from flask_pagerouter import render_pyx, h1_, div_

def page_user(user):
    return render_pyx(user=user)([
        "{% extends 'hello.html' %}",
        "{% block content %}",
        div_(class_="container")(
            h1_(class_="title")("{{user}}")
        ),
        "{% endblock %}"
    ])
```

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <div class="container"><h1 class="title">John</h1></div>
    </div>
</body>
</html>
```



## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue.



## License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2024 Etienne DTS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



