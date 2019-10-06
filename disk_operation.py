# -*- coding: utf-8 -*-

import os
import shutil
import datetime
import re


def show_menu():
    print('*' * 10, "磁盘操作系统菜单", '*' * 10,
          "\n1.增加文件夹\n"
          "2.删除文件夹\n"
          "3.修改文件夹\n"
          "4.查询文件夹\n"
          "5.退出磁盘操作\n", '*' * 37)


def make_file():
    """新增文件"""
    my_circular = True
    while my_circular:
        print("1.增加文件夹\n"
              "2.增加文件\n"
              "3.返回")
        my_operate = input("请继续您要执行的操作：")
        if my_operate == "1":
            dirname = input("请输入要创建的文件夹名称：")
            dirname = dirname.strip()
            if not os.path.exists(dirname):
                os.mkdir(dirname)
                print(dirname+"创建成功")
            else:
                print(dirname+"目录已存在")

        elif my_operate == "2":
            filename = input("请输入要创建的文件名称：")
            filename = filename.strip()
            if not os.path.exists(filename):
                print("1.保存为txt格式\n"
                      "2.保存为doc格式\n"
                      "3.保存为xlsx格式")
                my_select = input("请选择要保存的文件格式：")
                if my_select == "1":
                    f = open(filename+'.txt', 'w')
                    f.close()
                    print(filename + "创建成功")
                elif my_select == "2":
                    f = open(filename + '.doc', 'w')
                    f.close()
                    print(filename + "创建成功")
                elif my_select == "3":
                    f = open(filename + '.xlsx', 'w')
                    f.close()
                    print(filename + "创建成功")
                else:
                    print("您输入的格式有误，请重新输入！")
            else:
                print(filename + "文件已存在")
        elif my_operate == "3":
            break
        else:
            print("您输入的有误，请重新输入！")


def remove_file():
    """删除文件"""
    my_circular = True
    while my_circular:
        print("1.删除文件夹\n"
              "2.删除文件\n"
              "3.返回")
        my_operate = input("请继续您要执行的操作：")
        if my_operate == "1":
            path = os.getcwd()
            dirname = os.listdir(path)
            i = 1
            dirlist = []
            for order in dirname:
                if os.path.isdir(order):    # 将所有的目录加到列表中
                    print(i, "."+order)
                    dirlist.append(order)
                    if i <= len(dirlist):
                        i += 1
            dirorder = int(input("请输入您要删除的文件夹的序号："))
            if dirorder <= len(dirlist):
                my_index = dirlist[dirorder-1]
                if not os.listdir(my_index):
                    if 'recycle' in dirname:
                        os.mkdir(path + '\\recycle\\' + my_index)
                    else:
                        os.makedirs(path + "\\recycle\\" + my_index)
                    os.rmdir(os.path.join(path, my_index))
                    print(my_index + "删除成功！")
                else:
                    la_dirs = os.listdir(os.path.join(path, my_index))
                    i = 1
                    for la_dir in la_dirs:
                        print(i, "."+la_dir)
                        if i < len(la_dir):
                            i += 1
                    la_order = input("该目录下含有文件，请确认是否删除：\n"
                                     "1.确认删除\n"
                                     "2.取消")
                    if la_order == "1":
                        if 'recycle' not in dirname:
                            os.mkdir("recycle")
                        recycle_file(my_index)
                        shutil.rmtree(os.path.join(path, my_index), ignore_errors=True)
                        print(my_index + "删除成功")
                    elif la_order == "2":
                        return
                    else:
                        print("您的输入有误，请重新输入！")
            else:
                print("您的输入有误，请重新输入！")
        elif my_operate == "2":
            path = os.getcwd()
            filename = os.listdir(path)
            i = 1
            filelist = []
            for order in filename:
                if os.path.isfile(os.path.join(path, order)):
                    print(i, ":", order)
                    filelist.append(order)
                    if i <= len(filelist):
                        i += 1
            fileorder = int(input("请输入您要删除的文件的序号："))
            if fileorder <= len(filelist):
                my_index = filelist[fileorder - 1]
                f = open(my_index, 'r')
                contents = f.readlines()[:20]
                print("该文件的前20行内容为：")
                for content in contents:
                    print(content, end="")
                f.close()
                la_order = input("请确认是否删除该文件：\n"
                                 "1.确认删除\n"
                                 "2.取消")
                if la_order == "1":
                    if "recycle" not in filename:
                        os.mkdir("recycle")
                        shutil.copy(path + "\\" + my_index, path + "\\recycle")
                    else:
                        shutil.copy(path + "\\" + my_index, path + "\\recycle")
                    os.remove(my_index)
                    print(my_index + "删除成功")
                elif la_order == "2":
                    return
                else:
                    print("您的输入有误，请重新输入！")
            else:
                print("您的输入有误，请重新输入！")
        elif my_operate == "3":
            break
        else:
            print("您的输入有误，请重新输入！")


