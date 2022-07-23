import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
file = response.text
soup = BeautifulSoup(file, 'html.parser')

films = [i.getText() for i in soup.find_all(name="h3", class_="title")]

reversed_films = films[::-1]


with open("movie.txt", "w") as file:
    for movie in reversed_films:
        file.write(f"{movie}\n")




