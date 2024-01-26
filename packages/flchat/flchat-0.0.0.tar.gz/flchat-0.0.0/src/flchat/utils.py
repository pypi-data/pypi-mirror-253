from importlib import resources


def get_template_folder():
    return f'{resources.files("flchat").joinpath("assets/templates")}'

def get_static_folder():
    return f'{resources.files("flchat").joinpath("assets/static")}'
