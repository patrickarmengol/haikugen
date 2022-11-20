import markovify
import logging
from gutenberg_cleaner import super_cleaner
from string import punctuation
from syllablecount import count_syllables

logging.basicConfig(level=logging.CRITICAL)


def train_model(book_path):
    with open(book_path) as f:
        text = f.read()

    cleaned_text = super_cleaner(text)
    cleaned_text = cleaned_text.replace('—', ' ')

    text_model = markovify.Text(cleaned_text)

    return text_model


def tokenize(text):
    return text.split()


def detect_haiku(text):
    words = tokenize(text)
    line_flags = (5, 7, 5)
    lines = [[], [], []]
    li = 0
    sc = 0
    cur_phrase = []

    for word in words:
        if li > 2:
            logging.debug('too many words; not a haiku')
            return None
        cur_phrase.append(word)
        word = word.lower().strip(punctuation)
        if word.endswith('\'s'):
            word = word[:-2]
        sc += count_syllables(word)
        if sc == line_flags[li]:
            lines[li] = cur_phrase
            cur_phrase = []
            sc = 0
            li += 1
        elif sc > line_flags[li]:
            logging.debug(
                'syllables don\'t match up to line breaks; not a haiku')
            return None
    if not all(lines):
        logging.debug('not enough words; not a haiku')
        return None

    haiku = '\n'.join([' '.join(line) for line in lines])
    return haiku


def generate_haiku(model):
    tries = 0
    while True:
        tries += 1
        logging.debug(f'try {tries}')
        sentence = model.make_short_sentence(
            max_chars=90, min_chars=60, tries=100)
        if not sentence:
            logging.debug('sentence failed to generate from model')
            continue
        logging.debug('sentence: ' + sentence)
        haiku = detect_haiku(sentence)
        if haiku:
            return haiku


def main():
    # TODO: automatically generate this based on books included in books dir
    books = [
        ('Moby-Dick; or The Whale, by Herman Melville', 'books/2701-0.txt'),
        ('The Complete Works of William Shakespeare, by William Shakespeare',
         'books/pg100.txt'),
        ('Middlemarch, by George Eliot', 'books/pg145.txt'),
        ('A Room With A View, by E. M. Forster', 'books/pg2641.txt'),
        ('The Enchanted April, by Elizabeth Von Arnim', 'books/pg16389.txt'),
        ('Little Women, by Louisa M. Alcott', 'books/pg37106.txt'),
        ('The Blue Castle, by Lucy Maud Montgomery', 'books/pg67979.txt')
    ]

    # TODO: save models to disk to avoid retraining
    model_dict = {}

    user_command = 'b'

    while user_command != 'e':
        if user_command == 'b':
            print()
            for i, (book_name, book_path) in enumerate(books):
                print(f'{i} - {book_name}')

            user_book_index = input(
                '\npick a book by number\n> ')
            while not user_book_index.isnumeric() or int(user_book_index) >= len(books):
                user_book_index = input('please pick a book by number\n> ')
            user_book_index = int(user_book_index)

            user_book_name, user_book_path = books[user_book_index]
            print(f'\nselected book: {user_book_name}')

            print('checking if model is already trained...')
            model = model_dict.get(user_book_name)

            if not model:
                print('training model...')
                model = train_model(user_book_path)
                model_dict[user_book_name] = model

            print('generating a haiku...')
            haiku = generate_haiku(model)
            print()
            print(haiku)

        elif user_command == 'g':
            print('generating a haiku...')
            haiku = generate_haiku(model)
            print()
            print(haiku)

        # TODO: save haikus to file

        else:
            print('unknown command')

        # get next command
        user_command = input(
            """
g - generate another haiku
b - pick a new book
e - exit
> """)

    print('bye')


if __name__ == '__main__':
    main()
