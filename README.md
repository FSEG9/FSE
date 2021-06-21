# FSE

## 进度

2021/6/17建库
软工基沙比克
我们一定能做出来


## 虚拟环境

```bash
python -m venv env
env\Scripts\activate
```

从依赖列表中安装依赖：

```bash
# env
pip install -r requirements.txt
```

安装包后，手动生成依赖列表：

```bash
# env
pip freeze > requirements.txt
```

退出虚拟环境：

```bash
deactivate
```

PyPI (pip) 换源：

[从国内的 PyPI 镜像（源）安装 Python 包](https://zhuanlan.zhihu.com/p/57872888)

## 数据库

初始化数据库：

```bash
flask initdb --drop
```

## 网页目录结构

```bash
/exam
	# 教师：题目管理
	/problem                           # 题目列表 | 教师题库管理.html
		/add-problem                   
		/delete-problem/<problem_id>
		/edit-problem/<problem_id>
	# 教师：考试管理
	/manage-exam                       # 教师考试管理.html (教师首页)
		/add-exam                      # 添加考试 | 教师试卷生成.html
		/edit-exam/<exam_id>           # 修改考试 | 教师试卷生成.html
		/show-exam/<exam_id>           # 单次考试信息 | 教师考试信息.html
		    /detail                    # 查看小分 | 教师考试结果.html
			/answer/<student_id>       # 查看某位同学本次考试答卷
	# 学生：考试信息查看
	/view-exam                         # 学生考试列表.html (学生首页)
		/show-exam/<exam_id>           # 单次考试信息 | 学生考试信息.html
			/answer                    # 本人考试小分 | 学生考试结果.html
	# 学生：参加考试
	/take-exam/<exam_id>               # 学生参加考试 | 学生考试答题.html
	
# 以上是网页的目录结构
# 子模块下的目录结构可根据情况更改

```

## 代码组织

- 采用类似P300功能式架构
- 每个子模块使用蓝本管理

```bash
exam/
	blueprints/        # 蓝本（视图函数）
		__init__.py
		problem.py
		manage_exam.py
		view_exam.py
		take_exam.py
	forms/             # 表单
		__init__.py
		problem.py
		exam.py
	models/            # 数据库模型
	    __init__.py
	    problem.py
	    exam.py
	settings.py        # 配置信息
    templates/         # 模板
    static/            # 静态文件
    	css/
    	js/
```

## `exam/settings.py`

```python
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/fse_exam'  # 换成自己的数据库地址
SECRET_KEY = 'ca0ea394f434482a832976508446c227'
```