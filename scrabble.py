VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}

def worth_of_words(words):
    points = {words}    #CREATE A DICTIONARY WITH WORDS AS KEY AND THEIR POINTS AS VALUE
    for i in points:     #For every word in "points" loop each letter from "VALUES", if letter is in word, add its value
        for key in VALUES:
            if key in i:
                points[i] = points[i] + VALUES.get(key)
    return max(points.value) #Return word with highest value in "points" dictionary
worth_of_words(words)
