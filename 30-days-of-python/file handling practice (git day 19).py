import json
# with open("read_file_example.txt", "r") as f:
#     for line in f:
#         print(line, end="")

# Ex 1
# def line_and_word_counter(file_path):

#     with open(file_path) as text_file:
#         # (line counter code)
#         line_count = 0
#         for line in text_file:
#             line_count += 1
#         print(f"there are {line_count} lines in this file")

#         # (reset the pointer of te file to the beginning)
#         text_file.seek(0)

#         # (word counter code)
#         word_count = len(text_file.read().split())
#         print(f"the total number of words in this text file is {word_count}")


# line_and_word_counter(r"data\donald_trump_speech.txt")

# # Ex 2
# def most_spoken_languages(file, limit):
#     with open(file, encoding='utf-8') as data:
#         countries = json.load(data)

#         lang_count = {}
#         for country in countries:
#             for lang in country['languages']:
#                 if lang in lang_count:
#                     lang_count[lang] += 1
#                 else:
#                     lang_count[lang] = 1
#     sorted_list = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
#     return sorted_list[:limit]


# result = most_spoken_languages(r"data\countries_data.json", 5)
# for language, count in result:
#     print(f"{language}: {count}")


# # Ex 3
# def most_populated_countries(file, limit):
#     with open(file, encoding='utf-8') as data:
#         countries = json.load(data)
#         sorted_countries = sorted(
#             countries, key=lambda x: x["population"], reverse=True)

#         top_countries = []
#         for country in sorted_countries[:limit]:
#             top_countries.append(
#                 {"country": country["name"], "population": country["population"]})
#         return top_countries


# result = most_populated_countries("./data/countries_data.json", 10)
# print(json.dumps(result, ind))
