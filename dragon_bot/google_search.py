import requests

# Твій API-ключ і пошуковий ідентифікатор (замінити на свої)
# <script async src="https://cse.google.com/cse.js?cx=95bfc722ce68e407a">
# </script>
# <div class="gcse-search"></div>
# 116.16.251.38
# 70.36.61.17

API_KEY = "AIzaSyA4AuRPZEGlZ3hg1naGEfPT43BJgDnIRak"
CSE_ID = "95bfc722ce68e407a"


def search_google(query):
    """Виконує пошук у Google і повертає результати."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": API_KEY,
        "cx": CSE_ID,
        "num": 3,  # Кількість результатів
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for item in data.get("items", []):
        results.append(f"{item['title']} - {item['link']}")

    return results if results else ["Нічого не знайдено."]


def save_query(query, results):
    """Зберігає запити в файл."""
    with open("data/search_history.txt", "a", encoding="utf-8") as file:
        file.write(f"🔍 Запит: {query}\n")
        for res in results:
            file.write(f"   {res}\n")
        file.write("\n")


if __name__ == "__main__":
    query = input("Що ви хочете знайти? ")
    results = search_google(query)

    save_query(query, results)  # Записуємо запит у файл
