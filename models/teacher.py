from typing import List, Union
import random
from student import Student


ALL_CURRENT_STUDENTS = ["成文浩", "龚渊", "吉雅太", "劳珊珊", "李思衡", "梁添", "刘轩舟", "罗美薇",
        "谭璐", "杨程", "杨思谛", "余承泽", "周辉", "朱欣宇", "白星宇", "柏清岩", "陈怡凡", "高婕",
        "江旺杰", "李嘉屹", "刘镛", "石书玮", "孙嘉齐", "吴太强", "印飞", "曹铭登", "曹翔", "陈茂炎", 
        "雷洁琼", "田宸瑜", "汪宇通", "王家豪", "杨耿聪", "余然"]
SUPERVISOR = "杨余久"

class Teacher:
    def __init__(self, name) -> None:
        self.name = name
        self.students = dict()
        self.students_names = []

    def add_student(self, student: Student) -> None:
        student.supervisor = self
        self.students_names.append(student.name)
        self.students[student.name] = student
    
    def hold_weekly_group_meeting(self, report_students:Union[str, List[str]] = None) -> None:
        print("Prof." + self.name + " starts a weekly group meeting...")
        print('-' * 40 + "Meeting" + '-' * 40)
        if report_students is not None:
            report_students = list(report_students)
        else:
            report_students = self.random_choose_students()
        for name in report_students:
            print(name + " is making a PPT report, other students are listening carefully.")
            self.students[name].increase_knowledge_by_reporting()

        self.ask_about_progress_and_guide()

        for name, student in self.students.items():
            student.increase_knowledge_by_listening()
        print("All students' knowledge has increased after meeting, keep going!")
        print('-' * 40 + "Meeting End" + '-' * 40)
    
    def ask_about_progress_and_guide(self, names:Union[str, List[str]] = None) -> None:
        if names is None:
            names = self.random_choose_students()
        for name in names:
            if len(name) == 3:
                name = name[-2:]
            print("Prof." + self.name + ":" + name + "啊，说说你最近的进展呢？")

    def random_choose_students(self, num=3) -> List[Student]:
        chosen_students = random.sample(self.students.keys(), num)
        return list(chosen_students)



if __name__ == "__main__":
    teacher = Teacher(SUPERVISOR)
    for name in ALL_CURRENT_STUDENTS:
        teacher.add_student(Student(name))
    print("Teacher: " + teacher.name)
    print("His students: ", teacher.students_names)

    teacher.hold_weekly_group_meeting()

