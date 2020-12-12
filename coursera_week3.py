words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for i in words:
    if i[-1] == "e":
        i = i+"d"
    else:
        i = i+"ed"
    past_tense.append(i)
print (past_tense)
