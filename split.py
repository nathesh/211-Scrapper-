def  write_one(body,n):
	name = "211_corpus_" + str(n) + ".html"
	file = open(name, "w")
	body =  '\n '.join(body)
	file.write(body)



f = open("211_corpus.html", "r")
body = []
length = 1
n = 1
for line in f:
    if length == 100:
        if body:
            write_one(body,n)
            n += 1
        body = []
        length = 1
    body.append(line)
    length += 1
if body:
    write_one(body,n)

f.close()


