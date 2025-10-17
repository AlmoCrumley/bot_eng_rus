from sqlalchemy.orm import sessionmaker


from db_bot.models import User, Word, UserVocabulary, engine

Session = sessionmaker(bind=engine)

session = Session()

def new_user(user_id):
    users = session.query(User).all()
    if user_id in [user.telegram_id for user in users]:
        print('Пользователь уже существует')
    else:
        user = User(telegram_id=user_id)
        session.add(user)
        session.commit()

def get_word(word):
    word = session.query(Word).filter_by(english=word).one_or_none()
    return word

def get_vocabulary(telegram_id):
    existing_vocab = session.query(UserVocabulary).filter_by(
        user_id=telegram_id
    )
    if existing_vocab:
        words_id = [vocab.word_id for vocab in session.query(UserVocabulary).filter_by(user_id=telegram_id)]
        words = [session.query(Word).filter_by(id=word_id).one_or_none() for word_id in words_id]
        return [f'{word.english} -- {word.russian}' for word in words]
    else:
        return "Словарь пуст"

def add_word_to_the_vocabulary(word, user):
    print(word, user)
    user_vocabs = session.query(UserVocabulary).all()
    if user in [vocab.user_id for vocab in user_vocabs]:
        # Проверяем, есть ли уже такое слово у пользователя
        existing_vocab = session.query(UserVocabulary).filter_by(
            user_id=user,
            word_id=word.id
        ).one_or_none()
        if existing_vocab:
            return "Слово уже есть"
        else:
            vocab = UserVocabulary(user_id=user, word_id=word.id)
            session.add(vocab)
            session.commit()
            length_of_vocab = len([vocab.word_id for vocab in session.query(UserVocabulary).filter_by(user_id=user)])
            return f"Слово добавлено. Сохранено: {length_of_vocab} слов(а)"
    else:
        vocab = UserVocabulary(user_id=user, word_id=word.id)
        session.add(vocab)
        session.commit()
        return "Слово добавлено"
