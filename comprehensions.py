# cuadrado = []
# for x in [1, 2, 3, 4, 5]:
#     cuadrado.append(x**2)

# print(cuadrado)

# cuadrado = [x**2 for x in [1, 2, 3, 4, 5]]
# print(cuadrado)

sample_articles = [
    {
        "title": "Python logra nuevo exito",
        "source": {"name": "Tech News"},
        "publishedAt": "2024-06-01T10:00:00Z",
        "description": "Python se posiciona como el lenguaje de programacion mas popular del mundo.",
        "category": "Tecnologia",
    },
    {
        "title": "Economia global en recuperacion",
        "source": {"name": "Finance Daily"},
        "publishedAt": "2024-06-02T12:30:00Z",
        "description": "Los mercados muestran signos de recuperacion tras la crisis.",
        "category": "Economia",
    },
    {
        "title": "Nuevas tendencias en IA",
        "source": {"name": "AI Today"},
        "publishedAt": "2024-06-03T09:15:00Z",
        "description": "La inteligencia artificial sigue revolucionando diversas industrias.",
        "category": "Tecnologia",
    },
    {
        "title": "Salud mental",
        "source": {"name": "Wellness Weekly"},
        "publishedAt": "2024-06-04T14:45:00Z",
        "description": "Importancia de cuidar la salud mental en el entorno laboral.",
        "category": "Salud",
    },
]


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
