def fib(n):
    pred,curr=1,0
    k=0
    while k<n:
        pred,curr=curr,pred+curr
        k=k+1
    return curr

#使用input接收用户的键盘输入
user_input=input("请输入你想计算的项数 n:") 

#将输入的字符串转换为整数
n=int(user_input)

#调用函数并打印结果
result=fib(n)
print(f"第{n}项是: {result}")