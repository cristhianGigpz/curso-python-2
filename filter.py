from sample_data import sample_articles

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []
for number in numbers:
    if number % 2 == 0:
        pairs.append(number)

print(pairs)

# pairs = [number for number in numbers if number % 2 == 0]
# print(pairs)

# def is_pair(n: int) -> bool:
#     if n % 2 == 0:
#         return True
#     return False

# pairs_filtered = list(filter(is_pair, numbers))
# print(pairs_filtered)

pairs_filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(pairs_filtered)
for pair in pairs_filtered:
    print(f"Filtered even number: {pair}")


def get_articles_by_source(articles: list[dict], source_name: str) -> list[dict]:
    return list(
        filter(lambda article: article["source"]["name"] == source_name, articles)
    )

filtered_articles = get_articles_by_source(sample_articles, "Tech News")
for article in filtered_articles:
    print(f"Article from Tech News: {article['title']}")