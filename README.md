
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

| Chord | Word      |
|-------|-----------|
| dar   | the       |
| akd   | and       |
| waf   | have      |
| aeh   | that      |
| wid   | with      |
| flq   | for       |
| iou   | you       |
| jiqse | this      |
| dai   | they      |
| aeh   | that      |
| flm   | from      |
| sea   | say       |
| her   | their     |
| hase  | his       |
| doq   | but       |
| nafd  | not       |
| dks   | n't       |
| wod   | what      |
| wud   | would     |
| she   | she       |
| ado   | about     |
| epl   | people    |
| dlr   | there     |
| flk   | think     |
| kew   | know      |
| oic   | which     |
| malk  | make      |
| suil  | will      |
| lkud  | could     |
| jir   | year      |
| klz   | because   |
| kaux  | can       |
| dsm   | time      |
| wou   | who       |
| dps   | get       |
| wher  | her       |
| udirw | other     |
| uek   | when      |
| dlm   | them      |
| josfd | just      |
| seo   | some      |
| ald   | take      |
| arl   | all       |
| dko   | into      |
| jor   | your      |
| dys   | these     |
| klm   | come      |
| fkou  | through   |
| dakj  | than      |
| fdlsz | first     |
| wup   | one       |
| smf   | something |
| livx  | like      |
| dkl   | then      |
| msr   | more      |
| wdk   | want      |
| owfd  | out       |
| dwm   | him       |

To see the list of all 5000 different chords you can use with Pyanist,
[see this CSV file](./docs/all_chords.csv).

## Learning Pyanist

There is a course designed to learn the most useful chords in Pyanist.
This course teaches the top *100* words, and is split into 10 lessons.

You will probably need to practice each lesson multiple times on
different days before the chords are committed to your
muscle memory.

In order to practice the lessons, you can simply open the text files
and manually copy them by typing and chording them into a text
editor. Alternatively, you can use [Monkeytype](https://monkeytype.com/),
which will also measure your performance. Monkeytype allows you
to practice a custom file, which is the feature you will need to
use in order to practice these lessons.

The lessons available:

* [Lesson 1](docs/lesson_1.txt) - the and have with for you this they from say
* [Lesson 2](docs/lesson_2.txt) - their his but not what would she about people there
* [Lesson 3](docs/lesson_3.txt) - think know which make will could year because can time
* [Lesson 4](docs/lesson_4.txt) - who get her other when them just some take all
* [Lesson 5](docs/lesson_5.txt) - into your these come through than first one something like
* [Lesson 6](docs/lesson_6.txt) - then more want out him thing see look government those
* [Lesson 7](docs/lesson_7.txt) - should also between school now student American woman another more
* [Lesson 8](docs/lesson_8.txt) - child there here well its how find really our very
* [Lesson 9](docs/lesson_9.txt) - country after become tell many give question two problem only
* [Lesson 10](docs/lesson_10.txt) - world still back different family even against company good way

## Attributions/sources

./word-freq-top5000.csv - https://raw.githubusercontent.com/filiph/english_words/master/data/word-freq-top5000.csv (MIT)



