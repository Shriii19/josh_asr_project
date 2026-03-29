import pandas as pd

# Load words
df = pd.read_csv("q3_data/unique_words.csv")

# Assume column name is 'word'
words = df.iloc[:, 0].tolist()

print("Total words:", len(words))

from collections import Counter

# Count frequency
word_freq = Counter(words)

def classify_word(word):
    freq = word_freq[word]

    if len(word) <= 2:
        return "incorrect", "low"

    if freq > 5:
        return "correct", "high"
    elif freq > 2:
        return "correct", "medium"
    else:
        return "incorrect", "low"
    
results = []

for word in words:
    label, confidence = classify_word(word)

    results.append({
        "word": word,
        "label": label,
        "confidence": confidence
    })

result_df = pd.DataFrame(results)

result_df.to_csv("q3_data/spelling_results.csv", index=False)

print("✅ Q3 results saved!")

low_conf = result_df[result_df["confidence"] == "low"]

sample = low_conf.head(50)

sample.to_csv("q3_data/low_confidence_sample.csv", index=False)

print("Saved low confidence sample")