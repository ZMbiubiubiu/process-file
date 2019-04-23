"""
当前目录下, 有多个文件夹
每个文件夹中有一些文件
这个脚本的目标就是, 将这些文件移动到当前目录下
"""

import os


cwd = os.getcwd()
dirs = [dir for dir in os.listdir('.') if os.path.isdir(dir)]
for dir in dirs:
	cur_dir = os.path.join('.', dir)
	files = os.listdir(cur_dir)
	for file in files:
		file = os.path.join(cur_dir,file)
		os.system('mv %s .' % file)

