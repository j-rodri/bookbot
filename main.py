def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    text = word_count(file_contents)
    print(f"There are {text} words in Frankenstein")
    char_text = char_count(file_contents)
    sorted = sorter(char_text)
    
    for items in sorted:
        if not items["char"].isalpha():
            continue
        print(f"The {items['char']} character was found {items['num']} times")

def word_count(book_text):
    book_count =book_text.split()
    counter =0
    for i in book_count:
        counter +=1
    return counter

def char_count(book):
    chars = {}

    for char in book:
        lower = char.lower()
        if lower in chars:
            chars[lower] +=1
        else:
            chars[lower] =1

    return chars

def sort_on(d):
    return d["num"]


def sorter(dict):
    sorted_list = []

    for i in dict:
        sorted_list.append({"char":i,"num":dict[i]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list





main()
