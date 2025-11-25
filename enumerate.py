from sample_data import sample_articles

lista = ["Python", "Java", "C++", "JavaScript"]
# counter = 1
# for item in lista:
#     print(f"{counter}: {item}")
#     counter += 1

for index, item in enumerate(lista):
    print(f"{index}: {item}")

print("===================================")
for index, article in enumerate(sample_articles, start=1):
    print(f"{index}: {article['title']}")