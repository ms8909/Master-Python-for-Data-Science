def bubble_sort(Bubble_list1):
    for i in range (1,len(Bubble_list1)):
        current_index = 0


        for i in range (len(Bubble_list1)-1):
            index_L = Bubble_list1[current_index]
            index_R = Bubble_list1[current_index + 1]


            if index_L> index_R:
                Bubble_list1[current_index] = index_R
                Bubble_list1[current_index + 1] = index_L
            current_index = current_index +1
    

    return(Bubble_list1)

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
bubble_sort(list1)
print("Bubble sorted list is : ",list1)
    

