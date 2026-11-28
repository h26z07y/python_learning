#暴力枚举法
nums=[]
target=int(input("请输入目标"))
n=int(input("请输入数组中元素个数"))
for i in range(n):
    val=int(input(f"请输入第{i+1}个元素"))
    nums.append(val)
n=len(nums)

for j in range(n):
     for k in range(j+1,n):
         if nums[j]+nums[k]==target:
            print([j,k])
         else:
             print("没有找到")
             break



nums=[]
target=int(input("请输入目标"))
n=int(input("请输入数组中元素个数"))
for i in range(n):
    val=int(input(f"请输入第{i+1}个元素"))
    nums.append(val)
seen={}
for i in range(n):
    num=nums[i]
    need=target-num
    if need in seen:
        print([seen[need],i])
        break
    seen[num]=i






