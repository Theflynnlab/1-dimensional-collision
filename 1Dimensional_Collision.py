from sympy import *
def OneD_Collison(m1,v1,m2,v2,e):
    v1f, v2f = symbols('v1f, v2f')
    if e==1:
        eq1=Eq(m1*v1 + m2*v2, m1*v1f + m2*v2f)
        eq2=Eq(1/2*m1*v1**2 + 1/2*m2*v2**2, 1/2*m1*v1f**2 + 1/2*m2*v2f**2)
        sol = solve([eq1,eq2],[v1f, v2f])  #need to drop the v1=v1f and v2=v2f case
    print(sol)
OneD_Collison(2,3,4,-2,1)
