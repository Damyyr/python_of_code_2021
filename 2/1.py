import inputs


def multiplyAll(array):
    r = 1
    for value in array:
        r = value * r

    return r


# Answer 2102357
def chal1(instruction, value, results):
    match instruction:
        case 'down':
            results['depth'] += value
        case 'up':
            results['depth'] -= value
        case 'forward':
            results['horizontal'] += value
        case _:
            raise 'Error'

    return results


# Answer 2101031224
def chal2(instruction, value, results):
    match instruction:
        case 'down':
            results['aim'] += value
        case 'up':
            results['aim'] -= value
        case 'forward':
            results['horizontal'] += value
            results['depth'] += results['aim'] * value
        case _:
            raise 'Error'

    return results

# ------------------------- Runtime


def main(name, inputToConsider):
    chal1Results = {'horizontal': 0, 'depth': 0}
    chal2Results = {'horizontal': 0, 'depth': 0, 'aim': 0}

    for (k, v) in inputToConsider:
        # print('Instructions are: {0} -> {1}'.format(k, v)) # debug printing
        chal1Results = chal1(k, v, chal1Results)
        chal2Results = chal2(k, v, chal2Results)

    print('Chalenge 1:')
    print(chal1Results)
    print('Results: {0}'.format(multiplyAll(chal1Results.values())))
    print('-----')
    print('Chalenge 2:')
    print(chal2Results)
    toMultiply = [chal2Results['horizontal'], chal2Results['depth']]
    print('Results for {0} values: {1}'.format(name, multiplyAll(toMultiply)))


main('test', inputs.TEST)
main('real', inputs.INPUTS)
