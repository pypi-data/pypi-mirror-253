

allowed_chars = []

char_map = {
    '–': '-',
    "'": "\"",
    "«": "\"",
    "»": "\"",
    "...": "…",
    '‚': ',',
    "›": "\"",
    "‹": "\"",

    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
    "'": "\"",
}

def unify_chars(text):
    for key, val in char_map.items():
        text = text.strip().replace(key, val)

    for char in text:
        if char not in allowed_chars:
            print(f"illegal char: {char}")