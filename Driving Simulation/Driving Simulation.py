u=initial_velocity=0
def eq1(a, t):
    s=(u*t+a*(t**2))/2
    return s
def eq2(a, t):
    v=u+a*t
    return v

def solve():
    h = int(s/10)
    print("time: ",g,"distance: ","*"*(h))
x=int(input("type the number time"))
y=int(input("type the number distance travelled"))
z=int(input("type the accleration of the car"))
limit=60
for g in range(x+1):
    s=eq1(z,g)
    v=eq2(z,g)
    solve()


if v<=limit:
    print("The person was driving too slow to reach the speed limit. (Speed limit was",limit,"m/s",")")
else:
    print("The person was driving too fast than the speed limit. (Speed limit was",limit,"m/s",")")
if s<=y:
    print("The person's journey did not end. (Mileage",s,"m)")
else:
    print("The person's journey has ended. (Mileage",s,"m)")


