factors = lambda n: [x for x in range(1, n + 1) if not n % x]
is_prime = lambda n: len(factors(n)) == 2
primefactors = lambda n: list(filter(is_prime, factors(n)))


def primeFactorize(n):
    n = int(n)
    f = primefactors(n)
    if is_prime(n):
        return str(n)
    else:
        return str(f[0]) + "*" + primeFactorize(n / f[0])

if __name__=='__main__':
    print("Welcome to the prime factoriser. Please enter your number,Enter quit to exit")
    while True :
        print(">>>",end='')
        num = input()
        try:
            if num:
                print(primeFactorize(num))
            if num == 'quit':
                break


        except:
            print("Please Enter a Number")