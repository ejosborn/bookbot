def main():
    book_path = "Books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    num_letters = count_letters(text)
    printReport(num_words, num_letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    #makes all letters lower case in the text
    lower_letters = text.lower()
    
    #iterate through the letters
    for letter in lower_letters:
        #only takes letters (no numbers or characters)
        if letter.isalpha():
            #if exists, increment
            if letter in letter_dict:
                letter_dict[letter] += 1
            #if not, add to dictionary
            else:
                letter_dict[letter] = 1
    return letter_dict

def printReport(num_words, num_letters):
    print("=== Report of Frankenstein.txt ===")
    print(f"{num_words} words found in the book")

    for key, value in num_letters.items():
        print(f"The '{key}' letter was found '{value}' times")


main()