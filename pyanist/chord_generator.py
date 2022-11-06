from itertools import combinations, chain, product


fingers = {
    tuple(sorted(set("qaz"))),
    tuple(sorted(set("wsx"))),
    tuple(sorted(set("edc"))),
    tuple(sorted(set("rfvtgb"))),
    tuple(sorted(set("yhnujm"))),
    tuple(sorted(set("ik"))),
    tuple(sorted(set("ol"))),
    tuple(sorted(set("p"))),
}

hand_rows = [
    (
        tuple(sorted(set("qwert"))),
        tuple(sorted(set("asdfg"))),
        tuple(sorted(set("zxcvb"))),
    ),
    (tuple(sorted(set("yuiop"))), tuple(sorted(set("hjkl"))), tuple(sorted(set("nm")))),
]

center_columns_and_corresponding_hands = [
    (
        tuple(sorted(set("tgb"))),
        tuple(sorted(set("qwerasdfzxcv"))),
    ),
    (
        tuple(sorted(set("yhn"))),
        tuple(sorted(set("uiopjklm"))),
    ),
]

home_row_keys = "asdfjkl"


def verify_hand(chord, top_row, _, bottom_row, center_column, other_keys_on_hand):
    top_row_keys = set(chord) & set(top_row)
    bottom_row_keys = set(chord) & set(bottom_row)

    if top_row_keys and bottom_row_keys:
        return False

    pressed_center_column_keys = set(chord) & set(center_column)
    other_pressed_keys_on_hand = set(chord) & set(other_keys_on_hand)

    if pressed_center_column_keys and other_pressed_keys_on_hand:
        return False

    return True


def generate_chords():
    for fingers_to_use in chain(
        combinations(fingers, 3), combinations(fingers, 4), combinations(fingers, 5)
    ):
        for raw_chord in product(*fingers_to_use):
            chord = tuple(sorted(set(raw_chord)))
            left_hand_rows, right_hand_rows = hand_rows
            left_hand_center, right_hand_center = center_columns_and_corresponding_hands

            if not verify_hand(chord, *left_hand_rows, *left_hand_center):
                continue

            if not verify_hand(chord, *right_hand_rows, *right_hand_center):
                continue

            keys_outside_of_home_row = set(chord) - set(home_row_keys)
            center_column_keys = set(
                key
                for key in chord
                if any(
                    key in center_column
                    for center_column, _ in center_columns_and_corresponding_hands
                )
            )
            score = sum(
                [len(chord), len(keys_outside_of_home_row), len(center_column_keys)]
            )

            yield tuple(chord), score
