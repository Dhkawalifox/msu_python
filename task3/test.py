text1 = open("input1.txt").read().lower()
text2 = open("input2.txt").read().lower()
latters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for_text1 = [ [text1.count(a+b)/len(text1) , a+b ] for a in latters for b in latters]
for_text2 = [ [text2.count(a+b)/len(text2) , a+b ] for a in latters for b in latters]
#for_text1 = [ text1.count(a+b)/len(text1)  for a in latters for b in latters]
#for_text2 = [ text2.count(a+b)/len(text2)  for a in latters for b in latters]
#print('max1 is', max(for_text1))
#print('max2 is', max(for_text2))
#print(for_text1)
#print(for_text2)
#for_text1 = [ for_text1[a[0]] for a in latters for b in latters]
#print([a for a in enumerate(for_text1) for b])
list1 = [ [abs(i[1][0] - for_text2[i[0]][0]) , i[1][1] ] for i in enumerate(for_text1)]
print(max(list1))
#list1 = [ for_text1[i[0]]-for_text2[i[0]] for i in enumerate(for_text1)]
print(list1)
