import csv

CHORDS_PER_LESSON = 10


def generate_lesson(lesson_number, chord_word_pairs):
    with open(f"./docs/lesson_{lesson_number + 1}.txt", "w") as output_file:
        output_lines = [
            f"This is lesson {lesson_number + 1} of the Pyanist chording course.",
            f"To type {chord_word_pairs[0][1]}, press letters {chord_word_pairs[0][0]} at the same time.",
            " ".join([chord_word_pairs[0][1]] * 5),
            f"{chord_word_pairs[1][1]} is {chord_word_pairs[1][0]}",
            " ".join([chord_word_pairs[1][1]] * 5),
            " ".join([chord_word_pairs[0][1], chord_word_pairs[1][1]] * 3),
        ]

        last_words = [chord_word_pairs[0][1], chord_word_pairs[1][1]]

        for chord, word in chord_word_pairs[2:]:
            previus_word = last_words[-1]
            penultime_word = last_words[-2]

            output_lines.append(f"{word} is {chord}")
            output_lines.append(" ".join([word] * 5))
            output_lines.append(
                " ".join(
                    [
                        penultime_word,
                        word,
                        word,
                        previus_word,
                        word,
                        word,
                        previus_word,
                        penultime_word,
                        word,
                    ]
                )
            )

            output_lines.append(" ".join(last_words))
            last_words.append(word)

        output_lines.append(" ".join(last_words))
        output_file.write("\n".join(output_lines))


with open("./docs/all_chords.csv") as chords_file:
    chords_data = list(csv.DictReader(chords_file))

for lesson_number in range(10):
    lesson_chords_data = chords_data[
        lesson_number * CHORDS_PER_LESSON : (lesson_number + 1) * CHORDS_PER_LESSON
    ]
    list_of_words = " ".join(item["Word"] for item in lesson_chords_data)
    print(
        f"* [Lesson {lesson_number + 1}](docs/lesson_{lesson_number + 1}.txt) - {list_of_words}"
    )
    generate_lesson(
        lesson_number,
        [(item["Chord"], item["Word"]) for item in lesson_chords_data],
    )
