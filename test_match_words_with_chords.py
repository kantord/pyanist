import chord_generator
import chord_matcher
import os

with open(os.path.join("word-frequency-lists", "word-freq-top5000.csv")) as inputfile:
    raw_words = (
        line.strip().split(",")
        for line in inputfile
    )

    WORDS = [('tercanum', 1)] + [
        (word, int(raw_score))
        for word, raw_score in raw_words
    ][:100]

CHORDS = [
        (tuple(sorted((set("tgbyhn")))), 999),
] + list(chord_generator.generate_chords())

DICTIONARY = chord_matcher.match_chords_with_words(
    CHORDS, WORDS
)

def get_chord_score(chord):
    for chord_candidate, score in CHORDS:
        if chord == chord_candidate:
            return score

def get_chord_of_word(word_to_find):
    for chord, word_with_score in DICTIONARY.items():
        word, _ = word_with_score

        if word == word_to_find:
            return chord

def test_output_has_a_chord_a_word_and_a_score():
    word, _ = set(DICTIONARY.values()).pop()
    assert (word, 345) in DICTIONARY.values()

def test_output_includes_every_word_with_at_least_3_letters():
    words_to_include = set(word for word, _ in WORDS if len(word) >= 3)
    words_included = set(
        word for word, _ in DICTIONARY.values()
    )

    assert words_included == words_to_include

def test_that_all_keys_are_valid_chords():
    keys = set(DICTIONARY.keys())
    chords = set(chord for chord, _ in CHORDS)

    assert keys.difference(chords) == set()

def test_more_frequent_words_are_matched_with_better_chords():
    chord_of_frequent_word = get_chord_of_word("for")
    chord_of_infrequent_word = get_chord_of_word("first")

    assert (
        get_chord_score(chord_of_frequent_word) < get_chord_score(chord_of_infrequent_word)
    )


def test_chords_have_similar_keys_to_the_letters_of_the_word():
    assert get_chord_of_word("and") == tuple(sorted(set("and")))

