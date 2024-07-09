if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()))
    set_1 = set(arr)
    list_1 = list(set_1)
    if list_1[0]>list_1[1]:
        first_highest=list_1[0]
        second_highest = list_1[1]
    else:
        first_highest=list_1[1]
        second_highest = list_1[0]
    for i in range(len(list_1)-2):
        if list_1[i+2] >first_highest:
            second_highest = first_highest
            first_highest = list_1[i+2]
        elif list_1[i+2]>second_highest :
            second_highest = list_1[i+2]
        #elif list_1[i+2]==second_highest:
            #second_highest = list_1[i+2]
    print(second_highest)

