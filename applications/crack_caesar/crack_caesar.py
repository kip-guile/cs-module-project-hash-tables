# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
def decode(path):
    freq = {}
    freq["E"] = 11.53
    freq["T"] = 9.75
    freq["A"] = 8.46
    freq["O"] = 8.08
    freq["H"] = 7.71
    freq["N"] = 6.73
    freq["R"] = 6.29
    freq["I"] = 5.84
    freq["S"] = 5.56
    freq["D"] = 4.74
    freq["L"] = 3.92
    freq["W"] = 3.08
    freq["U"] = 2.59
    freq["G"] = 2.48
    freq["F"] = 2.42
    freq["B"] = 2.19
    freq["M"] = 2.18
    freq["Y"] = 2.02
    freq["C"] = 1.58
    freq["P"] = 1.08
    freq["K"] = 0.84
    freq["V"] = 0.59
    freq["Q"] = 0.17
    freq["J"] = 0.07
    freq["X"] = 0.07
    freq["Z"] = 0.03

    letterCounts = {}
    letterfreq = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in alphabet:
        letterCounts[i] = 0
        letterfreq[i] = 0

    total = 0

    encrypted = ''

    with open(path) as file:
        encrypted = file.read()

    for char in encrypted:

        if char in letterCounts:
            letterCounts[char] += 1
            total += 1

    for i in alphabet:
        letterfreq[i] = letterCounts[i] / total

    letterfreq = letterfreq.items()
    freq = freq.items()

    letterfreq = sorted(letterfreq, key=lambda letter: letter[1])
    freq = sorted(freq, key=lambda letter: letter[1])

    decreasing_freq = ''.join([letter_data[0] for letter_data in letterfreq])
    freq_decreasing = ''.join([letter_data[0] for letter_data in freq])

    table = encrypted.maketrans(decreasing_freq, freq_decreasing)
    decrypted = encrypted.translate(table)

    print(decrypted)


decode('applications/crack_caesar/ciphertext.txt')
