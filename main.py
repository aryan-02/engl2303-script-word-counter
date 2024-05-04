# Python Project Submission for ENGL 2303
# OnlineGDB Login Name: aryan-02
# Due date: April 17, 2024
# Name: Aryan Mediratta
# UTA ID: 1001910692
# I used Spider-Man : No Way Home from https://assets.scriptslug.com/live/pdf/scripts/spider-man-no-way-home-2021.pdf



import string # Used for string.punctuation
import matplotlib.pyplot as plt

# fileName stores the name of the input file for the script
fileName = "myMarvelScript.txt"

focusWords = ["phone", "tv", "radio", "tiktok"]

# Read the entire file as a string entireScript
entireScript = ""
with open(fileName) as scriptFile:
    entireScript = scriptFile.read()



# The number of lines in the script will simply be one more than
# the number of occurrences of the newline character '\n'
numLines = entireScript.count("\n") + 1


print(f"The script contains {numLines} lines.\n\n")


# Standardize all letters to lowercase
entireScript = entireScript.lower()

# Tokenize the script based on whitespace
contents = entireScript.split()

totalWords = len(contents)

print(f"We found a total of {totalWords} words in the script")


# Repeat for each space-delimited token (word) in the script
for i in range(len(contents)):
    # Remove all punctuation at the front and back of each word.
    contents[i] = contents[i].strip(string.punctuation + "‘’“”")

# Store the frequency of each word in a dictionary
word_frequencies = dict()

for word in contents:
    if word not in word_frequencies.keys():
        # If we have not seen this word before, add it to our list with a count of 1
        word_frequencies[word] = 1
    else:
        # If we have seen the word before, simply increment its count
        word_frequencies[word] += 1

# Turn the dictionary back into a list using list comprehension
frequency_list = [(key, value) for key, value in word_frequencies.items()]

totalUniqueWords = len(frequency_list)

print(f"Of those, there were {totalUniqueWords} unique words.")

# Sort the words in descending order by the second item [1] of the tuple (frequency)
frequency_list.sort(key = lambda x : x[1], reverse=True)

optionChosen = -1
while optionChosen != 0:
    print("""
==================== MENU ====================

0. Exit
1. Display all word-counts sorted by frequency (decreasing)
2. Display all word-counts sorted alphabetically (A-Z)
3. Show focus words
4. Dump data to file
          """)
    optionChosen = int(input("Enter your option: "))
    if optionChosen == 1:
        frequency_list.sort(key = lambda x: x[1], reverse=True) # Sort by index 1 of tuple
        for word, count in frequency_list:
            print("%4d \t%s" % (count, word))
    
    elif optionChosen == 2:
        frequency_list.sort(key = lambda x: x[0]) # Sort by index 0 of tuple
        for word, count in frequency_list:
            print("%4d \t%s" % (count, word))
    elif optionChosen == 3:
        focusw = []
        focusf = []
        for focusWord in focusWords:
            if(focusWord not in word_frequencies.keys()):
                print(f"{focusWord} did not occur in the script.")
            else:
                focusw.append(focusWord)
                focusf.append(word_frequencies[focusWord])
                print(f"{focusWord} occurred in the script {word_frequencies[focusWord]} times.")
        plt.figure(figsize=(10, 6))
        plt.bar(focusw, focusf)
        plt.xlabel("Words")
        plt.ylabel("Frequencies")
        plt.title("Comparison of Word Frequencies in Spider-Man: No Way Home")
        plt.show()
    elif optionChosen == 4:
        with open("output.txt", 'w') as outFile:
            outFile.write(f"The script contains {numLines} lines.\n\n")
            outFile.write(f"We found a total of {totalWords} words in the script\n")
            outFile.write(f"Of those, there were {totalUniqueWords} unique words.\n")
            frequency_list.sort(key = lambda x: x[1], reverse=True) # Sort by index 1 of tuple
            for word, count in frequency_list:
                outFile.write("%4d \t%s\n" % (count, word))
            outFile.write("\n\n")
            for focusWord in focusWords:
                if(focusWord not in word_frequencies.keys()):
                    outFile.write(f"{focusWord} did not occur in the script.\.")
                else:
                    outFile.write(f"{focusWord} occurred in the script {word_frequencies[focusWord]} times.\n")
    input("Press the enter key to continue.")

    