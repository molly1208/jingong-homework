w=48
h=1.53
t=w/(h**2)
if t<18:
    print("低体重")
elif t<=25:
    print("正常体重")
elif t<=27:
    print("超重体重")
elif t>27:
    print("肥胖")
