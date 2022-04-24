#!/usr/bin/env python3
# encoding: utf-8
"""
@version: v1.0
@author: XuanjieXiao
@license: BSD Licence
@contact: xuanjiexiao@163.com
@site: https://blog.csdn.net/weixin_40749043
@software: PyCharm
@file: pydemo.py
@time: 2022/4/13 下午3:33
"""
filename = 'students.txt'
import os


def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？请输入y/n')
                if answer == 'y' or answer == 'Y':
                    print('Thanks for using!!!')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('---------student profile management system------------------------------')
    print('--------------------------功能菜单--------------------------')
    print('\t\t\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t\t\t 5.排序学生信息')
    print('\t\t\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t\t\t 0.结束')
    print('---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------')


def insert():
    student_list = []
    while True:
        id = input('请输入ID（eg：1001）')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入java成绩'))
        except:
            print('输入无效，不是整数类的，请重新输入')
            continue

        # 将信息保存到字典当中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将其添加到列表中
        student_list.append(student)
        answer = input('是否继续添加y/n \n')
        if answer == 'Y' or answer == 'Y':
            continue
        else:
            break

    # 保存学生信息
    save(student_list)
    print('学生信息录入完毕！！！！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    pass


def delete():
    while True:
        student_id = input('请输入要删除的学生id:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['id'] != student_id:
                            wfile.write(str(d))
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生')
            else:
                print('无学生数据')
                break
            show()  # 重新显示全部数据
            answer = input('是否继续删除？y/n')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员的id')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id']==student_id:
                print('找到相关学生信息，可以继续修改')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                    except:
                        print('输入有误，清重新输入')
                wfile.write(str(d)+'\n')
                print('修改完成')
            else:
                wfile.write(str(d)+'\n')
        answer = input('是否继续修改其他学生信息Y\N')
        if answer == 'y' or answer == 'Y':
            modify()




def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()
