def normalize_numbers(text):
    mapping = {
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
        "सौ": "100",
        "हज़ार": "1000"
    }

    # Handle edge case
    if "दो चार" in text:
        return text

    words = text.split()
    result = []

    for word in words:
        if word in mapping:
            result.append(mapping[word])
        else:
            result.append(word)

    return " ".join(result)


def detect_english_words(text):
    english_words = ["interview", "problem", "job", "project"]

    result = []

    for word in text.split():
        if word.lower() in english_words:
            result.append(f"[EN]{word}[/EN]")
        else:
            result.append(word)

    return " ".join(result)


def cleanup_pipeline(text):
    text = normalize_numbers(text)
    text = detect_english_words(text)
    return text


# 🔥 TEST CASES (IMPORTANT)
sample1 = "तीन लोग आए"
sample2 = "मेरा interview अच्छा गया"
sample3 = "दो चार बातें"

print("Input:", sample1)
print("Output:", cleanup_pipeline(sample1))

print("Input:", sample2)
print("Output:", cleanup_pipeline(sample2))

print("Input:", sample3)
print("Output:", cleanup_pipeline(sample3))