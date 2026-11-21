#案例1
# def function_a(d,h):
#     """
#
#     :param d:
#     :param h:
#     :return:
#     """
#     return d*h/2
# print(function_a(10,6))
#
# #案例2
# e=['a','e','i','o','u','A','E','I','O','U']
# def function_b(s):
#     """
#
#     :param s:
#     :return:
#     """
#     n=0
#     for i in s:#in的优先级高于or
#         if i in "aeiouAEIOU":
#             n+=1
#     print(n)
#     return n
# s='acjefjU'
# function_b(s)
#
#
# #案例3统计最高分最低分平均分
# def val_score(score_list):
#     """
#     :param score_list:
#     :param score_list:
#     :return:
#     """
#     max_score=max(score_list)
#     min_score=min(score_list)
#     avg_score=round(sum(score_list)/len(score_list),1)
#     print(max_score,min_score,avg_score)
#     return max_score,min_score,avg_score
# score_list=[100,90,65,70,85,95,55]
# val_score(score_list)




#案例1
# def cla(a):
#     if a>=90:
#         return "A"
#     elif a>=75:
#         return "B"
#     elif a>=60:
#         return "C"
#     else:
#         return "D"
#
# a=int(input())
# print(cla(a))

#案例2 判断是否为回文字符串
# def abc(s):
#     return s[::-1]==s
# s=input()
# print(abc(s))

#案例3 输入秒转换成小时分钟秒
# def abc2(s):
#     if s<60:
#         return s
#     elif 60<=s<3600:
#         a=s%60
#         return s//60,a
#     else:
#         h=s//3600#有多少小时
#         a=(s-(h*3600))//60#有多少分钟
#         m=s-(h*3600)-(a*60)
#         return h,a,m
# s=int(input("请输入秒数:"))
# print(abc2(s))

#案例3-->秒转成时分秒
# def hms(t):
#     h=t//3600
#     m=(t-(h*3600))//60
#     s=t-(h*3600)-(m*60)
#     return h,m,s
# s=int(input("输入秒数:"))
# print(hms(s))

#案例4
def area_s(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            return "等边三角形"
        elif a==b or a==c or b==c:
            return "等腰三角形"
        else:
            return "普通三角形"
a=int(input())
b=int(input())
c=int(input())
print(area_s(a,b,c))












