# source for most of the code: https://bootphon.github.io/phonemizer/python_examples.html

from phonemizer.backend import EspeakBackend
from phonemizer.punctuation import Punctuation
from phonemizer.separator import Separator

with open("./word-frequency-lists/word-freq-top5000.csv") as input_file:
    words = [line.split(",")[0] for line in input_file]

backend = EspeakBackend("en-us")
separator = Separator(phone=" ", word=None)
lexicon = {
    word: backend.phonemize([word], separator=separator, strip=True)[0].split()
    for word in words
}

spelling_rules = {
    "b": ["b"],
    "d": ["d"],
    "f": ["f"],
    "g": ["g"],
    "h": ["h"],
    "dʒ": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "r": ["r"],
    "s": ["s"],
    "t": ["t"],
    "v": ["v"],
    "w": ["w"],
    "z": ["z"],
    "ʒ": ["s"],
    "tʃ": ["ch"],
    "ʃ": ["sh"],
    "θ": ["th"],
    "ð": ["th"],
    "ŋ": ["ng"],
    "j": ["y"],
    "æ": ["a"],
    "eɪ": ["a"],
    "e": ["e"],
    "iː": ["e"],
    "ɪ": ["i"],
    "aɪ": ["i"],
    "ɒ": ["a"],
    "oʊ": ["o"],
    "ʊ": ["o"],
    "ʌ": ["u"],
    "uː": ["o"],
    "ɔɪ": ["oi"],
    "aʊ": ["ow"],
    "ə": ["a"],
    "eəʳ": ["air"],
    "ɑː": ["a"],
    "ɜːʳ": ["ir"],
    "ɔː": ["aw"],
    "ɪəʳ": ["ear"],
    "ʊəʳ": ["ure"],
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
    "aɪɚ": ["aer", "air"],
    "aɪə": ["aie"],
    "ʔ": [""],
    "n̩": ["n"],
    "ds": ["ds", "z"],
}

for word, phoneme_list in lexicon.items():
    new_spelling = [spelling_rules[phoneme][0] for phoneme in phoneme_list]

    print(word, "".join(new_spelling))
