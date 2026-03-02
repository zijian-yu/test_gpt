# Django 示例网站

这是一个可直接运行的 Django 网站示例，包含：

- 首页（展示文章列表）
- 关于页
- Django Admin 后台（可管理文章）

## 1. 安装依赖

```bash
python3 -m pip install -r requirements.txt
```

## 2. 初始化数据库

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## 3. 创建管理员账号（可选）

```bash
python3 manage.py createsuperuser
```

## 4. 启动项目

```bash
python3 manage.py runserver
```

访问：

- 首页: http://127.0.0.1:8000/
- 关于: http://127.0.0.1:8000/about/
- 管理后台: http://127.0.0.1:8000/admin/
