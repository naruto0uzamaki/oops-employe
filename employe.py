class Employe:
    def __init__(self,name,id,age,gender):
        self.name = name
        self.age = age
        self.id = id
        self.gender = gender

class organisation:
    
    def __init__(self,oname,elist):
        self.oname = oname
        self.elist = elist

    def add_employe(self,name,age,id,gender):
        e = Employe(name,age,id,gender)
        self.elist.append(e)    

    def viewemploye(self):
        for e in self.elist:
            print (e.id)
            print (e.name)
            print (e.age)
            print (e.gender)

    def employe_count(self):
        return len(self.elist)

    def find_employe_age(self,id):
        for i in self.elist:
            if i.id == id:
                return (i.age)   

    def count_employe_byage(self,age):
        count = 0
        for e in self.elist:
            if e.age > age:
                count = +1
        return count

if __name__ == '__main__':
    elist = []
    o = organisation('TCS',elist)

    n = int(input('enter'))

    for i in range(n):
        name=input('name')
        id=int(input('id'))
        gender=input('gender')
        age=int(input('age'))
        o.add_employe(name,age,id,gender)

    o.viewemploye()
    print(o.employe_count)
