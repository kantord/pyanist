import functools
import itertools
import json
import sys
import os
from tqdm import tqdm

from phonemizer.backend import EspeakBackend
from phonemizer.punctuation import Punctuation
from phonemizer.separator import Separator
from frozendict import frozendict

import chord_generator

backend = EspeakBackend("en-us")
separator = Separator(phone=" ", word=None)
SPELLING_RULES = frozendict(
    {
        key: tuple(value)
        for key, value in {
            "b": ["b"],
            "d": ["d", "ed"],
            "f": ["f", "ph", "lf", "ft"],
            "g": ["g", "gu", "gh"],
            "h": ["h", "wh"],
            "dʒ": [
                "j",
                "g",
                "je",
            ],
            "k": ["k", "c", "ch", "x", "lk"],
            "l": ["l"],
            "m": [
                "m",
            ],
            "n": ["n", "kn", "gn", "pn"],
            "p": ["p"],
            "r": ["r", "rh"],
            "s": ["s", "c", "ce", "se"],
            "t": ["t", "ed"],
            "v": ["v", "f", "ve"],
            "w": ["w", "wh", "u", "o"],
            "z": ["z", "s", "x", "se", "ze"],
            "ʒ": ["s", "z", "si"],
            "tʃ": ["ch"],
            "ʃ": ["sh", "s"],
            "θ": ["th", "f", "t"],
            "ð": ["th", "d"],
            "ŋ": [
                "ng",
                "n",
            ],
            "j": ["y", "i", "j"],
            "æ": ["a", "ai", "au"],
            "eɪ": ["a", "ai", "ey"],
            "e": ["e", "ea", "ai", "a"],
            "iː": ["e", "y", "i"],
            "ɪ": ["i", "e", "y"],
            "aɪ": [
                "i",
                "y",
            ],
            "ɒ": ["a", "aw"],
            "oʊ": ["o", "ew"],
            "ʊ": [
                "o",
                "u",
            ],
            "ʌ": [
                "u",
                "o",
            ],
            "uː": ["o", "ou"],
            "ɔɪ": ["oi", "oy", "uoy"],
            "aʊ": ["ow", "ou"],
            "ə": [
                "a",
                "er",
                "i",
                "ar",
            ],
            "eəʳ": [
                "er",
                "are",
                "ear",
            ],
            "ɑː": [
                "a",
            ],
            "ɜːʳ": ["ir", "er", "ur", "ear", "or", "yr"],
            "ɔː": ["aw", "a", "or", "ar", "au"],
            "ɪəʳ": ["ear", "ier"],
            "ʊəʳ": ["ure", "our"],
            "ɔːɹ": ["or"],
            "ɔ": ["o"],
            "ɹ": ["r"],
            "ɛ": ["e"],
            "ɡ": ["g"],
            "ɛɹ": ["er"],
            "ɜː": ["er"],
            "ɐ": ["a"],
            "ɪ": ["i"],
            "ɪɹ": ["ir"],
            "əl": ["l"],
            "ʊɹ": ["or"],
            "ɚ": ["er", "ir"],
            "oːɹ": ["or"],
            "i": ["i", "y"],
            "ᵻ": ["e"],
            "iə": ["ie"],
            "ɑːɹ": ["ar"],
            "ɾ": ["t", "r"],
            "oː": ["o"],
            "aɪɚ": ["aer", "air", "er"],
            "aɪə": ["aie"],
            "ʔ": [""],
            "n̩": ["n"],
            "ds": ["ds", "z"],
        }.items()
    }
)


@functools.cache
def get_all_spellings(word, spelling_rules):
    def generate_spellings():
        phonemes = backend.phonemize([word], separator=separator, strip=True)[0].split()
        list_of_grapheme_options = [spelling_rules[phoneme] for phoneme in phonemes]

        return itertools.product(*list_of_grapheme_options)

    return list("".join(spelling) for spelling in generate_spellings())


def get_chord_score(word, chord):
    """
    Quantify how good of a match a chord is for a word
    """
    letters = set(word)
    keys_of_chord = set(chord[0])
    keys_not_in_word = keys_of_chord - letters
    keys_in_word = keys_of_chord & letters

    return (len(keys_not_in_word) - len(keys_in_word) * 2) / chord[1]


def get_best_remaning_chord(word, chords):
    best_chord = min(
        chords,
        key=lambda chord: min(
            get_chord_score(spelling, chord)
            for spelling in get_all_spellings(word, SPELLING_RULES)
        ),
    )

    chords.remove(best_chord)

    return best_chord[0]


def match_chords_with_words(chords, words):
    chords = list(chords)

    return {
        get_best_remaning_chord(word, chords): (word, 345)
        for word, _ in tqdm(sorted(words, key=lambda item: -item[1] / len(item[0])))
        if len(word) >= 3
    }


def main():
    language, wordsfile = sys.argv[1:]
    dictionary_file = os.path.join("dictionaries", f"{language}.json")

    with open(os.path.join("word-frequency-lists", wordsfile)) as inputfile:
        raw_words = (line.strip().split(",") for line in inputfile)

        words = [(word, int(raw_score)) for word, raw_score in raw_words]

    dictionary = match_chords_with_words(chord_generator.generate_chords(), words)

    with open(dictionary_file, "w") as outputfile:
        json.dump(
            {"".join(key): value[0] for key, value in dictionary.items()}, outputfile
        )


if __name__ == "__main__":
    main()
