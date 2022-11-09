
<h1 align="center">
<img src="logo.png" alt="Pyanist" width="300" />
</h1>


Pyanist is a tool that allows chorded typing using a regular N-key rollover keyboard.
It allows you to use chorded typing in addition to normal typing, which means that you can
get started by chording a few frequent words instead of having to learn a whole system 
from scratch.

## Installing Pyanist

To install Pyanist, you need to have `pip`, or another Python package manager
installed on your computer. If you have `pip` installed simply run:

**Linux**

```bash
sudo pip install pyanist
```

**OS X/Windows**

```bash
pip install pyanist
```

After that you should be ready to run Pyanist.

**Note**: Pyanist has only been tested on _Linux_, albeit it should run also on OS X and Windows.


## Running Pyanist

After you've installed Pyanist, you can run in using the command:

**Linux**

```bash
sudo pyanist
```

**OS X/Windows**

```bash
pyanist
```

## Using Pyanist

While Pyanist is running, you can type words using chords. Chording means,
that you press multiple letters at the same time. For example, you can press
the letters `iou` at the same time in order to type the word `you` with
a single keystroke.

Whenever you type a chord and a matching word is found, Pyanist will
write that word for you. If no matching word is found, your chord will
have no effect.

The chords used to type some of the most common English words:

| Importance rank | Frequency rank | Word    | Chord |
|-----------------|----------------|---------|-------|
| 0               | 0              | the     | dar   |
| 1               | 2              | and     | akd   |
| 4               | 7              | have    | waf   |
| 6               | 11             | that    | aeh   |
| 8               | 15             | with    | wid   |
| 10              | 12             | for     | flq   |
| 11              | 13             | you     | iou   |
| 14              | 19             | this    | jiqse |
| 15              | 20             | they    | dai   |
| 16              | 26             | that    | aeh   |
| 17              | 25             | from    | flm   |
| 19              | 18             | say     | sea   |
| 20              | 35             | their   | her   |
| 21              | 24             | his     | hase  |
| 22              | 22             | but     | doq   |
| 25              | 27             | not     | nafd  |
| 26              | 28             | n't     | dks   |
| 27              | 33             | what    | wod   |
| 28              | 40             | would   | wud   |
| 29              | 30             | she     | she   |
| 30              | 45             | about   | ado   |
| 31              | 61             | people  | epl   |
| 33              | 52             | there   | dlr   |
| 34              | 55             | think   | flk   |
| 36              | 46             | know    | kew   |
| 38              | 57             | which   | oic   |
| 39              | 44             | make    | malk  |
| 40              | 47             | will    | suil  |
| 41              | 70             | could   | lkud  |
| 42              | 53             | year    | jir   |
| 43              | 88             | because | klz   |
| 44              | 36             | can     | kaux  |
| 45              | 51             | time    | dsm   |
| 46              | 37             | who     | wou   |
| 48              | 38             | get     | dps   |
| 49              | 41             | her     | wher  |
| 51              | 74             | other   | udirw |
| 52              | 56             | when    | uek   |
| 53              | 58             | them    | dlm   |
| 54              | 65             | just    | josfd |
| 55              | 59             | some    | seo   |

To see the list of all 5000 different chords you can use with Pyanist,
[see this CSV file](./docs/all_chords.csv).

## Attributions/sources

./word-freq-top5000.csv - https://raw.githubusercontent.com/filiph/english_words/master/data/word-freq-top5000.csv (MIT)



