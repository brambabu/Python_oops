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
    def __init__(self, student_id = None ,name = None, age = None , score = None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score
    
    @staticmethod    
    def aggregations(agg = None,field = "", **kwargs):
        list = ['student_id','name','age','score','']
        
        multiple_values = []
            
        if field not in list:
                raise InvalidField
                
            
        for i,j in kwargs.items():
            
            a = i.split('__')
            
            if a[0] not in list:
                raise InvalidField
                
            oper = {'gt':'>', 'lt':'<', 'lte':'<=', 'gte':'>=', 'neq':'<>', 'eq' : '='}
            
            if len(a) == 1:
                val = "{} {} '{}' ".format(a[0],oper['eq'],j)
                
            elif a[1] == 'in':
                j = tuple(j)
                val = "{} {} {}".format(a[0],'IN',j)
            
            elif a[1] == 'contains':
                val = "{} {} '%{}%' ".format(a[0],'LIKE',j)
                
            else:
                val = "{} {} '{}' ".format(a[0],oper[a[1]],j)
                
            multiple_values.append(val)
            
        x = ' AND '.join(multiple_values)
        
        if x == "":
            data = read_data("SELECT {}({}) FROM Student".format(agg,field))
        else:
            data = read_data("SELECT {}({}) FROM Student where {}".format(agg,field,x))
            
        
        return data[0][0]
        
    @classmethod
    def avg(cls, field, **kwargs):
                
        ans = cls.aggregations('AVG', field, **kwargs)
        return ans
        
    @classmethod
    def min(cls, field, **kwargs):
        
        ans = cls.aggregations('MIN', field, **kwargs)
        return ans
        
    @classmethod
    def max(cls, field, **kwargs):
        
        ans = cls.aggregations('MAX', field, **kwargs)
        return ans
        
    @classmethod
    def sum(cls, field, **kwargs):
        
        ans = cls.aggregations('SUM', field, **kwargs)
        return ans
        
    @classmethod
    def count(cls, field = "",**kwargs):
        
        ans = cls.aggregations('COUNT', field, **kwargs)
        return ans
        
    
    
    
