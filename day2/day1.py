
def func1(*args):  
  if args[0] == "test1":
    # print(args[1])
  # print(args[0])
  # print(args[1])
    print("### function call ######")


def func2(v1, v2, v3):
  print(v2)
  print(v1)
  print(v3)
  print("#########")

def func3(v1, v2):
  print(v2)
  print(v1)
  print("#########")


func1("test1", "vinod", "if test2", "test3")
func2("day1", 1, "day2")
func3("day4",3)


# This function uses global variable s 
def f():  
  global s 
  print(s) 
  s = "Look for Geeksforgeeks Python Section"
  print(s)   


s = "I love"
f() 
s = "I love 2"
f() 
print("global ",s)

# "I love" ----
# "Look for Geeksforgeeks Python Section" --
# "I love 2"
# "Look for Geeksforgeeks Python Section"
# "Look for Geeksforgeeks Python Section"
# "global Look for Geeksforgeeks Python Section"