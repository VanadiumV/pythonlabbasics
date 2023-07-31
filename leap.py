"""def is_leap(year):
   leap = False
    
    # Write your logic here
    
return is_leap



year = int(input())
if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):
print(leap)

else:
print(is_leap)
--------------------------------------
def is_leap(year):
   
    
    # Write your logic here
     if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):
     print("False")
     
    return leap

year = int(input())
    """
def is_leap(year):
   
    
    # Write your logic here
     
    return(((year%4==0)and(year%100!=0))or(year%400==0))

year= int(input())
if(is_leap(year)):
    print("True")
else:
    print("False")
