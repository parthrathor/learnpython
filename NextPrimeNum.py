if __name__=='__main__':
    c=1
    while True:
        print("Do you wish to print a prime number? Enter 'yes' to do so, 'no' to not,'quit' to exit")
        n=input()
        if (n=='yes'or n=='no'or n=='quit'):
            if n=='yes':
                print(1+c)
                if c==1:
                    c-=1
                c=c+2
            if n=='no':
                continue
            if n=='quit':
                break
        else:
            print("enter from the given choice")


