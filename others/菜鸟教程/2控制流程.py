#列表推导式
old_list = [0,1,1,2,3,4,4,5]
new_list = [
    item
    for item in old_list
    if item % 2 == 0
]
# print(new_list)
#生成器推导式
new_list1=(
    item
    for item in old_list
    if item %2 ==0
)
# print(new_list1)
# print(next(new_list1))
# print(next(new_list1))
#集合推导式
new_set = {
    item
    for item in old_list
}
# print(new_list)
#字典推导式
old_student_score_info = {
 "Jack": {
     "chinese": 87,
     "math": 92,
     "english": 78
 },
 "Tom": {
     "chinese": 92,
     "math": 100,
     "english": 89
 }
}
new_student_score_info={
    name:scores
    for name,scores in old_student_score_info.items()
    if scores['math'] == 100
}
# print(new_student_score_info)
# 嵌套推导式
for i in range(1,10):
    for j in range(1,i+1):
        pass
        # print('{}x{}\t'.format(j,i,j*i),end='')
    # print('')

# 题目3：根据年份判断是否为闰年（能被4整除但不能被100整除，或者能被400整除的是闰年）

year= print(int(input('请输入年份：')))
if year %4 ==0 and  year%100 !=0:
    print(year,'是闰年')
elif year %400 ==0:
    print(year,'是闰年')







year = int(input("请输入一个年份："))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "是闰年")
        else:
            print(year, "不是闰年")
    else:
        print(year, "是闰年")
else:
    print(year, "不是闰年")
