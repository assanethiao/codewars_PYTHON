"""
Third day at your new cryptoanalyst job and you come across your toughest assignment yet.
Your job is to implement a simple keyword cipher. A keyword cipher is a type of monoalphabetic substitution
where two parameters are provided as such (string, keyword). The string is encrypted by taking the keyword,
dropping any letters that appear more than once. The rest of the letters of the alphabet that aren't used are
then appended to the end of the keyword.

For example, if your string was "hello" and your keyword was "wednesday", your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.

To encrypt 'hello' you'd substitute as follows,

              abcdefghijklmnopqrstuvwxyz
  hello ==>   |||||||||||||||||||||||||| ==> bshhk
              wednsaybcfghijklmopqrtuvxz

hello encrypts into bshhk with the keyword wednesday. This cipher also uses lower case letters only.

Good Luck.
"""
def keyword_cipher(msg, keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Nettoyer le mot-clé
    seen = set()
    cleaned_keyword = ''.join([c for c in keyword.lower() if c not in seen and not seen.add(c)])

    # Créer l'alphabet de substitution
    remaining_letters = ''.join([c for c in alphabet if c not in cleaned_keyword])
    cipher_alphabet = cleaned_keyword + remaining_letters

    # Créer le dictionnaire de substitution
    cipher_dict = {a: b for a, b in zip(alphabet, cipher_alphabet)}

    # Chiffrer le message (en minuscules uniquement)
    encrypted = ''
    for c in msg.lower():  # on ignore la casse du message
        encrypted += cipher_dict[c] if c in cipher_dict else c

    return encrypted

