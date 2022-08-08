import string
IGNORE_SYMBOLS = string.whitespace + string.punctuation


def is_palindrome(text: str) -> bool:
    # Приводим к единому регистру
    text = text.lower()

    # Оставляем символы, что не входят в IGNORE_SYMBOLS
    text = ''.join(c for c in text if c not in IGNORE_SYMBOLS)

    # Пустая строка не палиндром
    if not text:
        return False

    return text == text[::-1]


something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
