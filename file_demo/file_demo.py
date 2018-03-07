# coding:utf-8

import os

# 动态获取文件的换行符(windows系统中为:\r\n)
lineBreak = os.linesep

# 获取家目录所在的文件夹路径
homePath = os.path.expanduser('~')

# 获取当前脚本的文件名
fileName = os.path.basename(os.path.abspath(__file__))

# 获取工程路径
projectName = os.path.dirname(os.path.abspath(__file__))

# truncate()的用法：截断文件，若指定了可选参数size,则表示截断文件为size个字符；
#                  若不指定，则全部截断，截断之后size后面的所有字符都被删除；
with open("./mytest.txt", "r+", encoding="utf-8") as f:
    f.truncate(10)  # 从当前位置截断10个字符，剩余的字符全部删除

# 获取fileA文件夹所在的路径
fileAPath = os.path.join(projectName, "fileA")
# walk()的用法：递归获取文件夹下所有的文件
fileObj = os.walk(fileAPath)
fileList = [fileList for fileList in fileObj]  # [(路径名，文件夹名，文件名)]
# fileList = [file[2] for file in [fileList for fileList in fileObj]]  # 递归获取文件夹下的所有文件
print(fileList)

print("当前程序所在目录：", os.getcwd())
os.chdir(os.pardir)  # 切换到上一级目录: os.pardir
print("切换到上一级目录：", os.getcwd())

if __name__ == "__main__":
    pass
