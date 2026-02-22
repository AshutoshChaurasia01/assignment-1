def two_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second

def reverse(arr):

  rev = []

  for i in range(len(arr)-1, -1, -1):
      rev.append(arr[i])
      return rev

def find_min_max(arr):
    if len(arr) == 0:
        return "Empty list"

    minimum = maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return minimum, maximum

def find_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total

def count_freq(arr):
  for i in range(len(arr)):
      count=0
      for j in range(i,len(arr)):
          if arr[i]==arr[j]:
            count+=1
      print(f"The frequencu of {arr[i]} is {count}")

  return

def check_array(arr):
  sort=True
  for i in range(len(arr)-1):
    if arr[i]<arr[i+1] or arr[i]>arr[i+1]:
      pass
    else:
      sort=False
  print(f'Sorted: {sort}')
check_array(lst)
print(lst)print(lst)

def check_pair(arr,target):
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      if arr[i]+arr[j]==target:
        print(f'{i} and {j}sum up to {target}')
      else:
        pass
check_pair(lst,3)

def remove_dups(arr):
  dup=[]
  for i in range(len(arr)):
    if arr[i] in dup:
      pass
    else:
      dup.append(arr[i])
  return dup
remove_dups(lst)

def remove_element(arr,target):
  for i in arr:
    if i == target:
      arr.remove(i)
  return arr
print(remove_element(lst,1))

def missing_number(arr):
    n = len(arr) +1

    total = (n*(n+1))/2
    print(total)
    

    arr_sum = 0
    for x in arr:
        arr_sum += x

    return total - arr_sum
def merge_sorted(arr, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr) and j < len(arr2):
        if arr[i] < arr2[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr):
        res.append(arr[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res
 
def find_dups(arr):
  dup=[]
  for i in range(len(arr)):
    if arr[i] in dup:
      pass
    else:
      dup.append(arr[i])
  return dup

def intersection(arr1,arr2):
  common=[]
  for i in arr1:
    for j in arr2:
      if i ==j and j not in common:
        common.append(j)
  return common
arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,8,9]
print(intersection(arr1,arr2))


def union(arr1,arr2):
  union=[]
  for i in arr1:
    if i not in union:
      union.append(i)
  for j in arr2:
    if j not in union:
      union.append(j)
  return union

union(arr1,arr2)

def leaders(arr):
    res = []

    for i in range(len(arr)):
        leader = True
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            res.append(arr[i])

    return res

def move_zeros(arr):
  for i in range(len(arr)):
    if arr[i]==0:
      poped=arr.pop(i)
      arr.append(poped)

arr=[0,60,704,6,7,5,0,0,6,7,5,7,0]
move_zeros(arr)
print(arr)

def subarray_sum(arr, target):
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == target:
                return arr[i:j+1]
    return None

def kth_smallest(arr, k):
    temp = arr[:]

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]

    return temp[k-1]

def all_subarrays(arr):
    res = []

    for i in range(len(arr)):
        sub = []
        for j in range(i, len(arr)):
            sub.append(arr[j])
            res.append(sub[:])

    return res

def max_sum_subarray(arr):
    max_sum = arr[0]

    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s > max_sum:
                max_sum = s

    return max_sum

def majority_element(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > n//2:
            return arr[i]

    return None

def peak(arr):
  peak=[]
  for i in range(1,len(arr)-1):
    if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
      peak.append(arr[i])
  return peak
peak(arr)


def sort012(arr):
    c0 = c1 = c2 = 0
    for x in arr:
        if x == 0:
            c0 += 1
        elif x == 1:
            c1 += 1
        else:
            c2 += 1
    res = []
    for i in range(c0):
        res.append(0)
    for i in range(c1):
        res.append(1)
    for i in range(c2):
        res.append(2)

    return res

def product_except_self(arr):
    res = []

    for i in range(len(arr)):
        p = 1
        for j in range(len(arr)):
            if i != j:
                p *= arr[j]
        res.append(p)

    return res



def equilibrium_index(arr):
    for i in range(len(arr)):
        left = 0
        right = 0
        for j in range(i):
            left += arr[j]
        for j in range(i+1, len(arr)):
            right += arr[j]
        if left == right:
            return i
    return -1

def nax_pair(arr):
  max_prod=arr[0]*arr[1]
  pair=(arr[0],arr[1])
  for i in range(1,len(arr)):
    for j in range(i,len(arr)):
      if arr[i]*arr[j]>max_prod:
        pair=(arr[i],arr[j])

  return pair

def max_difference(arr):
    max_diff = arr[1] - arr[0]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = arr[j] - arr[i]
            if diff > max_diff:
                max_diff = diff

    return max_diff

def all_subarrays(arr):
    res = []

    for i in range(len(arr)):
        sub = []
        for j in range(i, len(arr)):
            sub.append(arr[j])
            res.append(sub[:])

    return res

