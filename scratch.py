import pymorphy2

text =  "Варкалось. Хливкие шорьки Пырялись по наве, И хрюкотали зелюки, Как мюмзики в мове. О бойся Бармаглота, сын! Он так свирлеп и дик А в глуще рымит исполин - Злопастный Брандашмыг."
text_split = text.split(" ")

morph = pymorphy2.MorphAnalyzer()
for a in text_split:
	parse = morph.parse(a)[0]
	result = parse.normalized
	sklon = parse.inflect({"gent"})
	lex = parse.lexeme
	print("Простой разбор", parse)
	print("Нормализовано: ", result)
	print("Склонение в родительном: ", sklon)
	print("Лексемы: ", lex)
	print("#################")