def rename_file():
    """修改文件"""
    my_circular = True
    while my_circular:
        print("1.修改文件夹名称\n"
              "2.修改文件信息\n"
              "3.返回")
        my_operate = input("请继续您要执行的操作：")
        if my_operate == "1":
            my_input = input("请输入要修改的文件夹名称：")
            path = os.getcwd()
            dirname = os.listdir(path)
            i = 1
            dirlist = []
            mark = 0
            for file in dirname:
                if my_input in file and os.path.isdir(file):
                    print(i, ".", file)
                    dirlist.append(file)
                    if i <= len(dirlist):
                        i += 1
                else:
                    mark += 1
            if mark == int(len(dirname)):
                print("没有包含该名称的文件夹！")
                continue
            dirorder = int(input("请输入您要修改的文件夹的序号："))
            if dirorder <= len(dirlist):
                my_index = dirlist[dirorder - 1]
                new_dir = input("请输入您要修改后的名称：")
                if 'BACKUP' not in dirname:
                    os.mkdir("BACKUP")
                backup_file(my_index)
                os.renames(my_index, new_dir)
                print(my_index, "成功修改为", new_dir)
            else:
                print("您的输入有误，请重新输入！")
        elif my_operate == "2":
            print("1.修改文件名称\n"
                  "2.修改文件内容\n"
                  "3.返回")
            my_input = input("请选择您要进行的文件操作：")
            if my_input == "1":
                my_la_input = input("请输入要修改的文件名称：")
                path = os.getcwd()
                filename = os.listdir(path)
                i = 1
                filelist = []
                mark = 0
                for file in filename:
                    if my_la_input in file and os.path.isfile(file):
                        print(i, ".", file)
                        filelist.append(file)
                        if i <= len(filelist):
                            i += 1
                    else:
                        mark += 1
                if mark == int(len(filename)):
                    print("没有包含该名称的文件！")
                    continue
                fileorder = int(input("请输入您要修改的文件的序号："))
                if fileorder <= len(filelist):
                    my_index = filelist[fileorder - 1]
                    new_file = input("请输入您要修改后的名称：")
                    if "BACKUP" not in filename:
                        os.mkdir("BACKUP")
                        shutil.copy(path + "\\" + my_index, path + "\\BACKUP")
                    else:
                        shutil.copy(path + "\\" + my_index, path + "\\BACKUP")
                    os.rename(my_index, new_file)
                    print(my_index, "成功修改为", new_file)
                else:
                    print("您的输入有误，请重新输入！")
            elif my_input == "2":
                path = os.getcwd()
                filename = os.listdir(path)
                i = 1
                filelist = []
                mark = 0
                for file in filename:
                    if os.path.isfile(file):
                        print(i, ".", file)
                        filelist.append(file)
                        if i <= len(filelist):
                            i += 1
                    else:
                        mark += 1
                fileorder = int(input("请输入您要修改的文件的序号："))
                if fileorder <= len(filelist):
                    my_index = filelist[fileorder - 1]
                    old_content = input("请输入要修改前的内容:")
                    new_content = input("请输入要修改后的内容:")
                    if "BACKUP" not in filename:
                        os.mkdir("BACKUP")
                        shutil.copy(path + "\\" + my_index, path + "\\BACKUP")
                    else:
                        shutil.copy(path + "\\" + my_index, path + "\\BACKUP")
                    f = open(my_index, "r")       # 只读方式打开，读取每一行
                    alllines = f.readlines()
                    f.close()
                    f = open(my_index, "w+")      # 然后以"w+"方式打开逐行匹配替换
                    for eachline in alllines:
                        a = re.sub(old_content, new_content, eachline)
                        f.writelines(a)
                    f.close()
                    print(my_index + "文件信息修改成功")
                else:
                    print("您的输入有误，请重新输入！")
            elif my_input == "3":
                continue
            else:
                print("您的输入有误，请重新输入！")
        elif my_operate == "3":
            my_circular = False
        else:
            print("您的输入有误，请重新输入！")
        backup_clear('BACKUP')


def search_file():
    """查询文件"""
    my_circular = True
    while my_circular:
        print("1.查询文件夹信息\n"
              "2.查询文件信息\n"
              "3.返回")
        my_operate = input("请继续您要执行的操作：")
        if my_operate == "1":
            my_input = input("请输入要查询的文件夹名称：")
            print("包含" + my_input + "的文件夹如下：")
            path = os.getcwd()
            dirname = os.listdir(path)
            i = 1
            dirlist = []
            for file in dirname:
                if my_input in file and os.path.isdir(file):
                    print(i, ".", file)
                    dirlist.append(file)
                    if i <= len(dirlist):
                        i += 1
            dirorder = int(input("请输入您要查询的文件夹的序号："))
            if dirorder <= len(dirlist):
                my_index = dirlist[dirorder - 1]
                print("该文件夹下的内容为：")
                os.listdir(my_index)
            else:
                print("您的输入有误，请重新输入！")
        elif my_operate == "2":
            my_input = input("请输入要查询的文件名称：")
            print("包含" + my_input + "的文件如下：")
            path = os.getcwd()
            filename = os.listdir(path)
            i = 1
            filelist = []
            for file in filename:
                if my_input in file and os.path.isfile(file):
                    print(i, ".", file)
                    filelist.append(file)
                    if i <= len(filelist):
                        i += 1
            fileorder = int(input("请输入您要查询的文件夹的序号："))
            if fileorder <= len(filelist):
                my_index = filelist[fileorder - 1]
                f = open(my_index, 'r')
                contents = f.read()
                print("该文件的内容为：", contents)
                f.close()
            else:
                print("您的输入有误，请重新输入！")
        elif my_operate == "3":
            break
        else:
            print("您的输入有误，请重新输入！")


