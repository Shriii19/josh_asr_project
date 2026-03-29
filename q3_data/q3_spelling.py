import pandas as pd
import unicodedata

df = pd.read_csv("q3_data/unique_words.csv")
words = df.iloc[:, 0].tolist()
print("total words:", len(words))


def is_valid_hindi_word(word):
    word = str(word).strip()
    if len(word) < 2:
        return False
    for ch in word:
        block = unicodedata.name(ch, "").split()[0] if ch.strip() else "SPACE"
        # allow devanagari, digits, spaces, and common punctuation
        if not ("DEVANAGARI" in block or ch.isdigit() or ch in " -."):
            return False
    return True


results = []

for word in words:
    word = str(word).strip()

    if is_valid_hindi_word(word):
        if len(word) >= 4:
            label = "correct spelling"
            confidence = "high"
            reason = "valid devanagari word with enough length"
        else:
            label = "correct spelling"
            confidence = "medium"
            reason = "short but valid devanagari chars"
    else:
        label = "incorrect spelling"
        confidence = "low"
        reason = "contains unexpected characters or too short"

    results.append({"word": word, "label": label, "confidence": confidence, "reason": reason})

result_df = pd.DataFrame(results)
result_df.to_csv("q3_data/spelling_results.csv", index=False)

correct_count = len(result_df[result_df["label"] == "correct spelling"])
print("correct words:", correct_count)
print("incorrect words:", len(result_df) - correct_count)

low_conf = result_df[result_df["confidence"] == "low"]
low_conf.head(50).to_csv("q3_data/low_confidence_sample.csv", index=False)
print("saved low confidence sample")