alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
         "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T", "U", "V", "W", "X", "Y", "Z"]

try:
    indexes = []
    for i in range(3):
        index = int(input("Enter a number between 0 and 25: "))
        if 0 <= index <= 25:
            indexes.append(index)
        else:
            print("Please enter a number between 0 and 25.")

    result = ''.join([alpha[i] for i in indexes])
    print("".join(result))

except ValueError:
    print("Please enter valid numeric values.")
