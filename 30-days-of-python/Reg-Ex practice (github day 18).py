import re
text = """
Contact List & Logs:
- Alice Smith: alice.smith@example.com, +1-555-0192, 1024 Elm St. (Zip: 90210)
- Bob Jones: b_jones1984@work-place.org, 555.839.2019, 44 Oak Ave. (Zip: 10001)
- Charlie: charlie@domain.co.uk, 5550183829, 89 Pine Rd.

Log entries on 2026-06-15:
[INFO] User login from IP 192.168.1.50
[ERROR] Failed connection attempt by 10.0.0.99 at 14:32:05
[WARNING] Low disk space on server-01 (ID: 404)
"""
# email_pattern = r"[a-zA-Z._0-9]+@[a-zA-Z-]+.[a-zA-Z.]+"
# matches = re.finditer(email_pattern, text)
# for match in matches:
#      print(f"Email: {match}")

# name_pattern = r"(?<=- )[A-Z][a-z]+(\s([A-Z][a-z])*)?"
# matches = re.finditer(name_pattern, text)
# for match in matches:
#     print(f"Name: {match}")


# Level 1
# Ex 1

# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


def most_frequent_word(string):
    pattern = re.compile(r"\b\w+\b", re.IGNORECASE)
    all_words = pattern.findall(paragraph)
    word_count = {}
    for word in all_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted([(count, word)
                          for word, count in word_count.items()], reverse=True)
    return sorted_words


print(most_frequent_word(paragraph))

# Ex 2
