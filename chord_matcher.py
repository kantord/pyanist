import json
import sys
import os
import chord_generator

def get_chord_score(word, chord):
    letters = set(word)
    keys_of_chord = set(chord[0])
    keys_not_in_word = keys_of_chord - letters
    keys_in_word = keys_of_chord & letters

    return (len(keys_not_in_word) - len(keys_in_word)) / chord[1]

def get_best_remaning_chord(word, chords):
    best_chord = min(
            chords, key=lambda chord: get_chord_score(word, chord)
    )

    chords.remove(best_chord)

    return best_chord[0]

def match_chords_with_words(chords, words):
    chords = list(chords)

    return {
        get_best_remaning_chord(word, chords): (word, 345)
        for word, _
        in sorted(words, key=lambda item: -item[1])
        if len(word) >= 3
    }

def main():
    language, wordsfile = sys.argv[1:]
    dictionary_file = os.path.join("dictionaries", f"{language}.json")

    with open(os.path.join("word-frequency-lists", wordsfile)) as inputfile:
        raw_words = (
            line.strip().split(",")
            for line in inputfile
        )

        words = [
            (word, int(raw_score))
            for word, raw_score in raw_words
        ]

    dictionary = match_chords_with_words(
        chord_generator.generate_chords(),
        words
    )

    with open(dictionary_file, "w") as outputfile:
        json.dump({
            "".join(key): value[0]
            for key, value in dictionary.items()
        }, outputfile)

if __name__ == "__main__":
    main()
