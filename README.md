
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

```
dar--->the
akd--->and
waf--->have
aeh--->that
flq--->for
iou--->you
wid--->with
sea--->say
jiqse--->this
dai--->they
doq--->but
hase--->his
flm--->from
aeh--->that
nafd--->not
dks--->n't
she--->she
wod--->what
her--->their
kaux--->can
wou--->who
dps--->get
wud--->would
wher--->her
arl--->all
malk--->make
ado--->about
kew--->know
suil--->will
wup--->one
```

To see the list of all 5000 different chords you can use with Pyanist,
[see this CSV file](./docs/all_chords.csv).

## Attributions/sources

./word-freq-top5000.csv - https://raw.githubusercontent.com/filiph/english_words/master/data/word-freq-top5000.csv (MIT)



