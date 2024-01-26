"""This module is responsible for compiling templates and generating HTML files.

This module contains functions for loading modules, finding modules in a directory,
rendering HTML templates, creating paths, and the main function for compiling templates.

Functions:
- walk_module(directory: str) -> AsyncIterator[Tuple[str, str]]: Walks through a directory and yields the root and file name of each file.
- load_modules(module_name: str, module_path: str) -> ModuleType: Loads a module from a file path.
- find_modules(directory: str) -> Dict[str, ModuleType]: Finds all modules in a directory and returns them as a dictionary with their corresponding routes.
- render_html(route: str, module: ModuleType, env: Environment) -> str: Renders an HTML template using a module and an environment.
- create_path(directory: str, current_path: str) -> str: Creates a path based on the current directory and the given path.
- main() -> None: The main function that compiles templates and generates HTML files.

Raises:
- ImportError: Raised when a module fails to load.

Returns:
- None

Yields:
- None
"""
import asyncio
import json
import os
import importlib.util
from inspect import iscoroutinefunction
import shutil
from types import ModuleType
from typing import Any
from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound
from typer import Typer
from colorama import Fore
import watchfiles


async def walk_module(directory: str, py_convention: str):
    """Walks through a directory and yields the root and file name for each Python file.

    Args:
        directory (str): The directory to walk through.

    Yields:
        Tuple[str, str]: A tuple containing the root directory and the file name for each Python file.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file != py_convention:
                continue
            yield root, file


async def load_modules(module_name: str, module_path: str) -> ModuleType:
    """Load a module from a file.

    This function dynamically loads a module from a specified file path.

    Args:
        module_name (str): The name of the module.
        module_path (str): The path to the module file.

    Raises:
        ImportError: If the module fails to load.
        ImportError: If the module fails to load.

    Returns:
        ModuleType: The loaded module.
    """
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if not spec:
        raise ImportError(f"Failed to load module {module_name} from {module_path}")
    module: ModuleType = importlib.util.module_from_spec(spec)
    if not spec.loader:
        raise ImportError(f"Failed to load module {module_name} from {module_path}")
    spec.loader.exec_module(module)
    return module
    # Use the loaded module as needed


async def find_modules(directory: str, py_convention: str) -> dict[str, ModuleType]:
    """Find and load modules from a given directory.

    Args:
        directory (str): The directory to search for modules.

    Returns:
        dict[str, ModuleType]: A dictionary mapping the module routes to the loaded modules.
    """
    routes = {}

    async for root, file in walk_module(directory, py_convention):
        module_name: str = file.split(".")[0]
        module_path: str = os.path.join(root, file)
        module = await load_modules(module_name, module_path)
        route = await create_path(directory, root)
        routes.setdefault(route, module)

    return routes


async def render_html(
    route: str,
    module: ModuleType,
    env: Environment,
    callable_convention,
    html_conventions: dict[str, str],
) -> tuple[str, str]:
    """Render HTML for a given route using a module and environment.

    Args:
        route (str): The route for which to render the HTML.
        module (ModuleType): The module containing the callable function.
        env (Environment): The environment for rendering templates.

    Returns:
        str: The rendered HTML.
    """
    if iscoroutinefunction(getattr(module, callable_convention)):
        callable_func: dict[str, Any] = await getattr(module, callable_convention)()
    else:
        callable_func: dict[str, Any] = getattr(module, callable_convention)()

    page: str = await env.get_template(route + html_conventions["page"]).render_async(
        **callable_func
    )
    error = ""
    try:
        error: str = await env.get_template(
            route + html_conventions["error"]
        ).render_async(**callable_func)
    except TemplateNotFound:
        pass
    routes: list[str] = [x for x in route.split("/") if x]

    html: str = ""
    error_html: str = ""
    for index in reversed(range(len(routes))):
        if not index:
            path = "/" + "/".join(routes[:-1] + [routes[-1]]) + "/"
        else:
            path = "/" + "/".join(routes[:-index]) + "/"
        try:
            layout: Template = env.get_template(path + html_conventions["layout"])
            if not html:
                html = await layout.render_async(slot=page)
            if html:
                html = await layout.render_async(slot=html)
        except TemplateNotFound:
            continue

    try:
        if not html:
            html = await env.get_template(html_conventions["layout"]).render_async(
                slot=page, **callable_func
            )
        if not error_html and error:
            error_html = await env.get_template(
                html_conventions["layout"]
            ).render_async(slot=error, **callable_func)
    except TemplateNotFound:
        html = page
        error_html = error
    return html, error_html


async def create_path(directory: str, current_path: str) -> str:
    """Create a new path by removing the specified directory from the current path.

    Args:
        directory (str): The directory to be removed from the current path.
        current_path (str): The current path.

    Returns:
        str: The new path with the specified directory removed.
    """
    return current_path.replace(directory, "") + "/"


app = Typer()


@app.command()
def build(
    current_dir: str = os.getcwd(),
    out_dir: str = os.getcwd() + "/build",
    module_func: str = "load",
    module: str = "load.py",
    page: str = "page.html",
    layout: str = "layout.html",
    error: str = "error.html",
    config: str = "",
    watch: bool = False,
):
    """Builds the Meowiz project by rendering HTML templates and writing them to the specified directory.

    Args:
        current_directory (str, optional): The current working directory. Defaults to os.getcwd().
        dist_directory (str, optional): The directory where the compiled HTML files will be written. Defaults to os.getcwd()+"/dist".
        callable (str, optional): The name of the callable function to be used for rendering the templates. Defaults to "load".
        module (str, optional): The name of the module containing the templates. Defaults to "load.py".
    """
    build_config = {
        "current_dir": current_dir,
        "out_dir": out_dir,
        "module_func": module_func,
        "module": module,
        "html_conventions": {
            "page": page,
            "layout": layout,
            "error": error,
        },
    }
    if config:
        with open(os.getcwd() + "/" + config, "r", encoding="utf-8") as f:
            data: dict = json.loads(f.read())
            build_config = {**build_config, **data}

    async def run_build():
        print(f"{Fore.YELLOW} [Starting]: Meowiz Compiling...")
        env = Environment(
            loader=FileSystemLoader(current_dir),
            line_statement_prefix="#",
            line_comment_prefix="##",
            enable_async=True,
        )
        modules = await find_modules(
            build_config["current_dir"], build_config["module"]
        )

        temp_dir = {}

        for route, module_obj in modules.items():
            print(f"{Fore.BLUE} [INFO]:    {Fore.CYAN} Rendering route: {route}")
            render_data = await render_html(
                route,
                module_obj,
                env,
                build_config["module_func"],
                build_config["html_conventions"],
            )
            temp_dir.setdefault(build_config["out_dir"] + route, render_data)
            print(
                f"{Fore.BLUE} [SUCCESS]: {Fore.GREEN} Complete rendering route: {route}"
            )

        print(f"{Fore.BLUE} [INFO]:     Writing to directory...")

        for path, render_data in temp_dir.items():
            html, error_page = render_data
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path + "/index.html", "w", encoding="utf-8") as f:
                f.write(html)
                print(f"{Fore.BLUE} [SUCCESS]:  Done writing at {path}index.html")
            if error_page:
                with open(
                    path + f"/{build_config['html_conventions']['error']}",
                    "w",
                    encoding="utf-8",
                ) as f:
                    f.write(error_page)
                    print(f"{Fore.BLUE} [SUCCESS]:  Done writing at {path}error.html")
        print(
            f"{Fore.YELLOW} [COMPLETE]: Meowiz is now done compiling the directory..."
        )

    if watch:
        print(
            f'{Fore.YELLOW} [Watch]: Meowiz\'s watching this directory "{current_dir}"...'
        )
        for change in watchfiles.watch(current_dir):
            print(f"{Fore.YELLOW} [Change]: {change}")
            asyncio.run(run_build())
    else:
        asyncio.run(run_build())


if __name__ == "__main__":
    app()
