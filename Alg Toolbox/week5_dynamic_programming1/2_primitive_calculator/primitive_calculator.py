# python3
import math
# number of operations required for getting 0, 1, 2,.. , n
def compute_operations(n):
    num_operations = [0, 0] + [math.inf]*(n-1)
    for i in range(2, n+1):
       temp1, temp2, temp3 = [math.inf]*3
       temp1 = num_operations[i-1] + 1
       if i%2 == 0: temp2 = num_operations[i//2] + 1
       if i%3 == 0: temp3 = num_operations[i//3] + 1
       min_ops = min(temp1, temp2, temp3)
       num_operations[i] = min_ops
    return num_operations
def backtracking(n):
       num_operations = compute_operations(n)
       print(num_operations[n])
       # Backtracking the numbers leading to n
       nums = [n]
       while n!=1:
           if n%3 ==0 and num_operations[n]-1 == num_operations[n//3]:
               nums += [n//3]
               n = n//3
        #print(nums)
           elif n%2 ==0 and num_operations[n]-1 == num_operations[n//2]:
               nums += [n//2]
               n = n//2
        #print(nums)
           else:
               nums += [n-1]
               n = n - 1
        #print(nums)
       return nums
#if __name__=='__main__':
    #n = int(input())
   # nums=backtracking(n)
    #print(' '.join([str(i) for i in nums][::-1]))

if __name__ == '__main__':
    n = int(input())
    #output_sequence = compute_operations(input_n)
    #print(len(output_sequence) - 1)
    nums=backtracking(n)
    print(*nums)
