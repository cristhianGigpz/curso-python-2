# cuadrado = []
# for x in [1, 2, 3, 4, 5]:
#     cuadrado.append(x**2)

# print(cuadrado)

# cuadrado = [x**2 for x in [1, 2, 3, 4, 5]]
# print(cuadrado)

from sample_data import sample_articles


# def extract_titles_traditional(articles):
#     titles = []
#     for article in articles:
#         if len(article["title"]) > 20:
#             titles.append(article["title"])
#     return titles

# print(extract_titles_traditional(sample_articles))


# # [expression for item in iterable [if condition]]
# def extract_titles_comprehension(articles):
#     return [article["title"] for article in articles if len(article["title"]) > 20]


# print(extract_titles_comprehension(sample_articles))


def extract_articles_sumaries(articles):
    return {
        article["title"]: article["description"] for article in articles if len(article["title"]) > 20
    }

print(extract_articles_sumaries(sample_articles))


def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        sources.add(article["source"]["name"])
    return sources

print("==============================")
print(get_sources_traditional(sample_articles))

#{expression for item in iterable [if condition]}
def get_sources_comprehension(articles):
    return {article["source"]["name"] for article in articles}

print(get_sources_comprehension(sample_articles))
