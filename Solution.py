#importing numpy library
import numpy as np
import time

#function definition
"""
keypad : create standard push button telephone keypad
l_location : position of * key
r_location : position of # key -- these are starting position
tot_cost : smallest amount of euclidean distance both fingers together have moved -- starts with value 1
result : return tuple 
n:length of the telephone number
pos_x,pos_y: position of ith key
l_cost, r_cost : cost (timing/euclidean distance) for moving left or right finger
shortest_ecludian_path : shortest ecluidian distance 
"""
# k corresponds to the number of keys on the key board
# n corresponds to the length of the telephone number
def compute_laziest_path(telephone_number: str):
    keypad=np.matrix([["1","2","3"],["4","5","6"],["7","8","9"],["*","0","#"]])
    l_location=(3,0)
    r_location=(3,2)
    tot_cost=1
    result=[(keypad[l_location],keypad[r_location])]
    n=len(telephone_number)
    try:
        if n>0:
            for i in range(n):
                pos_x,pos_y=np.where(keypad==telephone_number[i])
                l_cost=np.linalg.norm(np.array((l_location))-np.array((pos_x,pos_y)))
                r_cost=np.linalg.norm(np.array((r_location))-np.array((pos_x,pos_y)))
                shortest_ecludian_path=min(l_cost,r_cost)
                if shortest_ecludian_path==float(l_cost):
                        l_location=(pos_x[0],pos_y[0])
                        result.append((keypad[l_location],keypad[r_location]))
                        tot_cost+=1

                else:
                    r_location=(pos_x[0],pos_y[0])
                    result.append((keypad[l_location],keypad[r_location]))
                    tot_cost+=1
        return (float(tot_cost),result)
    except BaseException as e:
        print("Invalid Input")
        
#function call and test case
test=compute_laziest_path("110")
print("test case result = ",test)

start_time=time.time()
compute_laziest_path("110")
print("execution time ",(time.time()-start_time)*1000,"ms" )

# let's say C=cost, n=no. of time it runs 
# for constant : n=1 , for loop n=n+1 , within loop : n=n
#max run time : C*1+C*1+C*1+C*1+C*1+C*1+C*1+C*1+C*(n+1)+C*n+C*n+C*n+C*n+C*n+C*n+C*n+C*n+C*n = 9*C*1+10*C*n =O(n)+O(1)
# if k :corresponds to the number of keys on the keyboard, then = O(nk)+O(1*k) ~ O(nk)
print("Time Complexity = O(nk)") 
print ("Space Complexity : Linear space complexity occurs when the program runs")
# p.s : total space required : depends on the input length 



