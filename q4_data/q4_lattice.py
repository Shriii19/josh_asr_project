import pandas as pd

ref_df = pd.read_csv("q4_data/Question 4 - Task.csv")
model_df = pd.read_csv("q4_data/ft_results.csv")

reference = ref_df.iloc[0, 0]
model_outputs = model_df.iloc[0].tolist()

print("reference:", reference)
print("model outputs:", model_outputs)


def create_lattice(reference, outputs):
    ref_words = str(reference).split()
    all_outputs = [str(o).split() for o in outputs]

    # find max length across reference and all outputs
    max_len = len(ref_words)
    for out in all_outputs:
        max_len = max(max_len, len(out))

    lattice = []
    for i in range(max_len):
        bin_words = set()

        if i < len(ref_words):
            bin_words.add(ref_words[i])

        # if 3 or more models agree on a word at this position, trust them over ref
        word_votes = {}
        for out in all_outputs:
            if i < len(out):
                w = out[i]
                word_votes[w] = word_votes.get(w, 0) + 1
                bin_words.add(w)

        # if most models agree on something different from ref, note it
        for w, count in word_votes.items():
            if count >= 3 and i < len(ref_words) and w != ref_words[i]:
                print(f"position {i}: models prefer '{w}' over reference '{ref_words[i]}'")

        lattice.append(list(bin_words))

    return lattice


def compute_wer_with_lattice(prediction, lattice):
    pred_words = str(prediction).split()
    errors = 0
    total = max(len(pred_words), len(lattice))

    for i in range(len(lattice)):
        if i < len(pred_words):
            if pred_words[i] not in lattice[i]:
                errors += 1
        else:
            errors += 1  # deletion

    for i in range(len(lattice), len(pred_words)):
        errors += 1  # insertion

    return errors / total if total > 0 else 0


lattice = create_lattice(reference, model_outputs)

for i, bin_words in enumerate(lattice):
    print("position", i, ":", bin_words)

for j, output in enumerate(model_outputs):
    wer = compute_wer_with_lattice(output, lattice)
    print(f"model {j+1} lattice WER: {round(wer, 4)}")