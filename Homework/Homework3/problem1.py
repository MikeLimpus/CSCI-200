sequence = [1, 1, 2, 12, 3, 8, 100, 1000]
new_sequence = []
for i in range(sequence[2], len(sequence)):
    foo = sum(sequence[0, i - 1])
    if (sequence[i] > foo):
        new_sequence.append(sequence[i])
print(sequence)
print(new_sequence)
