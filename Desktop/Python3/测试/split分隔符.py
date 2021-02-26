# str.split(str = "", num = string.count(str))
# 参数:
# str -- 分隔符,默认为所有的空字符，包括空格，换行符('\n'),制表符('\f')
# num -- 分隔此时默认为-1，分隔所用
sentence = 'Hello word !'
sentence_list = sentence.split()
print(len(sentence_list))
print(sentence_list)
sentence_list_2 = [i.lower() for i in sentence.split('\f')]
print(sentence_list_2)
for W in sentence_list_2:
    print(W)
