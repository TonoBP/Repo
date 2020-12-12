
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []

pos_f = open("positive_words.txt")
for lin in pos_f:
    if lin[0] != ';' and lin[0] != '\n':
        positive_words.append(lin.strip())


negative_words = []
pos_f = open("negative_words.txt")
for lin in pos_f:
    if lin[0] != ';' and lin[0] != '\n':
        negative_words.append(lin.strip())

def strip_punctuation(x):
    for char in x:
        if char in punctuation_chars:
            x = x.replace(char, "")
    return x



def get_pos(x):
    pos_count = 0
    s = x.lower()
    s1 = strip_punctuation(s)
    lista = s1.split(" ")

    for i in positive_words:
        if i in lista:
            pos_count = pos_count + 1
    return pos_count

def get_neg(x):
    neg_count = 0
    s = x.lower()
    s1 = strip_punctuation(s)
    lista = s1.split(" ")

    for i in negative_words:
        if i in lista:
            neg_count = neg_count + 1
    return neg_count

orig_tw = open("project_twitter_data.csv","r")
lmd = orig_tw.read()
lmd_separado = lmd.split(",")
pos_tw = get_pos(lmd_separado[0])
neg_tw = get_neg(lmd_separado[0])
ret = lmd_separado[1]
rep = lmd_separado[2]
print(pos_tw)

final_tw = open("resulting_data.csv", "w")
final_tw.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
final_tw.write("\n")

#final_tw.write(ret,",",rep,",",pos_tw,",",neg_tw,",",pos_tw - neg_tw)
                   
