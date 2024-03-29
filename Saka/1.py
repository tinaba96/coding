#1. [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]  -> [0, 4, 2, 4, 6, 8, 1, 3, 5, 1, 9]

from typing import List

def even_first_odd_last(num: List[int]) -> None:
    i = 0
    j = len(num) -1 
    while i < j:
        if num[i]%2 == 0:
            i += 1
        else:
            num[i], num[j] = num[j], num[i]
            j -= 1
        #print(num)
    return num
 

'''
2. Maximum subarray sum
Input [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output 14 (3, 6, -1, 2, 4)
'''

def Maxarray(arr: List[int]) -> int:
    ans = 0
    tmp = 0
    for i in range(len(arr)):

        '''
        if 0 > tmp + arr[i]:
            tmp = 0
        else:
            tmp += arr[i]
        ''' 
        tmp = max(0, tmp+arr[i])


        #tmp = max(arr[i], tmp + arr[i])
        if ans < tmp:
                ans = tmp
        #ans = max(ans, tmp)
            
    return ans
 

'''
3. Maximum circular subarray sum
Input [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output 15 (2, 1, -2, 3, 6, -1, 2, 4)
'''

def MaxCirculararray(arr: List[int]):
    tot = sum(arr)
    inverse = []
    for ele in arr:
        inverse.append(-ele)
    return tot + Maxarray(inverse)



if __name__ == '__main__':
    '''
    l =  [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    even_first_odd_last(l)
    print(l)
    '''

    print(Maxarray([1, -2, 3, 6, -1, 2, 4, -5, 2]))

    print(MaxCirculararray([1, -2, 3, 6, -1, 2, 4, -5, 2]))












