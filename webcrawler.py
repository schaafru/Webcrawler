import requests
import lxml
from bs4 import BeautifulSoup
import textwrap


def webcrawler(number_movies):
    url = "https://www.rottentomatoes.com/top/bestofrt/"

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    f = requests.get(url, headers=headers)

    movies_lst = []

    soup = BeautifulSoup(f.content, 'lxml')

    movies = soup.find('table', {
        'class': 'table'
      }).find_all('a')

    # print("movies: ", movies)

    count = 0

    if number_movies < 1 or number_movies > 100:
        print("\nPlease enter a number between 1 and 100")
        return

    if number_movies == 1:
        print("\nRotten Tomatoes Top Movie Of All Time:\n")
    else:
        print("\nRotten Tomatoes Top", number_movies, "Movies Of All Time:\n")

    for i in movies:
        while count < number_movies:
            urls = 'https://www.rottentomatoes.com' + i['href']
            movies_lst.append(urls)
            count += 1
            movie_url = urls
            movie_f = requests.get(movie_url, headers=headers)
            movie_soup = BeautifulSoup(movie_f.content, 'lxml')
            movie_content = movie_soup.find('div', {
              'class': 'movie_synopsis clamp clamp-6 js-clamp'
            })
            description = movie_content.string.strip()
            print(count, urls, '\n Title: ' + i.string.strip())
            print(' Description: ' + textwrap.fill(description, 160), "\n")


if __name__ == "__main__":

    print("Enter the number of top movies you want to view:")

    number_movies_to_view = int(input())
    webcrawler(number_movies_to_view)
