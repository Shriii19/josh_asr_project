import pandas as pd

# Load data
ref_df = pd.read_csv("q4_data/Question 4 - Task.csv")
model_df = pd.read_csv("q4_data/ft_results.csv")

# Example: take one row
reference = ref_df.iloc[0, 0]
model_outputs = model_df.iloc[0].tolist()

print("Reference:", reference)
print("Models:", model_outputs)

def create_lattice(reference, outputs):
    ref_words = str(reference).split()

    lattice = []

    for i in range(len(ref_words)):
        bin_words = set()

        # Add reference word
        bin_words.add(ref_words[i])

        # Add model words (if available)
        for out in outputs:
            out_words = str(out).split()
            if i < len(out_words):
                bin_words.add(out_words[i])

        lattice.append(list(bin_words))

    return lattice

lattice = create_lattice(reference, model_outputs)

for i, bin in enumerate(lattice):
    print(f"Position {i}: {bin}")

def lattice_match(prediction, lattice):
    pred_words = prediction.split()

    errors = 0

    for i in range(min(len(pred_words), len(lattice))):
        if pred_words[i] not in lattice[i]:
            errors += 1

    return errors