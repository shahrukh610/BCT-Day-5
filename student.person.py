class Student:
    def _init_(self, n, a, r):
        self.Name = n
        self.Age = a
        self.Rollno = r
    def showName(self):
        print("Name =",self.Name)
    def showAge(self):
        print("Age =",self.Age)
    def showrollno(self): 
        print("Roll number =", self.Rollno)

class Person(Student):
    def _init_(self,n,a,r):
        super()._init_(n, a, r)
s1 = Student("Shahrukh", 20, 78)
s1.showName()
s1.showAge()
s1.showrollno()