text = open("input.txt").read().lower()
latters = "qwertyuiopasdfghjklzxcvbnm"
alltext = [ (sum(1 for x in text if x == i)/len(text), i) for i in latters]
print(alltext)
print('max is', max(alltext))