def copyfile(path):
    """备份文件到要存放的目录"""
    if os.path.isfile(new_path):     # 当new_path指的文件存在时
        shutil.copy(path, new_path)
    else:             # 当new_path指的文件不存在时
        dirname = os.path.dirname(new_path)    # 返回上一层目录
        if os.path.exists(dirname):
            shutil.copy(path, new_path)
        else:
            try:
                os.mkdir(dirname)
                shutil.copy(path, new_path)
            except WindowsError:
                print("创建目录出错")


def backup_file(src):
    """备份文件：遍历目标文件src下及其子目录下的所有文件"""
    for name in os.listdir(src):
        name = os.path.join(src, name)    # 构建绝对路径
        global new_path
        new_path = "BACKUP"
        new_path = os.path.join(new_path, name)
        if os.path.isdir(name):
            if not os.listdir(name):     # 对空文件夹的处理
                # print("{}".format(name), "是空文件夹")
                os.makedirs(new_path)
            backup_file(name)      # 如果是文件夹，则继续调用backup_file()
        else:
            copyfile(name)     # 如果是文件，则调用copyfile()函数


def recycle_file(src):
    """删除文件到回收站：遍历目标文件src下及其子目录下的所有文件"""
    for name in os.listdir(src):
        name = os.path.join(src, name)    # 构建绝对路径
        global new_path1
        new_path1 = "recycle"
        new_path1 = os.path.join(new_path1, name)
        if os.path.isdir(name):
            if not os.listdir(name):     # 对空文件夹的处理
                # print("{}".format(name), "是空文件夹")
                delete_file(name)
            recycle_file(name)      # 如果是文件夹，则继续调用recycle_file()
        else:
            delete_file(name)     # 如果是文件，则调用copyfile()函数


def delete_file(path):
    """文件放到回收站"""
    if os.path.isfile(new_path1):     # 当new_path指的文件存在时
        shutil.copy(path, new_path1)
    else:             # 当new_path指的文件不存在时
        dirname = os.path.dirname(new_path1)    # 返回上一层目录
        if os.path.exists(dirname):
            shutil.copy(path, new_path1)
        else:
            try:
                os.mkdir(dirname)
                shutil.copy(path, new_path1)
            except WindowsError:
                print("创建目录出错")


def backup_clear(backup):
    """备份文件夹清理：大于50M提示清理"""
    path = os.getcwd()
    os.chdir(path)
    size = 0
    for root, dirs, files in os.walk(os.path.join(path, backup)):
        for name in files:
            size += os.path.getsize(os.path.join(root, name))
    if size > 51200:
        my_select = input("BACKUP目录占用空间大于50M，请选择是否清空：\n"
                          "1.清空\n"
                          "2.忽略")
        if my_select == "1":
            for file in os.listdir(os.path.join(path, backup)):
                if os.path.isfile(os.path.join(os.path.join(path, backup), file)):
                    os.remove(file)
                else:
                    shutil.rmtree(os.path.join(os.path.join(path, backup), file))
        elif my_select == "2":
            pass
        else:
            print("您的输入有误，请重新输入！")
    else:
        pass


def recycle_clear():
    path = os.getcwd()
    if not os.path.exists("recycle"):
        os.mkdir("recycle")
    endtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = open("time.txt", 'r+')
    if not os.path.getsize(os.path.join(path, "time.txt")):   # 内容为空的时候写入时间
        f.write(endtime)
        f.close()
        f1 = open('time.txt')
        starttime = f1.read()
        d1 = datetime.datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')   # 字符串转datetime
        d2 = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')     # datetime转字符串是strftime
        interval = (d2 - d1).seconds
        f1.close()
    else:              # 内容不为空的时候
        starttime = f.read()
        d1 = datetime.datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
        d2 = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
        interval = (d2 - d1).seconds
        f.truncate()   # 清空文件内容
        f.close()
        f1 = open("time.txt", 'r+')
        f1.write(endtime)    # 写入本次时间
        f1.close()
    if interval > 86400:     # 大于24小时，清空回收站
        shutil.rmtree("recycle", ignore_errors=True)


def main():
    recycle_clear()
    my_mark = True
    while my_mark:
        # 1.显示系统菜单
        show_menu()
        # 2.获得用户输入的菜单
        my_operate = input("请输入您要执行的操作：")
        # 3.根据用户输入来判断做什么事情
        if my_operate == "1":
            make_file()
        elif my_operate == "2":
            remove_file()
        elif my_operate == "3":
            rename_file()
        elif my_operate == "4":
            search_file()
        elif my_operate == "5":
            print("退出系统！")
            break
        else:
            print("您的输入有误，请重新输入！")


if __name__ == "__main__":
    main()
