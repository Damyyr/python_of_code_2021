import inputs

def initializeOnesHash(nbBits):
    returned = {}
    for i in range(nbBits):
        returned[i] = 0
        
    return  returned

def gamma(bits, inputSize):
    returned = []
    
    for b in bits:
        if bits[b] - inputSize / 2 < 0:
            returned.append(0)
        else:
            returned.append(1)
    
    return returned 


def epsilon(bits, inputSize):
    returned = []
    
    for b in bits:
        if bits[b] - inputSize / 2 < 0:
            returned.append(1)
        else:
            returned.append(0)
    
    return returned 

def main(name,  input):
    print('Output for {0}'.format(name))
    
    inputSize = len(input)
    rowSize = len(input[0])
    ones = initializeOnesHash(rowSize)
    
    print('ones looks like {0}'.format(ones))
    
    for row in input:
        for i in range(rowSize):
            ones[i] += int(row[i])
    
    print('ones looks like {0}'.format(ones))
    
            
    print(gamma(ones, inputSize))
    print(epsilon(ones, inputSize))
    
    print('End of {0} output'.format(name))
    
main('Test', inputs.TEST)
main('Chal1', inputs.INPUT)