"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：

1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
    1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
    1.3 验证成绩范围（0-100分）
    1.4 创建学生对象并添加到系统
2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    2.1 输入要修改的学生姓名
    2.2 根据姓名查找该学生，显示该生当前成绩信息
    2.3 输入新的语文、数学、英语成绩
    2.4 更新学生成绩数据
3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
    4.1 输出格式为："姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
5.展示全部学生成绩：展示出系统中所有学生的成绩
"""
#学生类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f"姓名 {self.name} |语文成绩 {self.chinese} |数学成绩 {self.math} |英语成绩 {self.english} |总分{self.chinese+self.math+self.english}"
    #修改学生成绩
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english
#测试
# if __name__=="__main__":
#     s1=Student("张三",90,85,95)
#     print(s1)自动调用__str__
#     s1.update_score(chinese=95)
#     print(s1)
#教务系统管理类
class EduManagement:
    system_version="1.0"
    system_name="教务管理系统"
    def __init__(self):#student用不上
        self.student_list=[]
    #添加学生信息
    def add_student(self):
        name=input("请输入学生姓名: ")
        for s in self.student_list: #student_list=[  [abc,12,12,12],[],[]...]
            if name in self.student_list:
                print("该学生成绩已存在")
                return
        chinese1=int(input("请输入语文成绩: "))
        math1=int(input("请输入数学成绩: "))
        english1=int(input("请输入英语成绩: "))
        #判断分数是否在0-100之间
        if 0<=chinese1<=100 and 0<=math1<=100 and 0<=english1<=100:
            stu=Student(name,chinese1,math1,english1)#调用学生类,传入参数,通过__str__打印该学生的信息
            self.student_list.append(stu)#将该学生的信息添加到列表中
            print("学生信息添加成功")
        else:
            print("各科成绩必须在0-100之间")
    #修改学生信息
    def update_score(self):
        name = input("请输入学生姓名: ")
        for s in self.student_list:
            if s.name==name:
                print(f"当前成绩{s}")
            chinese1 = int(input("请输入修改后语文成绩: "))
            math1 = int(input("请输入修改后数学成绩: "))
            english1 = int(input("请输入修改后英语成绩: "))
    # 判断分数是否在0-100之间
            if 0 <= chinese1 <= 100 and 0 <= math1<= 100 and 0 <= english1 <= 100:
                s.update_score(chinese1,math1,english1)#调用Student类中的函数,将xx2这些数据放入
                print(f"{s.name}同学的成绩修改完成")
                print(f"当前成绩{s}")
                return
            else:
                print("各科成绩必须在0-100之间")
                return
        print("未找到该学生信息,修改失败")
    #删除学生信息
    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")
        for s in self.student_list:
            if s.name==name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生信息,删除失败")
    #查询指定学生信息
    def query_student(self):
        name = input("请输入要查询的学生姓名: ")
        for s in self.student_list:
            if s.name==name:
                print(f"该学生信息{s}")
                return
        print("未找到该学生信息,查询失败")
    #展示全部学生信息
    def student_list1(self):
        for s in self.student_list:
            print(s)

    #运行系统---控制栏菜单
    def run(self):
        print(f"欢迎使用教务管理系统{EduManagement.system_version}")
        while True:
            print()
            print("##########################################################################################")
            print("1.添加学生信息   2.修改学生信息   3.删除学生信息   4.查询指定学生信息   5.查询所有学生信息   6.退出系统")
            choice=input("请输入要选择的操作,输入1-6")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_score()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.student_list1()
                case "6":
                    print("bey")
                    break
                case _:
                    print("输入错误,请选择1-6之间的功能")
#测试
if __name__=="__main__":
    edu_management=EduManagement()
    edu_management.run()

















