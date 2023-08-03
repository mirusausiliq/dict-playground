ipa_data = {
    'a': 'a',
    'b': 'b',
    'c': 't\u0361s',
    'd': 'ɬ',
    'e': 'ə',
    'f': 'f',
    # 'g': ' -',
    'h': 'h',
    'i': 'i',
    # 'j': ' -',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'ng': 'ŋ',
    'o': 'o',
    'p': 'p',
    # 'q': ' -',
    'r': 'ɾ',
    's': 's',
    't': 't',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': 'j',
    # 'z': ' -',
    "'": 'ʡ',
    '^': 'ʔ',  # '  
    ':': 'ː',  # ^ 
    ' ': ' ',
}

def getIPA(term):
  new_term = term.lower()
  ipa = ""
  i = 0

  vowels = ('a', 'e', 'i', 'o', 'u')
  consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', "'", '^')


  while i < len(new_term):
    if i < len(new_term) - 1 and new_term[i] in vowels:
        if new_term[i-1] not in consonants:
            new_term = new_term[:i] + "^" + new_term[i:]
            i += 1
        elif i < len(new_term) - 1 and new_term[i+1] not in consonants:
            new_term = new_term[:i] + "^" + new_term[i:]
            i += 1
    i += 1

  i = 0

  while i < len(new_term):
    
    if i < len(new_term) - 1 and new_term[i] == "n" and new_term[i+1] == "g":
      ipa += ipa_data.get("ng", "")
      i += 2
    else:
      ipa += ipa_data.get(new_term[i], "")
      i += 1

  

  return ipa

