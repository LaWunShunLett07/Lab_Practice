def display_mainmenu():
    print('Enter some numbers separated by commas(e.g.,5,67,32,etc)')

def calc_average(average):
    ans=sum(average)/len(average)
    print("Average is "+str(ans))

def calc_min_max_temperature(find):
    find_min=int(min(find))
    find_max=int(max(find))
    print("Minimum is "+str(find_min))
    print("Maximum is "+str(find_max))


def get_user_input():
    user_input=[]
    user_input=input()
    split=user_input.split(',')
    x_input=[float(A) for A in split]#
    print("User inputs are "+str(x_input))
    return x_input

#sort() is used with non-return value and sorted(parameter) is used with return type. sort() will sort the list in-place, mutating its indexes and returning None , whereas sorted() will return a new sorted list leaving the original list unchanged
def sort_temperature(list):
    numbers=list
    sorted_list=sorted(numbers)
    print("Sorted Temperature is "+str(sorted_list))
    return sorted_list

def calc_median_temperature(list_number):
    length=len(list_number)
    check=length%2
    if check==0:
        middle1=list_number[length//2 - 1] #// means you round to whole number-->2.5 so 2 ko yuu
        middle2=list_number[length//2]
        median=float((middle1+middle2)/2)
    elif check==1:
        median=float(list_number[length//2])#0,1,2,3,4,5
    print("Median is "+str(median))
    return median

def main():
    display_mainmenu()
    input_list=get_user_input()
    #sort_temperature(input_list) don't do it twice
    sorted_value=sort_temperature(input_list)#***
    calc_median_temperature(sorted_value)
    calc_average(sorted_value)
    calc_min_max_temperature(sorted_value)


if __name__=='__main__':
    main()