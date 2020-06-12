import sys
import requests
import json

url = 'https://api.themoviedb.org/3/movie/top_rated/' 
api_key = '7bfeda2276dd8eac6859724170d2ace6'
params = {
    'api_key': api_key,
}
results = requests.get(url, params=params).json()["results"]
# print(results)
jsondata = []
for result in results:
    temp = {}
    temp['model'] = 'articles.movie'
    temp['id'] = result.pop('id')
    field = {}
    modelfield = ['title', 'original_title', 'release_date', 'popularity', 'vote_count', 'vote_average', 'adult', 'overview', 'original_language', 'poster_path', 'backdrop_path','genres']
    for key, value in result.items():
        if key in modelfield:
            field[key] = value
    # print(field)
        temp['fields'] = field
    # print()
    jsondata.append(temp)
# print(jsondata)

with open('moviedata.json', 'w', encoding="UTF-8") as make_file:
    json.dump(jsondata, make_file, indent="\t")


