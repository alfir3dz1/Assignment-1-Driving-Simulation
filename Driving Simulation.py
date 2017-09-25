u=initial_velocity=0
def eq1(a, t):
    s=(u*t+a*(t**2))/2
    return s
def eq2(a, t):
    v=u+a*t
    return v
def eq3(a, u):
    v=sqrt=(u+2*a*s)
    return v
def eq4(t, u):
    s=((u+v)*t/2)
    return s
def solve():
    h = int(s/10)
    print("time: ",g,"distance: ","*"*(h))
x=int(input("time"))
y=int(input("distance"))
z=int(input("accleration"))
limit=60
for g in range(x+1):
    s=eq1(z,g)
    v=eq2(z,g)
    solve()
    v=eq3(z,g)
    s=eq4(z,g)


if v<=limit:
    print("The person was driving too slow to reach the speed limit. (Speed limit was",limit,"m/s",")")
else:
    print("The person was driving too fast than the speed limit. (Speed limit was",limit,"m/s",")")
if s<=y:
    print("The person's journey did not end. (Mileage",s,"m)")
else:
    print("The person's journey has ended. (Mileage",s,"m)")


