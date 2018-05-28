# coding:utf-8  fxb_qzyx@163.com
"""python第三方库(peewee)：和数据库交互——ORM——CRUD"""

from peewee import MySQLDatabase  # 导入数据库
from peewee import Model  # 导入模型类
from peewee import PrimaryKeyField, CharField, ForeignKeyField, BooleanField, IntegerField  # 导入字段类型
from peewee import fn  # 导入统计函数


class MySQLDB(object):
    def __init__(self,
                 database=None,
                 host='localhost',
                 port=3306,
                 user=None,
                 password=None):
        self.db = MySQLDatabase(database=database,
                                host=host,
                                port=port,
                                user=user,
                                password=password,
                                charset='utf8')

    def get_db_obj(self):
        """获取数据库对象"""
        return self.db


class BaseModel(Model):
    """ORM基类，并指定所使用的数据库，子类继承该基类，则不必在子类中重复声明数据库"""

    class Meta:
        database = MySQLDB(database='test',
                           host='localhost',
                           port=3306,
                           user='root',
                           password='mysql').get_db_obj()


class Course(BaseModel):
    """课程表"""
    # 主键
    id = PrimaryKeyField()
    #  课程名：不能为空
    title = CharField(null=False)
    # 学时：整型
    period = IntegerField()
    # 课程描述：字符串(varchar)
    description = CharField()

    class Meta:
        db_table = "course"  # 定义数据库中的表名：course


class Teacher(BaseModel):
    """teacher表"""
    # 主键
    id = PrimaryKeyField()
    # 姓名
    name = CharField(null=False)
    # 性别
    gender = BooleanField()
    # 地址
    address = CharField()
    # 外键：course-->teacher 1:N的关系。Course:关联的表名，to_field：关联的字段名，related_name:给该关系赋予一个名字
    course_id = ForeignKeyField(Course, to_field="id", related_name='courseTeacher')

    class Meta:
        db_table = "teacher"  # 定义数据库中的表名：teacher


def create_db_table():
    """向数据库中创建数据表"""
    # 创建课程表
    Course.create_table()
    # 创建学生表
    Teacher.create_table()


def insert_data_to_db():
    # 向Course表中插入数据
    Course.create(id=1, title="物理学", period=300, description="大一必修课")
    Course.create(id=2, title="文学鉴赏", period=100, description="大二选修课")
    Course.create(id=3, title="思想政治", period=100, description="大一必修课")
    Course.create(id=4, title="计算机基础", period=200, description="大一必修课")
    # 向Teacher表中插入数据
    Teacher.create(id=1, name="夏军", gender=True, address='China', course_id=2)
    Teacher.create(id=2, name="Tony", gender=True, address="USA", course_id=4)
    Teacher.create(id=3, name="王勇", gender=False, address="China", course_id=1)


def select_course_one():
    """查询course表中的一条数据"""
    # 查询获得的第一条数据
    record = Course.get(description="大一必修课")
    print("课程名：{title}; 学时：{period}".format(title=record.title, period=record.period))


def select_course_all():
    """查询course表中的所有数据"""
    record_all_obj = Course.select()
    for record in record_all_obj:
        print("id:{id}, 课程名：{title}; 学时：{period}".format(id=record.id, title=record.title, period=record.period))


def select_course_condition():
    """带条件的查询：course表"""
    record_condition_obj = Course.select().where(Course.description == "大一必修课")
    for record in record_condition_obj:
        print("id:{id}, 课程名：{title}; 学时：{period}".format(id=record.id, title=record.title, period=record.period))


def delete_course_one():
    """删除course表中的一条数据"""
    record = Course.get(title="思想政治")
    print("课程名：{title}; 学时：{period}".format(title=record.title, period=record.period))
    record.delete_instance()  # 删除的语句


def update_teacher_one():
    """更新teacher表中的一条数据"""
    record = Teacher.get(id=2)
    print("name:{name}, gender:{gender}, address:{address}".format(name=record.name,
                                                                   gender=record.gender,
                                                                   address=record.address))
    record.address = "China"
    record.save()  # 保存修改结果


def update_teacher_many():
    """更新teacher表中的多条数据"""
    Teacher.update(address="WuHan").where(Teacher.id > 1).execute()


def fn_course():
    """统计函数：对course表中的学时求平均值 、求和"""
    p_sum = fn.Sum(Course.period)  # 求和
    p_avg = fn.Avg(Course.period)  # 求平均值
    # alias:起别名
    record_obj = Course.select(p_sum.alias("sum_period"), p_avg.alias("avg_period"))
    for record in record_obj:
        print("sum_period:{sum_period}, agv_period:{avg_period}".format(sum_period=record.sum_period,
                                                                        avg_period=record.avg_period))


def join_select():
    """连表查询：默认只显示左表的字段，右表的字段需要在select中添加才会显示"""
    record_obj = Course.select(Course.id,
                               Course.title,
                               Course.period,
                               Course.description,
                               Teacher.gender,
                               Teacher.name).join(Teacher).where(Teacher.gender == True)

    for record in record_obj:
        print(record.id, record.title, record.period, record.description, record.teacher.name, record.teacher.gender)


if __name__ == "__main__":
    # create_db_table()  # 创建数据表，只需创建一次
    # insert_data_to_db()  # 插入数据
    # select_course_one()  # 查询一条数据
    # select_course_all()  # 查询所有的数据
    # select_course_condition()  # 带条件的查询
    # delete_course_one()  # 删除一条数据
    # update_teacher_one()  # 更新一条数据
    # update_teacher_many()  # 更新多条数据
    # fn_course()
    join_select()
    pass
