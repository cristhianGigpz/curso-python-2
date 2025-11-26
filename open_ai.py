import os
from dotenv import load_dotenv
from openai import OpenAI

from sample_data import sample_articles

load_dotenv()

def analyze_news_with_ia(articles: list[dict], query:str) -> str | None:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    context = "\n\n".join(
        [
            f"Title: {article['title']}\nContent: {article['description']}"
            for article in articles
        ]
    )

    prompt = (
        "Eres un asistente de IA que ayuda a analizar noticias. "
        "Usa el siguiente contexto para responder a las preguntas del usuario:\n\n"
        f"{context}\n\n"
        f"Pregunta: {query}\n\n"
        f"Respuesta:"
    )

    print(prompt)

    reponse = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7,
        max_tokens=500,
    )

    return reponse.choices[0].message.content if reponse.choices else None

result = analyze_news_with_ia(
    sample_articles,
    "Resumir cada uno de los temas tratados y explicalos en un parrafo corto. cada uno",
)

print(result)

