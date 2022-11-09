import csv
import itertools
import json
import sys
import editdistance
from tqdm import tqdm

from chord_matcher import SPELLING_RULES, get_all_spellings

with open("./pyanist/dictionaries/english-us.json") as dictionary_file:
    dictionary = json.load(dictionary_file)

reverse_dictionary = {value: key for key, value in dictionary.items()}

with open("./pyanist/word-frequency-lists/word-freq-top5000.csv") as frequency_file:
    frequency_data = list(csv.reader(frequency_file))


csv_output = csv.DictWriter(sys.stdout, ["Importance rank", "Frequency rank", "Word", "Chord"])


def format_chord(chord, word):
    chord_variants = itertools.permutations(chord)
    all_spellings = get_all_spellings(word, SPELLING_RULES)

    variant_pairs = itertools.product(chord_variants, all_spellings)

    best_pair = min(variant_pairs, key=lambda pair: editdistance.eval(*pair))
    best_chord_variant, _ = best_pair

    return "".join(best_chord_variant)


all_words = enumerate(frequency_data)
most_important_words = sorted(
    all_words,
    key=lambda item: len(item[1][0]) * float(item[1][1]),
    reverse=True
)
csv_output.writeheader()

for importance_rank, word_data in tqdm(enumerate(most_important_words)):
    frequency_rank, frequency_datum = word_data
    word, _ = frequency_datum

    if word in reverse_dictionary:
        csv_output.writerow(
            {
                "Importance rank": importance_rank,
                "Frequency rank": frequency_rank,
                "Word": word,
                "Chord": format_chord(reverse_dictionary[word], word),
            }
        )
