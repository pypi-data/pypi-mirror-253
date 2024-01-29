import re

def collapse_whitespace(text):
    collapsed_text = re.sub(r'\s+', ' ', text)
    return collapsed_text

allowed_chars_all = " !\"#$'()*+,…-.:;?@0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzČčŠšŽžÉÍÜßàáèéíñóôöøüē"

allowed_chars_normalized = " !\",…-.:?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzČčŠšŽžÉÍÜßàáèéíñóôöøüē"

allowed_chars_min = " !\",…-.:?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzČčŠšŽž"

char_map = {
    '–': '-',
    "'": "\"",
    "«": "\"",
    "»": "\"",
    "...": "…",
    '‚': ',',
    "›": "\"",
    "‹": "\"",
    "“": "\"",
    "”": "\"",
    "‘": "\"",
    "’": "\"",
    "–": "-",
    "—": "-",
    "Ć": "Č",
    "ć": "č",
    "ç": "c",
    "‚": "\"",
    "=": " je ",
    " ": "",
    "♥": "love",
    "●": "-",
    "": "",
    "ȇ‌": "e",
    "đ": "dž"
}

def unify_chars(text, type = 'all'):
    text = collapse_whitespace(text)
    for key, val in char_map.items():
        text = text.strip().replace(key, val)

    allowed_chars = allowed_chars_all
    if type == 'normalized':
        allowed_chars = allowed_chars_normalized
    elif type == 'min':
        allowed_chars = allowed_chars_min

    illegal = []
    for char in text:
        if char not in allowed_chars:
            print(f"illegal char: {char}")
            illegal.append(char)

    for char in illegal:
        text = text.replace(char, "")

    return text