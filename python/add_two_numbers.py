'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
l1= [9,9,9,9,9,9,9]
l2= [9,9,9,9]
def solution(l1:list, l2:list):
    shallow_l1 = l1
    shallow_l2 = l2
    srt_l1= ''
    srt_l2= ''
    result=[]
    while (len(shallow_l1) != len(shallow_l2)):
        if len(shallow_l1) > len(shallow_l2):
            shallow_l2.append(0)
        else:
            shallow_l1.append(0)
    for i in range(len(shallow_l1)):
        srt_l1 +=str(shallow_l1[i])
        srt_l2 +=str(shallow_l2[i])
    sum = int(srt_l1)+int(srt_l2)
    for i in range(len(str(sum))):
        result.append(int(str(sum)[i]))
    result.reverse()
    return print(result)
        
        
solution(l1, l2)