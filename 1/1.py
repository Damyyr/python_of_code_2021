import inputs

outcomes = dict(zip(['ascend', 'descend', 'same', 'null'], [0, 0, 0, 0]))


def compare(first, second):
    outcome = 'null'

    if first == second:
        outcome = 'same'
    elif second > first:
        outcome = 'descend'
    elif second < first:
        outcome = 'ascend'

    outcomes[outcome] += 1
    print('{0} - ({1})'.format(first, outcome))


def processChallenge2(input):
    result = []
    for i, value in enumerate(input):
        if i == 0 or i == 1:
            next

        result.append(input[i - 2] + input[i - 1] + value)

    return result


# --------------------------------------
# First challenge (answer: 1791)
# chal1 = inputs.INPUTS
# --------------------------------------
# Second challenge (answer: 1822)
chal2 = processChallenge2(inputs.INPUTS)
# --------------------------------------

inputToConsider = chal2

# Compare each value with the previous one
for i, value in enumerate(inputToConsider):
    if i == 0:
        next
    compare(inputToConsider[i - 1], value)


# Print all outcomes. Be carefull: outcome values can be accessed globally
for k, v in outcomes.items():
    print(k, v)
