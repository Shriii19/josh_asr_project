number_map = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "छह": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "तीस": "30",
    "चालीस": "40",
    "पचास": "50",
    "साठ": "60",
    "सत्तर": "70",
    "अस्सी": "80",
    "नब्बे": "90",
    "सौ": "100",
    "हज़ार": "1000"
}

# idioms where number words should not be converted
idioms = ["दो-चार", "दो चार", "चार-पांच", "पांच-सात"]


def normalize_numbers(text):
    for idiom in idioms:
        if idiom in text:
            return text

    words = text.split()
    result = []
    for word in words:
        if word in number_map:
            result.append(number_map[word])
        else:
            result.append(word)
    return " ".join(result)


def detect_english_words(text):
    result = []
    for word in text.split():
        # roman script words are english
        if word.isascii() and word.isalpha():
            result.append("[EN]" + word + "[/EN]")
        else:
            result.append(word)
    return " ".join(result)


def run_pipeline(text):
    text = normalize_numbers(text)
    text = detect_english_words(text)
    return text


if __name__ == "__main__":
    tests = [
        "तीन लोग आए",
        "मेरा interview अच्छा गया",
        "दो चार बातें",
        "उसने दस किताबें खरीदीं",
        "मुझे job मिल गई"
    ]

    for t in tests:
        print("in: ", t)
        print("out:", run_pipeline(t))
        print()