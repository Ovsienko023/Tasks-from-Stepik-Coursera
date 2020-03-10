 
with open("text.txt") as in_t, open("text_revers.txt", "w") as out_t:
    for line in reversed(in_t.readlines()):
        out_t.write(line)
       




