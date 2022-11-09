def generate_lesson(lesson_number, chord_word_pairs):
    with open(f"../docs/lesson_{lesson_number}") as output_file:
        output_file.writelines(
            [
                f"This is lesson {lesson_number} of the Pyanist chording course.",
                f"To type {chord_word_pairs[0][1]}, press {chord_word_pairs[0][1]} at the same time.",
                " ".join([chord_word_pairs[0][1]] * 5),
                f"{chord_word_pairs[1][1]} is {chord_word_pairs[1][1]}",
                " ".join([chord_word_pairs[1][1]] * 5),
            ]
        )

        last_words = [chord_word_pairs[0][1], chord_word_pairs[1][1]]
