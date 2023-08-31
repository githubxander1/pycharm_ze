
# print(objects,sep='',end='\n',file=sys.stdout,flush=False)
import time

a=12
b=1.2
c='sfsdafas'
d='红色'
e='蓝色'
# 制表位符（\t）为分隔符，最后以换行符（\r与\n连用，\r是回车符）
print(a,b,c,d,e,sep='\t',end='\r',flush=False)
print(a,b,c,d,e,sep='\n',end='\r',flush=False)
print(a,b,c,d,e,sep='->')
print(a,b,c,d,e,sep='#')

# 打印进度条
# tasks=range(1,31)
# progress_width=25
#
# for n in tasks:
#     #延时0.5秒，模拟耗时操作
#     time.sleep(0.5)
#     #计算当前进度的百分比
#     curr_ps =n /len(tasks)
#     #进度条的样式为：用“>”字符来表示实际进度，其余的字符用“-”字符来填充。
#     # ljust方法的作用是让字符串左对齐，剩下的空间则用指定的字符去填充，本例中使用“-”填充字符串的剩余宽度。格式控制符“.
#     # 0%”的含义是把浮点数值转换为百分比（乘以100，并在后面加上符号“%”），“.0”用于去掉小数位部分（保留0位小数）
#     progress_str ='{0:s}'.format(int(progress_width * curr_ps) * '>').ljust (progress_width,'-')
#     msg_str='【{0:.0%}】'.format(curr_ps)
#     print(f'\r{progress_str}{msg_str}',end ='')
#
# # 文本打印到文件
# my_file= open('test.txt',mode='wt',encoding='utf-8')#t表示以文本形式读写文件
# print('Hello world!',file=my_file)