def run():
#    dictionary = {}
#       for i in range (1, 101):
#           dictionary[i] = i**3

#    print(dictionary)

#solo los que no son divisible por 3

#    dictionary = {}
#       for i in range (1, 101):
#           if i % 3 != 0:
#               dictionary[i] = i**3

#    print(dictionary)

#with dictionary comprehensions
    #dictionary = {i: i**3 for i in range (1, 101) if i % 3 != 0}

    #print(dictionary)

#challenge
    dictionary = {i: round(i**(1/2), 2) for i in range (1, 1001)}
    
    print(dictionary)


if __name__ == '__main__':
    run()