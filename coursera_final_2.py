stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""
lst = org.split(" ")

for word in lst:
    if word not in stopwords:

        acro = acro + upper.word[0]
