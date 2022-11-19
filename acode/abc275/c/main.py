import math
import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

mp = []
for i in range(9):
    A = str(input())
    mp.append(A)

al = set()
 
ans = 0
for i in range(9):
    for j in range(9):
        for p in range(9):
            for q in range(9):
                if mp[i][j] == mp[p][q] and mp[i][j] == '#': # find 2 points
                    d = int(10*math.sqrt((i-p)**2 + (j-q)**2)) # get length
                    for ta in range(9):
                        for tb in range(9):
                            if mp[ta][tb] == '#': # 3rd point should also be #
                                d2 = int(10*math.sqrt((p-ta)**2 + (q-tb)**2)) # get length
                                if d == d2: # if both length is same
                                    for h in range(9):
                                        for w in range(9): # 4th point
                                            if mp[h][w] == '#': # whether 4th length is also #
                                                d3 = int(10*math.sqrt((h-ta)**2 + (w-tb)**2)) 
                                                d4 = int(10*math.sqrt((i-ta)**2 + (j-tb)**2))

                                                #if d4 == d3 and i != p and p != ta and ta != h and j != q and q != tb and tb != w:
                                                if d2 == d3 and d3 == d4: #checking all 4 length are same
                                                    #print('o')
                                                    ans += 1
                                                #if d2 == d3 and d4 == d3 and (i,j) != (p,q) and (p,q) != (ta, tb) and (ta,tb) != (h, w) and (h,w) != (i, j):
                                                #if d4 == d3 and (i, j, p, q, ta, tb, h, w) not in al:
                                                    #print(al)
                                                    #al.add((i, j, p, q, ta, tb, h, w))
                                                    #if abs(p-i)//abs(q-j) == abs(h-ta)//abs(w-tb):
                                                    '''
                                                    print(i, j)
                                                    print(p, q)
                                                    print(ta, tb)
                                                    print(h, w)
                                                    print('----')
                                                    '''
                                                    #ans += 1
print((ans+1)//4)

# same length for 4 lines is not the only condition for squares
# also length of both diagonal is also not enough
# it is better to use rotation just like a video tutorial 
# https://www.youtube.com/watch?v=WHAC0LfyPcw

# https://sugim48.hatenadiary.org/entry/20141007/1412679470
'''
4 点間の距離を 4C2=6 通り計算し、それらの比が 1:1:1:1:√2:√2 になっていればよい。
ルートを取ると誤差が怖いので、実際には距離の自乗の比が 1:1:1:1:2:2 になっているか確認する。
ただし、すべての距離が 0 になる場合に注意。
'''
        



