def occurrence(arr, size):
      
    for i in range(0, size):
        count = 0
        for j in range(0, size):
            if arr[i] == arr[j]:
                count+= 1
              
            if (count % 2 != 0):
                return arr[i]
    print (arr)     
    return -1
 
def mean(list):
        return sum(list)/len(list)

def near_mean(list):
    average = mean(list)
    low = max(list)
    for i in range(len(list)):
        value = abs(list[i]-average)
        if (value<low):
            low = value
            ans = list[i]
        print(ans)
        return ans


def avgspeed():
    speeds = []
    n = int(input("enter number of speed intervals"))
    for i in range(0,n):
            e = int(input("enter distance travelled for each interval"))
            speeds.sppend(e)
    d = 0
    for i in range(0,n):
        d = d + speeds[i]
    d = d/n
    return d
    

def missing_no(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    print(total - sum_of_A) 
    return(total - sum_of_A)


def number_of_elements(arr):
    total = sum(arr)
    n = len(arr)
    avg = total / n
    count = 0
    for i in range(n):
        if(arr[i]<avg):
           count= count+1
    print(count)
    return count


arr = [8, 3, 6, 4, 6, 8, 4, 3, 6, 8, 4, 4, 8 ]
n = len(arr)
occurrence(arr,n)

list = [1,2,3,4,5,6,7,8,9,10]
near_mean(list)


A = [1, 2, 3, 5, 6]
missing_no(A)

#number_of_elements(arr)