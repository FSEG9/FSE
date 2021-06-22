from exam import app, db
from exam.models.problem import Problem, Tag
import click


# 注册命令 initdb
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialize database.')


# 注册命令 forge-problems
@app.cli.command()
@click.option('--count', default=64, help='Quantity of problems, default is 64.')
def forge_problems(count):
    from faker import Faker
    import random

    """Generate fake problems."""
    click.echo('Working...')

    fake = Faker('zh_CN')
    subjects = ['FDS', 'Java', '高级数据结构', '软件工程基础', '面向对象程序设计', 'C语言']
    ans = [
        ['T', 'F'],
        ['A', 'B', 'C', 'D'],
        ['A', 'B', 'C', 'D', 'AB', 'BC', 'CD', 'AC', 'BD', 'AD', 'ABC', 'ABD', 'ACD', 'BCD', 'ABCD']
    ]

    for i in range(count):
        type_index = random.randint(0, 2)

        answer = random.choice(ans[type_index])
        problem = Problem(
            type=type_index,
            text=fake.paragraph(nb_sentences=2, variable_nb_sentences=True),
            choice_A=fake.sentence(),
            choice_B=fake.sentence(),
            choice_C=fake.sentence(),
            choice_D=fake.sentence(),
            solution=answer,
            adder='Default User',
            chosen=False
        )
        db.session.add(problem)
        tag_name = random.choice(subjects)
        tag = Tag.query.filter_by(tag_name=tag_name).first()
        if tag is None:
            tag = Tag(tag_name=tag_name)
        problem.tags.append(tag)

    db.session.commit()
    click.echo('Created %d fake problems.' % count)
