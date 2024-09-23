def my_function(fname):         # takes Only One Argument
     print(fname + " kumar")


def my_function1(fname ="kuch nii"): # takes one Argument as well as set default value
     print(fname + " ki jai ")


def my_function2(fname, lname): # takes Only Two Argument
      print(fname + " " + lname)

def my_function3(fname='Nandini', lname='Mishra'): # takes Only Two Argument with default values
      print(fname + " " + lname)

# Arbitrary Arguments *args

def my_function4(*name):      # taking multiple value at a time
      print("Your Data is : ",name) # print whole tuple
      #print(*name)
      #print(name)

# here name work as tuple argument that is iteratable      

def my_function5(*name):  # tuple name using loop to print it
        for i in name:
              print(i)  


# KeyWord Arguments

# You can also Argments with the key =value syntax
# this way the order of the arguments does not matter

def my_function6(child3,child2,child1):
      print("The youngest child is " + child3)


# Arbitrary keyword Arguments **Kwargs
#  here argument recive in form of dictionary that is also iteratable

def my_function7(**kid):
       print("His last name is " +kid["lname"])
       #print(**kid)
       print(kid)

# dictionary is also iterable than we use loop to print value one by one
def my_function7(**kid):
      for i in kid:
            print(i)
            print(i , kid[i])



# List, passing List as an Argument in function

def my_function8(food):
      for x in food:
            print(x)


fruits = ["Apple","Banana","Mango"]
my_function8(fruits)




 # my_function('Gaurav')
 # my_function1('Nandini')
 # my_function1()
 # my_function2('Gaurav','Kushwaha')
 # my_function3()
 # my_function3('Gaurav')

 # my_function4(1,2,3,4,5)
 # my_function4('Gaurav','shubham','Atendra','Diksha')

# my_function5(1,2,3,4,5,6)
# my_function5("Gaurav","nandini","Rahul","Adarsh")

# my_function6(child1 ="Gaurav",child2 ="Shubham",child3 ="Atendra")
# my_function6("Gaurav","shubham","Atendra")
# my_function6("shubham") single argument not supported                  

# my_function7(fname="Gaurav",lname="kushwaha")