from sample_data import sample_articles

numeros = [1, 2, 3, 4, 5]
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)

print(numeros)
print(cuadrados)

# def cuadrado(n):
#     return n**2

# cuadrados_map = list(map(cuadrado, numeros))
# print(cuadrados_map)

cuadrados_map_lambda = list(map(lambda x: x**2, numeros))
print(cuadrados_map_lambda)


def get_reading_times(article: dict) -> dict:
    
    reading_time_minutes = len(article["description"]) / 200
    article["reading_time_minutes"] = f"{reading_time_minutes} min read"
    return article

articles_with_reading_time = map(get_reading_times, sample_articles)
for article in articles_with_reading_time:
    print(f"Title: {article['title']}")
    print(f"Reading Time: {article['reading_time_minutes']}")