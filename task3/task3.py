text1 = open("input1.txt").read().lower()
text2 = open("input2.txt").read().lower()
latters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for_text1 = [ [text1.count(a+b)/len(text1) , a+b ] for a in latters for b in latters]
for_text2 = [ [text2.count(a+b)/len(text2) , a+b ] for a in latters for b in latters]
print(for_text1)
print('max1 is', max(for_text1))
print('max2 is', max(for_text2))
print(for_text2)
