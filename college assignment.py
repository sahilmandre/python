def main():
    print("Concatenation")

    a = "sahil"
    b = "mandre"

    print(a + " " + b)

    print("repeatation process below")
    print(a * 3)

    print("Indexing elements")

    list1 = ['a', 'b', 'c', 'd']
    index = list1.index("c")
    print('the index of list1 is', index)

    print("length of the string")
    word = "sahil"
    print(len(word))

    sent = "i am sahil"
    print(sent.isupper())

    print(sent.upper())

    sent1 = "I AM LEARNING PYTHON"
    print(sent1.lower())

    print(len(sent1))

    print(min("This", "software", "is", "pycharm"))
    print(max("This", "software", "is", "pycharm"))


if __name__ == '__main__': main()
