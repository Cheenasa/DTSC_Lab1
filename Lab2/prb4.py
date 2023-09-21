from collections import Counter
from mrjob.job import MRJob
import re

def map_function(line):
  """Emits each word bigram as a key-value pair, where the key represents the bigram separated by a comma and the value is set to 1."""

  words = re.findall(r'\b\w+\b', line.lower())

  for i in range(len(words) - 1):
    bigram = ','.join(words[i:i+2])
    yield bigram, 1

def reduce_function(bigram, counts):
  """Reduces the bigrams by counting their occurrences."""

  counts[bigram] += 1
  return counts

def main():
  """Counts the bigrams in the given text."""

  text = """a man a plan a canal panama there was a plan to build a canal in panama in panama a canal was built."""

  # Split the text into lines.
  lines = text.split('\n')

  # Create a Counter object to store the bigram counts.
  counts = Counter()

  # Map the lines to bigrams.
  for line in lines:
    for bigram, count in map_function(line):
      counts = reduce_function(bigram, counts)

  # Print the bigram counts.
  for bigram, count in counts.items():
    print(f'{bigram}: {count}')

if __name__ == '__main__':
  main()
