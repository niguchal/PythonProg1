import re
from collections import Counter

def analyze_text(filename):


  with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()


  text = re.sub(r'[^\w\s]', '', text).lower()
  words = text.split()


  word_count = len(words)
  char_count = len(text)


  word_counts = Counter(words)
  top_words = word_counts.most_common(10)


  print(f"Количество слов: {word_count}")
  print(f"Количество символов: {char_count}")
  print("\n10 наиболее часто встречающихся слов:")
  for word, count in top_words:
    print(f"{word}: {count}")


if __name__ == '__main__':
  filename = "text.txt"  # замените на имя вашего файла
  analyze_text(filename)
