from typing import List, Union
import random
import time
from tqdm import tqdm
from models.student import Student

CURRENT_STUDENTS_FOR_CV = ["成文浩","龚渊","吉雅太","劳珊珊","罗美薇","杨思谛","周辉","陈怡凡","刘镛", 
        "石书玮","印飞","柏清岩","曹铭登","田宸瑜","王家豪","杨耿聪","余然","舒大伟"]
CURRENT_STUDENTS_FOR_NLP = ["李思衡","梁添","刘轩舟","谭璐","杨程","余承泽","朱欣宇","白星宇","高婕",
        "江旺杰","李嘉屹","孙嘉齐","吴太强","曹翔","陈茂炎","汪宇通","雷洁琼","王军杰","于顺顺"]
SUPERVISOR = "Yang"

def all_student_express_sincere_love() -> None:
    print("老师，您总是把我们的需求放在第一位，尽可能带我我们优良的成长氛围————")
    print("\n")
    print("您往往到的最早，走的最晚，辛勤为实验室大家庭耕耘————")
    print("\n")
    print("感激您所付出的一切，今天是您的节日")
    print("\n")
    time.sleep(2)
    print("给您笔芯(●'◡'●)")
    time.sleep(7)
    [(print("\033[91m"+i,end="",flush=True)) for i in ('\n'.join([''.join([(' We love U'[(x-y)%10]if((x*0.05)**2+
    (y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(13,-13,-1)]))]

def happy_teachers_day() -> None:
    time.sleep(3)
    print("Prof.Yang ，1919全体运动员祝您教师节快乐！")

def moring() -> None:
    print("Today is a nice Saturday. ")
    time.sleep(3)
    print("Prof." + teacher.name + " is drving to the institute...")
    for i in tqdm(range(1000)):
        time.sleep(0.001)
    print("It's 9:55. The students outside meeting room are swarming into the 1809...")
    for i in tqdm(range(300)):
        time.sleep(0.001)

def afternoon() -> None:
    print("Prof" + teacher.name + " has a rest...")
    for i in tqdm(range(1000)):
        time.sleep(0.001)
    print("It's 13:55. The students outside meeting room are swarming into the 1809...")
    for i in tqdm(range(300)):
        time.sleep(0.001)

def dinner() -> None:
    print("Prof.Yang invites all the students to dinner because of the arrival of new students..." )
    print("\n" * 3)
    time.sleep(3)

class Teacher:
    def __init__(self, name) -> None:
        self.name = name
        self.cv_students = dict()
        self.cv_students_names = []
        self.nlp_students = dict()
        self.nlp_students_names = []

    def add_cv_student(self, student: Student) -> None:
        student.supervisor = self
        self.cv_students_names.append(student.name)
        self.cv_students[student.name] = student

    def add_nlp_student(self, student: Student) -> None:
        student.supervisor = self
        self.nlp_students_names.append(student.name)
        self.nlp_students[student.name] = student

    def hold_weekly_group_meeting_of_cv(self, report_students:Union[str, List[str]] = None) -> None:
        print("\n")
        time.sleep(3)
        print("Some students have prepared a lot for the meeting")
        time.sleep(3)
        print("Prof." + self.name + " starts a weekly group meeting of CV...")
        print('-' * 30 + "Meeting" + '-' * 30)
        time.sleep(3)
        if report_students is not None:
            report_students = list(report_students)
        else:
            report_students = self.random_choose_cv_students()
        for i, name in enumerate(report_students):
            n = i + 1
            print("the #" + str(n) + " student starts the presentation...")
            print(name + " is making a presentation, other students are listening carefully.")
            time.sleep(2)
            for j in tqdm(range(100)):
                time.sleep(0.001)

            print("Prof." + self.name + " proposes suggestions for improvement.")
            time.sleep(1)
            self.cv_students[name].increase_knowledge_by_reporting()
            print('\n')
            time.sleep(2)

        self.ask_cv_about_progress_and_guide()

        for name, student in self.cv_students.items():
            student.increase_knowledge_by_listening()
        print("All students' knowledge has increased after meeting, keep going!")
        print('-' * 30 + "Meeting End" + '-' * 30)

    def hold_weekly_group_meeting_of_nlp(self, report_students:Union[str, List[str]] = None) -> None:
            print("Prof." + self.name + " starts a weekly group meeting of NLP...")
            print('-' * 30 + "Meeting" + '-' * 30)
            time.sleep(3)
            if report_students is not None:
                report_students = list(report_students)
            else:
                report_students = self.random_choose_nlp_students()
            for i, name in enumerate(report_students):
                n = i + 1
                print("the #" + str(n) + " student starts the presentation...")
                print(name + " is making a presentation, other students are listening carefully.")
                time.sleep(2)
                for i in tqdm(range(100)):
                    time.sleep(0.001)

                print("Prof." + self.name + " propose suggestions for improvement.")
                time.sleep(1)
                self.nlp_students[name].increase_knowledge_by_reporting()
                print('\n')
                time.sleep(2)

            self.ask_nlp_about_progress_and_guide()

            for name, student in self.cv_students.items():
                student.increase_knowledge_by_listening()
            time.sleep(3)
            print("All students' knowledge has increased after meeting, keep going!")
            time.sleep(2)
            print('-' * 30 + "Meeting End" + '-' * 30)

    

    def ask_cv_about_progress_and_guide(self, names:Union[str, List[str]] = None) -> None:
        if names is None:
            names = self.random_choose_cv_students()
        print("Prof." + self.name + "看了看手表————已经快12：00了")
        time.sleep(2)
        print("Prof." + self.name + ":" +"那我们感谢今天分享的三位同学，有感兴趣的同学会后可以深入交流")
        time.sleep(2)
        print("Prof." + self.name + ":" + "时候也不早了，那我们进入第二个环节吧！")
        time.sleep(3)
        for i, name in enumerate(names):
            if len(name) == 3:
                name = name[-2:]
            if i == 2:
                print("Prof." + self.name + ":" + "嗯好！" + name + "啊，你也说两句吧！")
                time.sleep(2)
                print(name + "说最近熬了几个晚上做了很多实验，但是做的效果不太行")
                time.sleep(2)
                print("Prof." + self.name +  ":" + "嗯好！伟浩也在实验室里，多向他请教！")
                print('\n')
                time.sleep(5)
                
            if i == 0:                
                print("Prof." + self.name + ":" + "嗯好！" + name + "啊，实验做的怎么样啊！")
                time.sleep(2)
                print(name + "说最近读了一篇CVPR的文章，深受启发")
                time.sleep(2)
                print("Prof." + self.name +"这篇文章我也看过，确实做的不错，有机会复现一下！")
                print('\n')
                time.sleep(2)
                
            if i == 1:
                print("Prof." + self.name + ":" + "嗯好！" + name + "，最近关于***的问题解决了吗？")
                time.sleep(2)
                print(name + "回答道已经解决了，后面准备深挖一下这个算法方面的问题")
                time.sleep(2)
                print("Prof." + self.name + "鼓励了" + name + "：做的不错！确实咱们还是应该把精力多放到算法上来。")
                print('\n')
                time.sleep(2)
    
    def ask_nlp_about_progress_and_guide(self, names:Union[str, List[str]] = None) -> None:
        if names is None:
            names = self.random_choose_nlp_students()
        print("Prof." + self.name + "看了看手表————已经快5：00了")
        time.sleep(2)
        print("Prof." + self.name + "那我们感谢今天分享的三位同学，有感兴趣的同学会后可以深入探讨")
        time.sleep(2)
        print("Prof." + self.name + ":" + "时候也不早了，那我们进入第二个环节吧！")
        time.sleep(3)
        for i, name in enumerate(names):
            if len(name) == 3:
                name = name[-2:]
            if i == 2:
                print("Prof." + self.name + ":" + "嗯好！" + name + "啊，你也说两句吧！")
                time.sleep(2)
                print(name + "说最近做了一篇很好的工作，中了顶会")
                time.sleep(2)
                print("Prof." + self.name + "内心非常高兴，不过嘴上只是说做的不错，keep going！")
                print('\n')
                time.sleep(5)
                
            if i == 0:                
                print("Prof." + self.name + ":" + "嗯好！" + name + "啊，实验做的怎么样啊！")
                time.sleep(2)
                print(name + "说最近读了一篇EMNLP的文章，深受启发")
                time.sleep(2)
                print("Prof." + self.name +":不能光顾着读文章呀，多实验才能做出成果！")
                print('\n')
                time.sleep(2)
                
            if i == 1:
                print("Prof." + self.name + ":" + "嗯好！" + name + "，最近关于***的问题解决了吗？")
                time.sleep(2)
                print(name + "回答道目前还在跑实验，已经有解决的方法了")
                time.sleep(2)
                print("Prof." + self.name + "鼓励了" + name + "并提出了他的看法")
                print('\n')
                time.sleep(2)

    def random_choose_cv_students(self, num=3) -> List[str]:
        chosen_cv_students = random.sample(self.cv_students.keys(), num)
        return list(chosen_cv_students)

    def random_choose_nlp_students(self, num=3) -> List[str]:
        chosen_nlp_students = random.sample(self.nlp_students.keys(), num)
        return list(chosen_nlp_students)

if __name__ == "__main__":
    teacher = Teacher(SUPERVISOR)
    for name in CURRENT_STUDENTS_FOR_CV:
        teacher.add_cv_student(Student(name))
    print("Teacher: " + teacher.name)
    print("His cv students: ", teacher.cv_students_names)

    for name in CURRENT_STUDENTS_FOR_NLP:
        teacher.add_nlp_student(Student(name))
    print("Teacher: " + teacher.name)
    print("His nlp students: ", teacher.nlp_students_names)
    print("\n")


    moring()
    teacher.hold_weekly_group_meeting_of_cv()
    
    afternoon()
    teacher.hold_weekly_group_meeting_of_nlp()

    dinner()

    all_student_express_sincere_love()
    happy_teachers_day()
