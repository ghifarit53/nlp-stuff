#
# merge_phrase.py
# author  : Muhammad Ghifari Taqiuddin
# created : Tuesday, 02 May 2023 at 08:45
#
import re


def create_phrase_list(filepath: str):
    # create phrase list from file
    file = open(filepath, "r")
    phrase_list = []

    for line in file:
        phrase_list.append(line.strip().lower())

    return phrase_list


def merge_phrase(text, phrase_list: list):
    # preprocessing
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.split()

    result = text.copy()

    # window sliding algorithm
    # win_size is from longest (the whole text) to shortest (2 words),
    # to make sure longer phrase that has the same sub-phrase handled first
    for win_size in range(len(text), 1, -1):
        for i in range(len(result) - win_size + 1):
            phrase = result[i:i + win_size]
            joined = " ".join(phrase)

            if joined in phrase_list:
                result[i:i + win_size] = [joined.replace(" ", "")]
            else:
                continue

    return " ".join(result)


def main():
    # create list of phrases from frase.txt
    phrase_list = create_phrase_list("./frase.txt")

    # some example text that contains few phrases from the file
    example_text = [
        "Terima kasih atas pertanyaannya",
        "Buang air besar berlebihan mungkin disebabkan berbagai faktor.",
        "Jaga pola makan dan olahraga untuk mencapai berat badan ideal",
    ]

    for text in example_text:
        print(merge_phrase(text, phrase_list))


if __name__ == "__main__":
    main()
