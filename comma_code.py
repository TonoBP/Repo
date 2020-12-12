def comma(lista):
    for i in range((len(lista)-1)):
        print(lista[i] + ", ")
    print("and " + lista[-1])

spam = ["apples", "bananas", "tofu", "cats"]

comma (spam)
