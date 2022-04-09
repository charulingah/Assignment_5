#Write a Python class to implement pow(x, n)

'''Explanation:
User should be able to find the nth power of the x.(i.e x*x*x*x...n times)
You must implement it using Class
'''

Solution-->


class nth_pow:

  def pow(self, x, n):

       if x==0 or x==1 or n==1:

           return x

       if x==-1:

           if n%2 ==0:

               return 1

           else:

               return -1

       if n==0:

           return 1

       if n<0:

           return 1/self.pow(x,-n)

       val = self.pow(x,n//2)

       if n%2 ==0:

           return val*val

       return val*val*x

#user input or you can add the user input by commenting it in
x=int(input("Enter base value: "))
n=int(input("Enter power value: "))

#way to call via user input
output = nth_pow().pow(x, n)
print("sample Input:\nx:",x,"\nn:",n,"\nSample Output:",output)

#without taking user input the method can be called this way --> nth_pow().pow(10,2)


sample Input:
x: 10 
n: 2 
Sample Output: 100



