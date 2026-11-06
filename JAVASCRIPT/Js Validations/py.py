'''class smp:
  x,y,z=1,2,3
  def __init__(self):
    self.a,self.b,self.c=10,20,30
  @classmethod
  def display1(cls):
    print("Class method")
  @staticmethod
  def display2():
    print("Static method")
  def display3(self):
    self.display1()
    self.display2()
    print(self.x,self.y,self.z)
    print(self.a,self.b,self.c)
smp().display3()'''


"""class sample:
  class inner1:
    a,b=10,20
  class inner2:
    c,d=1,2
  class inner3:
    e,f=30,40
print(sample.inner1.a,sample.inner1.b)
print(sample.inner2.c,sample.inner2.d)
print(sample.inner3.e,sample.inner3.f)"""

'''class sample:
  class inner1:
    @classmethod
    def display(cls):
      print("CLASS METHOD")
  class inner2:
    @staticmethod
    def display1():
      print("STATIC METHOD")
sample.inner1.display()
sample.inner2.display1()'''

'''class sample:
  class inner1:
    a,b=10,20
  class inner2:
    c,d=1,2
  class inner3:
    e,f=30,40
  def display3(self):
      print(self.inner1.a,self.inner1.b)
      print(self.inner2.c,self.inner2.d)
      print(self.inner3.e,self.inner3.f)
sample().display3()'''

'''class sample:
  class inner1:
    a,b=10,20
  class inner2:
    c,d=1,2
  class inner3:
    e,f=30,40
  def display3(cls):
      print(cls.inner1.a,cls.inner1.b)
      print(cls.inner2.c,cls.inner2.d)
      print(cls.inner3.e,cls.inner3.f)
sample().display3()'''