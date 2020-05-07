'''
#A
N = str(input())

if N == 'ABC':
    print('ARC')
else:
    print('ABC')
#B
N, K = list(map(int, input().split()))
arr = []
for i in range(K):
    C = int(input())
    A = list(map(int, input().split()))
    for ele in A:
        if ele not in arr:
            arr.append(ele)

print(N-len(arr))

#C
from collections import defaultdict 
N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
tog = defaultdict(list)
cnt = 0

for i in range(M):
    a, b = list(map(int, input().split()))
    tog[a].append(H[b-1])
    tog[b].append(H[a-1])
#print(tog)
    
for ele in tog:
    #print(tog[ele])
    #print(max(tog[ele]))
    if H[ele-1] > max(tog[ele]):
        #print('ok')
        cnt += 1

#print(len(tog))
t = N - len(tog)
#print(t)
#print(len(arr))
#print(len(tog)+N-cnt)
print(cnt+t)

#anther way by myself
N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
arr = [True for i in range(N)]
ans = 0
for i in range(M):
    A, B = list(map(int, input().split()))
    A -= 1
    B -= 1
    if H[A] <= H[B]:
        arr[A] = False
    if H[B] <= H[A]:
        arr[B] = False
for ele in arr:
    if ele == True:
        ans += 1

print(ans)

#anther way by myself
N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
arr = [[] for i in range(N)]
ans = 0
#print(arr)
for i in range(M):
    a, b = list(map(int, input().split()))
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
    
for i in range(N):
    if arr[i] == []:
        ans += 1
    else:
        if all(H[i] > H[arr[i][j]] for j in range(len(arr[i]))):
            ans += 1
print(ans)

'''
#D
X = int(input())

for A in range(100):
    for B in range(-50, 50):
        if A**5-B**5 == X:
            print(A, B)
            exit()

#ans
x = int(input())

for a in range(-118,120):
    for b in range(-118,120):
        if a**5 - b**5 == x:
            print(a, b)
            exit()

#違うアプローチ（友達に聞いた）
#cpp
'''
#include <iostream>
#define int long long
using namespace std;

int f(int a, int b) {
	return a * a * a * a * a - b * b * b * b * b;
}

signed main() {
	int x;
	cin >> x;
	
	//a = b + iとおく
	for (int i = 1; i <= 240; i++) {
		//f(b) = (b + i)^5 - b^5 (b:実数, i:非負整数)を考えると、b = -i / 2のとき最小値を取る. 
		//(wolfram alphaというサイトで計算）
		//また、b <= -i / 2の範囲ではbを小さくするほどf(b)は大きくなる。
		//b > -i / 2の範囲ではbを大きくするほどf(b)は大きくなる。
		
		//b <= -i / 2の範囲 (について、f(b) <= x (解説にならえば右辺は10^9としてもよい）となる最小のbまで探索
		//c++の場合、-5 / 2 = -2になるらしい。つまり(負の数) / (正の数)は「小数切り上げ」になってしまう。
		//今回は、小数を切り下げたいので、-(i + 1) / 2からスタートにする。i = 5のときはb = -3からスタートということ。
		for (int b = -(i + 1) / 2; ; b--) {
			int res = f(b + i, b);
			if (res > x) break;
			if (res == x) { cout << b + i << " " << b << endl; return 0; }
		}
		
		//b >= i / 2の範囲について、f(b) <= 10^9 (解説にならえば右辺は10^9としてもよい）となる最大のbまで探索
		for (int b = -(i + 1) / 2 + 1; f(b + i, b) <= x; b++) {
			cerr << b + i << ", " << b << endl;
			int res = f(b + i, b);
			if (res > x) break;
			if (res == x) { cout << b + i << " " << b << endl; return 0; }
		}
	}
	return 0;
}

'''



