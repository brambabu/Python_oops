
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    c = connection.cursor() 
    c.execute("PRAGMA foreign_keys=on;") 
    c.execute(sql_query) 
    connection.commit() 
    connection.close()

def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    c = connection.cursor() 
    c.execute(sql_query) 
    ans= c.fetchall()  
    connection.close()
    return ans


class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass
	
class Student:
    count = 0
    def __init__(self, student_id = None ,name = None, age = None , score = None):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.score = score

    
    @classmethod
    def get (cls,**kwargs):
        for k,v in kwargs.items():
            #print(k,v)
            
            if 'score' == k:
        
                data = read_data('''select * from Student where score = {}'''.format(v))
            
            
            elif 'name' == k:

                data = read_data('''select * from Student where name like "%{}%"'''.format(v))
                
            elif 'age' == k:
            
                data = read_data('''select * from Student where age = {}'''.format(v))
                
                
            elif 'student_id' == k:
            
                data = read_data('''select * from Student where student_id = {}'''.format(v))
              
                
            else:
                raise InvalidField
                
            if len(data) > 1:
                raise MultipleObjectsReturned
                
            elif len(data) == 0:
                raise DoesNotExist
                
            else:
                return Student(*data[0])    
                            
            
    def delete(self):
        
        write_data(''' delete  from Student where student_id = {}'''.format(self.student_id))
        
    def save(self):
        
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        c = connection.cursor()
        if self.student_id == None:
            c.execute('''insert into Student (name,age,score) values (?,?,?)''',(self.name,self.age,self.score))
            self.student_id = c.lastrowid
        else:
            c.execute('''update Student set name = ?,age = ?,score = ?''',(self.name,self.age,self.score))
        
        connection.commit()
        connection.close()
        
        
        
        
       
stu_obj = Student.get(student_name = 1)
print(stu_obj.name)
