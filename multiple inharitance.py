class A:
 def fun1(self):
  print("day 1")

class B:
 def fun2(self):
  print("day 2")

class C(A,B):
  pass

obj=A()
obj2=B()
obj.fun1()
obj2.fun2()
day 1
day 2
