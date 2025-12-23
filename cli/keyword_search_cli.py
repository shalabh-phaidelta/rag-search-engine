import argparse
import string
import json
from utils.helper import read_stop_words, remove_stop_words_from, stem_words

import os
print(os.getcwd())

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Avaialable commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")
    args = parser.parse_args()
    found = []
    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            movies = load_movies_from_json_file("data/movies.json")
            found = find_movies_by_keyword(args.query, movies)
        case _:
            parser.print_help()
    res_count = 0 
    for m in found:
        res_count += 1
        if res_count > 5:
            break
        print(f"{m['id']}. {m['title']}")
    

def find_movies_by_keyword(query: str, movies: dict) -> list:
    #movies:dict = load_movies_from_json_file("data/movies.json")
    result = []
    translator = str.maketrans('', '', string.punctuation)
    query = query.translate(translator).lower()
    query_tokens = query.split()
    query_tokens = remove_stop_words_from(query_tokens)
    query_tokens = stem_words(query_tokens)
    # print(help(stem_words))
    for k, v in movies.items():
        if "movies" == k:
            all_movies: dict = movies["movies"]
            for movie in all_movies:
                title_tokens = movie["title"].translate(translator).lower().split()
                title_tokens = remove_stop_words_from(title_tokens)
                title_tokens = stem_words(title_tokens)
                # if query.lower() in movie["title"].translate(translator).lower():
                # if set(query_tokens) & set(title_tokens):
                for qt in query_tokens:
                    for tt in title_tokens:
                        if qt in tt:
                            found_movie = {"id": movie["id"], "title":movie["title"]}
                            # print(f"{query_tokens} {tt}")
                            if found_movie not in result:
                                result.append(found_movie)
                
    return result

def load_movies_from_json_file(path: str) -> dict:
    try:
        with open(path, 'r') as file:
            movies:dict = json.load(file)
        return movies
    except FileNotFoundError:
        print(f"Error: The file {path} was not found")
    except json.JSONDecodeError:
        print(f"Error: Could not decode json from the file")


if __name__ == "__main__":
    main()

    
