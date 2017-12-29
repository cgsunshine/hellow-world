import sys

#print("命令行参数为:")
#for i in sys.argv:
#	print(i)

#print('\n python 路径为',sys.path)
#input("/n/nPress the enter key to exit.")
'''
a = 20
b = 30
c = 40
'''
#if (a==b):
#	print("a 等于 b")
#else:
#	print("a 不等于 b")

#斐波纳契数列
'''
a,b = 0,1
while b < 100:
	print(b)
	a,b = b,a+b
'''

#计算狗的年龄
'''
while True:
	age = int(input("请输入狗的年龄："))
	print("")
	if age<0:
		print("不合逻辑的年龄!")
	elif age ==1:
		print("相当于14岁的人")
	elif age == 2:
		print("相当于22岁的人")
	elif age>2:
		human = 22 + (age -2)*5
		print("对应人类的年龄:",human)
	print("")
'''
###退出提示
#input("点击Enter键退出!")
'''
sites = ["baidu","google","runoob","1688"]
for site in sites:
	#if site == "1688":
	#print("阿里巴巴")
	print("循环数据"+site)
else:
	print("没有循环数据!")
print("完成循环!")
'''

def fibonacci(n): #函数的声明
	a,b,counter = 0,1,0
	while True:
		if(counter > n):
			return
		yield a 
		a,b = b,a + b
		counter += 1
f = fibonacci(10)

while True:
	try:
		print(next(f),end=",")
	except StopIteration:
		sys.exit()

