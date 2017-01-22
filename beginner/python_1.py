"Returning the year the user will turn 100"

def turn100 (name, age):
    years_remaining = 100 - age
    year = 2017 + years_remaining
    print "Hey", name, "you will turn 100 in the year", year
    
    
    
    
turn100("madhura", 25)



def evenodd(lists):
    listb = []
    for i in lists:
        if i <= 5:
            listb.append(i);
                
    print "There are ", len(listb), "numbers in your output, which are", listb
        

my_list = [3, 4, 6, 7, 8]

evenodd(my_list)
    
mylist = []
evenodd(mylist)



def common (a, b):
    list3 = []
    for i in a:
        if i in b:
            list3.append(i)
        
    print "There are ", len(list3), "common numbers in the two lists, and they are", list(set(list3))


mylist1 = [1, 2, 3, 4, 5, 6, 1]
mylist2 = [1, 3, 4, 5, 8, 1]

common(mylist1, mylist2)

"Madhura is a cutie pie"