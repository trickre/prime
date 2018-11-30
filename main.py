#encoding utf8
def main():
    FILE_NAME="primes.txt"
    primes=[]
    #read primes from file
    primes = file_get_primes(FILE_NAME)

    #snum: suspect number
    snum = primes[len(primes)-1]
    for cnt in range(48):
        snum += 2
        ret = is_prime(snum,primes)
        if(ret!=False):
            primes.append(snum)
            print("prime! ",end="")
            print(snum)
    print("prime discoverd : ",end ="")
    print(len(primes))

#num = []
def file_num_add(file,num):
    with open(file,mode="a",encoding="utf8") as f:
        f.writelines(num)

def file_get_primes(file):
    return [2,3]
#primesで割ってみて余りが0ならば割り切れるということ
#num:number int
#primes: list of primes at now
def is_prime(num,primes):
    for prm in primes:
        if(0==num%prm):
            return(False)
    return num
if __name__ == "__main__":
    main()