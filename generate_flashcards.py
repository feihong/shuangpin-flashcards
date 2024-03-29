from pathlib import Path

layout_file = Path('layout.txt')
examples_file = Path('example-words.txt')
output_file = Path('flashcards.txt')

header = """\
#separator:tab
#html:true
#notetype column:1
#tags column:2
"""

def get_mappings():
  lines = layout_file.read_text().splitlines()
  for line in lines:
    line = line.strip()
    if not line:
      continue

    initial, *finals = line.split(' ')
    yield initial, finals

def get_key_cards():
  for initial, finals in get_mappings():
    yield 'Cloze\tshuangpin\t双拼韵母 for %s: {{c1::%s}}' % \
      (initial, ', '.join(finals))

def get_finals_cards():
  for initial, finals in get_mappings():
    for final in finals:
      yield 'Cloze\tshuangpin\t双拼 key for %s: {{c1::%s}}' % \
        (final, initial)

def get_example_cards():
  lines = examples_file.read_text().splitlines()
  for line in lines:
    line = line.strip()
    if not line:
      continue

    word, keys = line.split(maxsplit=1)
    yield 'Cloze\tshuangpin\t双拼 for %s: {{c1::%s}}' % (word, keys)

with output_file.open('w') as fp:
  fp.write(header)

  for line in get_key_cards():
    fp.write(line + '\n')

  for line in get_finals_cards():
    fp.write(line + '\n')

  for line in get_example_cards():
    fp.write(line + '\n')
