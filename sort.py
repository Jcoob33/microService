import json

# Read the sorting preference from the text file
with open('sorting_preference.txt', 'r') as preference_file:
    sorting_preference = preference_file.read().strip().lower()

# Open the file with article information in read mode
with open('times_api.json', 'r') as file:
    # Load the JSON data
    data = json.load(file)

# Get the list of articles from the "results" key
articles = data['results']

# Sort the articles based on the sorting preference
if sorting_preference == 'name':
    sorted_articles = sorted(articles, key=lambda article: article['title'])
elif sorting_preference == 'date':
    sorted_articles = sorted(articles, key=lambda article: article['published_date'])
else:
    raise ValueError('Invalid sorting preference. Please specify either "name" or "date".')

# Create a list of dictionaries for the ordered articles
ordered_articles = []
for index, article in enumerate(sorted_articles):
    ordered_articles.append({
        'index': index + 1,
        'title': article['title'],
        'url': article['url'],
        'published_date': article['published_date']
    })

# Write the ordered articles to a JSON file
with open('sorted_articles.json', 'w') as file:
    json.dump(ordered_articles, file, indent=4)