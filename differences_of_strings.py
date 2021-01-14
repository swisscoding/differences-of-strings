#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Find the differences of two strings | ----\n", fg("red")))

# condition
print(stylize("Condition:", fg("green")))
print("These two strings have to be the same length.\n*** upper/lower case is ignored ***\n")

# user interaction
original_string = input("Enter original string: ").lower().rstrip()
other_string = input("Enter string to compare: ").lower().rstrip()

# function
def difference_of(string1, string2):
    differences = []
    for i in range(len(string1)):
        if string2[i] != string1[i]:
            differences.append((f"Character: {string2[i]}", f"Index: {i}"))
    return differences

# output
if len(original_string) == len(other_string):
    result = difference_of(original_string, other_string)

    if result != []:
        print(f"\nDifferences between\n\"{original_string}\" and \"{other_string}\":\n")
        for i in result:
            print(stylize(i, fg("red")))
        print()
    else:
        print(f"\nThere are no differences between\n\"{original_string}\" and \"{other_string}\".\n")
else:
    print("\nCondition not met.\n")
