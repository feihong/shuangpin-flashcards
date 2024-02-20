from pathlib import Path

layout_file = Path('layout.txt')
output_file = Path('flashcards.txt')

header = """\
#separator:semicolon
#html:true
#notetype column: 1
#tags column: 2
#columns:basic;tags;front;back
"""

def get_mappings():
  lines = Path('layout.txt').read_text().splitlines()
  for line in lines:
    line = line.strip()
    if not line:
      continue

    initial, *finals = line.split(' ')
    yield initial, finals

def get_key_cards():
  for initial, finals in get_mappings():
    yield 'cloze;shuangpin;双拼韵母 for %s: {{c1::%s}};' % \
      (initial, ', '.join(finals))

def get_finals_cards():
  for initial, finals in get_mappings():
    for final in finals:
      yield 'cloze;shuangpin;双拼 key for %s: {{c1::%s}};' % \
        (final, initial)

with output_file.open('w') as fp:
  fp.write(header)

  for line in get_key_cards():
    fp.write(line + '\n')

  for line in get_finals_cards():
    fp.write(line + '\n')
