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


csv_output = csv.DictWriter(sys.stdout, ["#", "word", "chord"])


def format_chord(chord, word):
    chord_variants = itertools.permutations(chord)
    all_spellings = get_all_spellings(word, SPELLING_RULES)

    variant_pairs = itertools.product(chord_variants, all_spellings)

    best_pair = min(variant_pairs, key=lambda pair: editdistance.eval(*pair))
    best_chord_variant, _ = best_pair

    return "".join(best_chord_variant)


csv_output.writeheader()

for number, frequency_datum in tqdm(list(enumerate(frequency_data))):
    word, _ = frequency_datum

    if word in reverse_dictionary:
        csv_output.writerow(
            {
                "#": number,
                "word": word,
                "chord": format_chord(reverse_dictionary[word], word),
            }
        )
