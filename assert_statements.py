def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'Ingresa un número'
    print(divisors(int(num)))
    print('Programa terminado')

if __name__ == '__main__':
    run()