import  os
stud_list=[]
def show_menu():
    print("1:添加学生")
    print('2:删除学生')
    print('3:修改学生信息')
    print('4:查询单个学生信息')
    print('5:查询所有学生信息')
    print('6:退出系统')


def insert_student():
    name=input('请输入学生姓名：')
    for stud in stud_list:
        if stud['name']==name:
            print("——————学生信息已经存在——————")
            return
    age=input('请输入学生年龄：')
    gender=input('请输入学生性别：')
    stud_dict={'name':name,'age':age,'gender':gender}
    stud_list.append(stud_dict)
    print('———————学生信息添加成功——————')
    pass
def remove_student():
    name=input('请输入要删除的学生姓名：')
    for stud in stud_list:
        if stud["name"]==name:
            stud_list.remove(stud)
            print('成功删除')
            break
    else:
        print('————该学生信息已经不存在————')

def modify_student():
            name = input('请输入要修改的学生姓名：')
            for stud in stud_list:
                if stud["name"] == name:
                   stud["age"]=int(input('请输入要修改的年龄'))
                   break
            else:
                print('————该学生信息不存在，无法删除————')


def search_student():
    name = input('请输入要查询的学生姓名：')
    for stud in stud_list:
        if stud["name"] == name:
            print(f'姓名：{stud["name"]},年龄:{stud["age"]},性别:{stud["gender"]}')
            break
    else:
        print('————该学生信息不存在，无法删除————')
def show_all_info():
    if len(stud_list)>0:
        for stud in stud_list:
            print(f'姓名：{stud["name"]},年龄:{stud["age"]},性别:{stud["gender"]}')
    else:
        print('目前没有学生信息')


def save():
    f=open('学生信息.txt','w',encoding='utf-8')
    f.write(str(stud_list))
    f.close()


def load_file():
    global stud_list
    if os.path.exists('学生信息.txt'):
        f=open('学生信息.txt','r',encoding='utf-8')
        buf=f.read()
        if buf:
            stud_list = eval(buf)
        f.close()


def main():
    load_file()
    while True:
        show_menu()
        cho=input('请输入您要使用的功能编号：')
        if cho=='1':
            insert_student()
        elif cho=='2':
            remove_student()
        elif cho == '3':
            modify_student()
        elif cho == '4':
            search_student()
        elif cho == '5':
            show_all_info()
        elif cho == '6':
            print('欢迎下次使用本系统')
            save()
            break
            # 为了停止系统输出
        else:
            print('输入有误，请重新输入')
            continue
            # (为了在输入有误后继续输出菜单)
        input('.....请回车继续操作.....')
main()