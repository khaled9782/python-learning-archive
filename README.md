# Python Learning Archive

A personal archive of exercises, mini-projects, and practice scripts written while learning Python. This repository isn't a polished project — it's a record of the process: working through books, following tutorials, and experimenting on my own.

## About This Archive

Everything here was written while learning core Python fundamentals — variables, control flow, functions, data structures, file handling, OOP, decorators, and more. It's organized by source so it's easy to trace which exercises came from which book or tutorial, and to see how the material built on itself over time.

Nothing in here is meant to be production-quality code. Expect rough edges, inconsistent style, and the occasional leftover debugging line — that's part of the point.

## Sources

This archive draws from three main sources, plus a folder of self-directed practice:

| Source | Description | Folder |
|---|---|---|
| **Python Crash Course** by Eric Matthes | Exercises from the book, covering lists, dictionaries, conditionals, functions, classes, and more | [`01-python-crash-course/`](./01-python-crash-course) |
| **Automate the Boring Stuff with Python** by Al Sweigart | Practical, project-based exercises focused on automation | [`02-automate-the-boring-stuff/`](./02-automate-the-boring-stuff) |
| **30 Days of Python** (GitHub tutorial repository) | Daily practice scripts following a structured 30-day curriculum | [`03-30-days-of-python/`](./03-30-days-of-python) |
| Self-directed practice | Exercises and mini-scripts written outside of any specific course, for extra reinforcement | [`04-general-practice/`](./04-general-practice) |

## Repository Structure

```
python-learning-archive/
├── README.md
├── .gitignore
├── 01-python-crash-course/          # Exercises from Python Crash Course
├── 02-automate-the-boring-stuff/    # Exercises from Automate the Boring Stuff
├── 03-30-days-of-python/            # Daily practice from the 30 Days of Python tutorial
├── 04-general-practice/             # Independent practice scripts and small experiments
└── data/                            # Supporting files (text/data) used by scripts above
```

Each source folder contains standalone `.py` files. File names have generally been kept close to their original naming so they're still recognizable against my own notes and the source material (e.g. `Ex 6.1 - 6.3 (dictionaries).py`, `web scraping (git day 22).py`).

## Why This Exists

I wanted a single place to keep the exercises I worked through while learning Python, rather than leaving them scattered across a local folder. Publishing it here serves a few purposes:

- **A personal record of progress** — a way to look back and see how my understanding of the language evolved.
- **Proof of consistent practice** — evidence of time spent learning, exercise by exercise.
- **A reference** — a searchable archive I can return to if I forget how I solved a particular problem the first time around.

## Notes

- These files were written at different points during the learning process, so code style and conventions are not consistent across the archive — later files generally reflect more comfort with the language than earlier ones.
- Some scripts depend on files in the `data/` folder (e.g. reading from a text file); those dependencies are kept alongside the scripts that use them.

## License

This repository is for personal/educational purposes. Exercise prompts and problem descriptions belong to their respective authors (Eric Matthes, Al Sweigart, and the 30 Days of Python tutorial maintainers); the code implementations are my own.
