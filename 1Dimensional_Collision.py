from sympy import *
def OneD_Collison(m1,v1,m2,v2,e):
    v1f, v2f = symbols('v1f, v2f')
    if e==1:
        eq1=Eq(m1*v1 + m2*v2, m1*v1f + m2*v2f)
        eq2=Eq(1/2*m1*v1**2 + 1/2*m2*v2**2, 1/2*m1*v1f**2 + 1/2*m2*v2f**2)
        sol = solve([eq1,eq2],[v1f, v2f])  #need to drop the v1=v1f and v2=v2f case
    solution=[]
    for i in range(len(sol)):           #flatten the list.
        for j in range(len(sol[i])):
            solution.append("{:.2f}".format(sol[i][j]))
    for i in range(len(solution)):
        solution[i]=float(solution[i])
    solution.remove(v1)
    solution.remove(v2)
    ans= "first mass moving {} m/s and second mass moving {} m/s after collision".format(solution[0],solution[1])


    print(ans)
OneD_Collison(6,8,4,3,1)
