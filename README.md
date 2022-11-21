# haikugen

generate haikus with markov chains trained on books available from Project Gutenberg

## Example

```
0 - Moby-Dick; or The Whale, by Herman Melville
1 - The Complete Works of William Shakespeare, by William Shakespeare
2 - Middlemarch, by George Eliot
3 - A Room With A View, by E. M. Forster
4 - The Enchanted April, by Elizabeth Von Arnim
5 - Little Women, by Louisa M. Alcott
6 - The Blue Castle, by Lucy Maud Montgomery

pick a book by number
> 2

selected book: Middlemarch, by George Eliot
checking if model is already trained...
training model...
generating a haiku...

When he was to have
the advantage over him,
I think his own hands.

g - generate another haiku
b - pick a new book
s - save haiku to file
e - exit
> g

generating a haiku...

You will like to do
under the afternoon clouds
that sailed in masses.

g - generate another haiku
b - pick a new book
s - save haiku to file
e - exit
> e

saving models...
bye
```

## Installation

```
git clone git@github.com:patrickarmengol/haikugen.git
<do whatever virtual env stuff you want here>
pip install nltk markovify gutenberg-cleaner
```

launch python repl
```
> import nltk
> nltk.download('cmudict')
```

## Usage

```
python haikugen.py
```