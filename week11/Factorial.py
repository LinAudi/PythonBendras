class Math:

    @classmethod

    def factorial(cls, n):

        if n == 0:
            return 1
        else:
            return n * cls.factorial(n-1)


print(Math.factorial(5))
