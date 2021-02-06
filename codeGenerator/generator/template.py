import os


def init(root, module):
    path = root + '\\modules\\' + module + '\\__init__.py'
    file = open(path, mode='w', encoding='utf8')
    content = [
        "from .controller import " + module,
        "",
        "__all__ = ['" + module + "']"
    ]
    for state in content:
        file.write(state + '\n')
    file.close()


def controller(root, module):
    path = root + '\\modules\\' + module + '\\controller.py'
    file = open(path, mode='w', encoding='utf8')
    content = [
        "from flask import Blueprint, request",
        "from modules." + module + " import service",
        "",
        module + " = Blueprint('" + module + "', __name__)"
    ]
    for state in content:
        file.write(state + '\n')
    file.close()


def service(root, module):
    path = root + '\\modules\\' + module + '\\service.py'
    file = open(path, mode='w', encoding='utf8')
    file.write("from modules." + module + ".entity import *" + '\n')
    file.write("from app import db\n")
    file.close()


def entity(root, module, fields):
    path = root + '\\modules\\' + module + '\\entity'
    if not os.path.exists(path):
        os.makedirs(path)
    tablename = fields['tablename']
    field = fields['fields']
    file = open(path + '\\' + tablename.lstrip('t_') + '.py', mode='w', encoding='utf8')
    content = [
        "from app import db",
        "",
        "",
        "class " + tablename.lstrip('t_') + "(db.Model):",
        "\t__tablename__ = '" + tablename + "'",
        "\t",
        "\t" + field[0][0] + " = db.Column(db." + field[0][1] + ", primary_key=True)"
    ]
    for i in range(1, len(field)):
        content.append("\t" + field[i][0] + " = db.Column(db." + field[i][1] + ")")
    content.append("")
    state = "\tdef __init__(self"
    for f in field:
        state += ', ' + f[0]
    content.append(state + '):')
    for f in field:
        content.append("\t\tself." + f[0] + " = " + f[0])
    content.append("\t")
    content.append("\tdef __repr__(self):")
    state = "\t\treturn '<" + tablename.lstrip('t_')
    for i in range(len(field)):
        state += " %r"
    state += ">' % ("
    state += "self." + field[0][0]
    for i in range(1, len(field)):
        state += ", self." + field[i][0]
    content.append(state + ")")
    for state in content:
        file.write(state + '\n')
    file.close()


def moduleInit(root):
    path = root + '\\modules'
    file_init = open(path + '\\__init__.py', mode='w', encoding='utf8')
    file_views = open(path + '\\views.py', mode='w', encoding='utf8')
    file_views.write("from app import app\n")
    file_views.write("from modules import *\n")
    file_views.write("\n")
    file_views.write("\n")
    state = "__all__ = ["
    for module in os.listdir(path):
        if module.find('.py') != -1 or module == '__pycache__':
            continue
        file_views.write("app.register_blueprint(" + module + ", url_prefix='/" + module + "')\n")
        file_init.writelines("from ."+module+" import *\n")
        state += "'" + module + "', "
    file_init.write("\n")
    state += "]\n"
    file_init.write(state)
    file_views.close()
    file_init.close()


def entityInit(root, module):
    path = root + '\\modules\\' + module + '\\entity'
    file = open(path + '\\__init__.py', mode='w', encoding='utf8')
    for entity in os.listdir(path):
        entity = entity.split('.py')[0]
        if entity != '__init__':
            file.write("from ." + entity + " import " + entity + "\n")
    file.close()
