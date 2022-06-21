def isPrime(number: int) -> bool:
    counter = 0
    for i in range(1, number+1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        print("Is prime")
    else:
        print("Is not prime")

def run():
    print(isPrime(4))

if __name__ == '__main__':
    run()