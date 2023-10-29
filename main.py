from concurrent.futures import ThreadPoolExecutor
from sys import argv
from typing import Union


def get_count_word_in_file(word: str, file: str) -> Union[tuple[int, int], int]:
    """
    Returns in a tuple the line number and the character where the word in the text occurred
    :param word: word for find
    :param file: file where word must be
    :return: tuple(line, character) or -1 if word didn't find in file
    """
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            symbol: int = line.find(word)
            if symbol != -1:
                return i, symbol
    return -1


if __name__ == "__main__":
    word = argv[1]
    files = argv[2:]
    result = {}
    for file in files:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(get_count_word_in_file, word, file)
            if future.result() != -1:
                result[file] = future.result()
    if len(result) == 0:
        print(f'There is no files with word "{word}"')
    else:
        print(f'word "{word}" is in files: ')
        for key in result.keys():
            print(f'{key} - line {result[key][0]}, symbol {result[key][1]}')
