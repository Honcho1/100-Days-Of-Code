# Calcculate love score

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    # Count the letters in "TRUE"
    true_score = (
        combined_names.count("t") +
        combined_names.count("r") +
        combined_names.count("u") +
        combined_names.count("e")
    )

    # Count the letters in "LOVE"
    love_score = (
        combined_names.count("l") +
        combined_names.count("o") +
        combined_names.count("v") +
        combined_names.count("e")
    )

    # Comine scores
    final_score = int(str(true_score) + str(love_score))

    print(final_score)

calculate_love_score("Daniel", "Delight")