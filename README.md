# haikugen

generate haikus with markov chains trained on books available from Project Gutenberg

## Example

```
1 - The Enchanted April, by Elizabeth Von Arnim
2 - Little Women, by Louisa M. Alcott
3 - A Room With A View, by E. M. Forster
4 - Moby-Dick; or The Whale, by Herman Melville
5 - The Blue Castle, by Lucy Maud Montgomery
6 - The Complete Works of William Shakespeare, by William Shakespeare
7 - Middlemarch, by George Eliot

pick a book by number
> 3

selected book: A Room With A View, by E. M. Forster
checking if model is already trained...
training model...
generating a haiku...

and the horse was stopped,
and Lucy suspected that
he had intended

g - generate another haiku
s - save haiku to file
b - pick a new book
e - exit
> g

generating a haiku...

you will like to do
under the afternoon clouds
that sailed in masses

g - generate another haiku
s - save haiku to file
b - pick a new book
e - exit
> s

saving haiku to saved_haikus.txt...

g - generate another haiku
s - save haiku to file
b - pick a new book
e - exit
> e

saving models...
bye
```



## Installation

```
git clone git@github.com:patrickarmengol/haikugen.git
cd haikugen
<do whatever virtual env stuff you want here>
pip install nltk markovify gutenberg-cleaner
```

launch python repl: `python`
```
> import nltk
> nltk.download('cmudict')
> exit()
```

## Usage

```
python haikugen.py
```