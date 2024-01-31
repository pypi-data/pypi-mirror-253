from typing import Callable
from types import ModuleType

import os
import inspect
import sys
import importlib
import importlib.util

from flask import Flask

class PageRouter:
    
    PAGES_FOLDER_NAME = "pages"
    
    def __init__(self, app: Flask | None = None) -> None:
        """
        Initializes the Pagerouter.

        :param app: Instance of Flask, the web application.
        """
        self.app = app
        self.get_routes_attributes(app.root_path)
        
        
    def get_pages_dir(self, root_path: str)->str:
        """
        Obtains the path of the pages directory and creates it if it does not exist.

        :param root_path: Root path of the Flask application.
        :return: Path of the pages directory.
        """
        pages_dir = os.path.join(root_path, self.PAGES_FOLDER_NAME)
        os.makedirs(pages_dir, exist_ok=True)
        return pages_dir  
    
    
    def get_module(self, file_path: str) -> ModuleType:
        """
        Imports and returns a module from the file path.

        :param file_path: Path of the module file.
        :return: Imported module.
        """
        _, key, after = file_path.partition("pages")
        module_dir = f"{key}{after}".replace(os.path.sep, ".")
        module = None
        try:
            module = importlib.import_module(module_dir)
        except ImportError as e:
            raise ValueError(f"Error: {e}. Module {module_dir} not found.")
        return module
    
    
    def get_module_function(self, module, file_path):
        """
        Obtains and returns the function of the module associated with a page.

        :param module: Python module.
        :param file_path: Path of the module file.
        :return: Function associated with the page.
        """
        function = None
        is_function = inspect.getmembers(module, inspect.isfunction)
        if len(is_function) > 0:
            is_page_function = False
            for f in is_function:
                if f[0].startswith("page"):
                    function = f[1]
                    is_page_function = True
            if not is_page_function :
                raise NameError(f"At page: {file_path}. A page function must be start with 'page' ")           
        else: 
            raise NotImplementedError(f"At page: {file_path}. A function must be defined for the page.")
        return function
            
        
    def get_routes_attributes(self, root_path: str):
        """
        Obtains route attributes for each file in the pages directory.

        :param root_path: Root path of the Flask application.
        """
        if root_path not in sys.path:
            sys.path.append(root_path)
        view_url = ""
        function = ""
        methods = []
        pages_dir = self.get_pages_dir(root_path)
        
                   
        for root, dirs, files in os.walk(pages_dir):
            for file in files :
                if file.endswith(".py") and not file.startswith("__"):
                    if file[:-3] == "index":
                        view_url = root
                    else: 
                        view_url = os.path.join(root, f"{file[:-3]}")
                        view_url = view_url.replace(os.pathsep, "/")
                        
                    view_url = view_url.replace("[", "<").replace("]", ">")
                    _, key, after = view_url.partition("pages")
                    view_url = after
                    if view_url == "":
                        view_url = "/"
                    
                    file_path = os.path.join(root, f"{file[:-3]}")
                    module = self.get_module(file_path)
                    function = self.get_module_function(module, file_path)
                                                 
                    methods = getattr(module, "page_methods", ["GET"])
                    self.add_route(view_url, methods, function)
                    
                               
    def add_route(self, view_url: str, methods: list, function: Callable):
        """
        Adds a route to the Flask application.

        :param view_url: URL of the route.
        :param methods: HTTP methods allowed for the route.
        :param function: Function associated with the route.
        """
        self.app.route(view_url, methods=methods)(function)