'''A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to
divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will
be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially
around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful.
Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are  prisoners and  pieces of candy. The prisoners arrange themselves in seats numbered  to .
Let's suppose two is drawn from the hat. Prisoners receive candy at positions . The prisoner to be warned sits in chair number .

Sample Input 0

2
5 2 1
5 2 2

Sample Output 0

2
3

'''


N = int(input())
arr = []
for _ in range(N):
    n, m, s = map(int, input().rstrip().split())
    a = (m + s - 1) % n
    if a == 0: a = n
    arr.append(a)
print(*arr, sep='\n')
