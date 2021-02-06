import pymysql
from codeGenerator.generator import *

rootDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))


def write(module, field_list):
    path = rootDir + '\\modules\\' + module
    if not os.path.exists(path):
        os.makedirs(path)
    for fields in field_list:
        init(rootDir, module)
        controller(rootDir, module)
        service(rootDir, module)
        entity(rootDir, module, fields)
    moduleInit(rootDir)
    entityInit(rootDir, module)


def generator(tablename):
    db = pymysql.connect(host='', user='', password='', db='', autocommit=True)
    cursor = db.cursor()
    sql = "select * from " + tablename
    cursor.execute(sql)
    fields = [desc[:2] for desc in cursor.description]
    cursor.close()
    db.close()
    return typeMapping(fields)


def execute():
    print('请输入表名：', end=' ')
    tablename = input().split(',')
    print('请输入模块名：', end=' ')
    module = input()
    field_list = []
    for name in tablename:
        field_list.append({
            'tablename': name,
            'fields': generator(name)
        })
    write(module, field_list)


if __name__ == '__main__':
    execute()
