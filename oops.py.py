class name:
    pass
person = name()
person.fname = 'reddy'
person.lname = 'basha'
person.age = 23
print("the particulars of this person are: \n",  person.fname ,"\n",person.lname ,"\n",person.age)


class name:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
person = name('reddy','basha',23)
print(f"the particulars of this person are: \n",person.fname,"\n",person.lname,"\n",person.age)
        
