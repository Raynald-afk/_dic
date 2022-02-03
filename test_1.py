# This program first asks the user the number of employers
# to enter their data for testing
# It then asks the user to type in the names of the employees 
# and their list of rankings
_dic = {}
for i in range (int(input())):
    name = input("Enter the name of employee: ")
    score = list(map(int,input("Enter the scores of the employess with space in between the scores: ")))
    _dic[name] = score
print(_dic)
