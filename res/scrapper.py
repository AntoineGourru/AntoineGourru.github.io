import requests

API_KEY = 

url = "https://newsapi.org/v2/everything"

# Output file
output_file = "news_results.txt"


with open(output_file, "w+", encoding="utf-8") as f:
    start_day = 1
    end_day = 29    # or however many days you want

    for day in range(start_day, end_day):
        day_from = str(day).zfill(2)          # "01", "02", ..., "09", "10", ...
        day_to   = str(day + 1).zfill(2)

        page = 1
        total_count = 0

        while True:
            params = {
                "q": "intelligence artificielle", #"intelligence artificielle OR IA",  # your theme
                "language": "fr",
                "pageSize": 100,                   # max per page
                "sortBy": "publishedAt", 
                "apiKey": API_KEY,
                "from": f"2026-01-{day_from}", #Changer ici la date
                "to": f"2026-01-{day_to}",
                "page": page                       # <-- pagination here
            }

            response = requests.get(url, params=params).json()
            articles = response.get("articles", [])

            # Stop if no articles on this page
            if not articles:
                break

            # Save each article
            for article in articles:
                titre = article.get("title")
                resume = article.get("description")
                source = article.get("source", {}).get("name")
                date = article.get("publishedAt")
                

                f.write(f"[{source}] {titre}\n")
                f.write(f"{resume}\n")
                f.write(f"{date}\n")
                f.write("---\n\n")

                total_count += 1
                #print("written:", titre)

            page += 1
            print(page)

        print(f"Done. Total articles saved: {total_count}")

