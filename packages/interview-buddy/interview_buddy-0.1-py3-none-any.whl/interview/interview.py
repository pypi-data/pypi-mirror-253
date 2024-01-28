class Interview:
    def __init__(self,data=None,data1=None) -> None:
        self.data = data
        self.data1 = data1

    def fibonacci_series(self):
        fibonacci = [0,1]
        for i in range(2,self.data):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
            print(f"The sum {fibonacci[i-2]}+{fibonacci[i-1]} = {fibonacci[i-1]+fibonacci[i-2]}")
            print(fibonacci)
    
    def palindrom(self):
        L = 0
        R = len(self.data)-1
        while L<R:
            print(f"{self.data[L]} == {self.data[R]}")
            if self.data[L] != self.data[R]:
                return False
            L+=1
            R-=1
        return True

    def bubble_sort(self):
        if isinstance(self.data,str):
            self.data = list(self.data)
        for i in range(len(self.data)-1,0,-1):
            for j in range(i):
               print(f"Is {self.data[j]} is greater than {self.data[j+1]}")
               if self.data[j] > self.data[j+1]:
                   self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
        return self.data

    def insertion_sort(self):
        for i in range(1,len(self.data)):
            temp = self.data[i]
            j = i - 1
            print(f"Is {self.data[i]} greater than {self.data[j]}")
            while temp<self.data[j] and j>-1:
                self.data[j+1] = self.data[j]
                self.data[j] = temp
                j -= 1
        return self.data

    def anagram(self):
        data_sorted = sorted(self.data)
        data_sorted1 = sorted(self.data1)
        for i in range(len(data_sorted)):
            print(f"Is {data_sorted[i]} equal to {data_sorted1[i]}")
            if data_sorted[i] != data_sorted1[i]:
                return False
        return True

    def binary_search(self):
        self.data.sort()
        L = 0
        R = len(self.data)
        while L<R:
            mid = (L+R)//2
            print(f"{self.data[mid]} is equal to {self.data1}")
            if self.data[mid] == self.data1:
                return self.data[mid]
            if self.data[mid]<self.data1:
                L = mid + 1
            elif self.data[mid]>self.data1:
                R = mid - 1
        return - 1
    
    def min_(self):
        min = self.data[0]
        for i in range(len(self.data)):
            print(f"min -> {min} current_value -> {self.data[i]}")
            if min>self.data[i]:
                min = self.data[i]
        return min

    def max_(self):
        max = self.data[0]
        for i in range(len(self.data)):
            print(f"Max value -> {max} current_value-> {self.data[i]}")
            if max<self.data[i]:
                max = self.data[i]
        return max
    
    def reverse(self):
        for i in range(len(self.data)-1,-1,-1):
            print(self.data[i])
