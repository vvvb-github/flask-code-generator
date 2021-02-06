# flask-code-generator

### 项目结构
```
|-flaskProject
    |-codeGenerator            代码生成工具
    |-modules                  各级模块
    |-__init__.py           
    |-views.py              蓝图映射
    |-module                具体模块
        |-controller        控制层
        |-service           服务层
        |-entity            实体类包
            |-__init__.py   
            |-Entity.py     实体类定义
    |-...
    app.py                     flask初始化及配置
    config.py                  配置参数
    main.py                    项目启动文件
```

### codeGenerator使用
- 需要`pymysql`
- 确保codeGenerator位于项目根目录下，生成的代码模块在modules目录下
- 目前仅支持部分主流的mysql数据类型，可参考`generator/typeMapper.py`
- 默认每张数据表第一个字段为主键
- 暂不支持数据表间关系连接，需手动在实体类文件中进行配置
- 执行`main.py`，根据提示输入相关信息，支持一个模块包含多个实体类
- 请确保项目根目录下`app.py`存在，并且其中已初始化了`app`和`db`两个对象
- `main.py`请务必从`views.py`引入`app`，确保蓝图映射被执行

### 项目配置
- 环境配置（推荐先配置`virtualenv`虚拟环境）
```
pip install Flask
pip install flask_cors
pip install flask_sqlalchemy
```

### 参考资料
- [flask W3Cschool教程](https://www.w3cschool.cn/flask/)
- [SQLAlchemy文档](https://www.osgeo.cn/sqlalchemy/index.html)
