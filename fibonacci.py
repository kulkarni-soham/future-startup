class Demo:
    def fib(self,n):
        if n<=1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

print(Demo().fib(0))