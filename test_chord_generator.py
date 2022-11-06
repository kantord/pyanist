from chord_generator import *


chords = list(generate_chords())


def get_score(keys):
    target_chord = tuple(sorted(set(keys)))
    for chord, score in chords:
        if target_chord == chord:
            return score


def test_returns_chords_that_have_a_score():
    assert (("a", "d", "k"), 3) in chords


def test_returns_multiple_chords():
    assert len(chords) > 1000


def test_each_chord_is_unique():
    assert len(set(chord for chord, _ in chords)) == len(chords)


def test_order_does_not_matter():
    assert len(set(chord for chord, _ in chords)) == len(
        set(tuple(sorted(set(chord))) for chord, _ in chords)
    )


def test_there_are_chords_with_4_characters():
    assert any(len(chord) == 4 for chord, _ in chords)


def test_there_are_chords_with_5_characters():
    assert any(len(chord) == 5 for chord, _ in chords)


def test_for_each_finger_there_is_only_one_key():
    for chord, _ in chords:
        for finger in fingers:
            letters_on_finger = set(chord) & set(finger)
            assert len(letters_on_finger) <= 1


def test_on_each_hand_bottom_and_top_row_arent_used_together():
    for chord, _ in chords:
        for top_row, _, bottom_row in hand_rows:
            top_row_keys = set(chord) & set(top_row)
            bottom_row_keys = set(chord) & set(bottom_row)
            assert top_row_keys == set() or bottom_row_keys == set()


def test_center_columns_are_the_only_key_pressed():
    for chord, _ in chords:
        for center_column, other_keys_on_hand in center_columns_and_corresponding_hands:
            pressed_center_column_keys = set(chord) & set(center_column)
            other_pressed_keys_on_hand = set(chord) & set(other_keys_on_hand)

            assert (
                pressed_center_column_keys == set()
                or other_pressed_keys_on_hand == set()
            )


def test_for_each_key_pressed_the_score_is_increased_1():
    assert get_score("sdf") == 3


def test_for_each_key_pressed_the_score_is_increased_2():
    assert get_score("asdf") == 4


def test_that_keys_outside_of_home_row_increase_score_1():
    assert get_score("asdr") == 5


def test_that_keys_outside_of_home_row_increase_score_2():
    assert get_score("asir") == 6


def test_keys_on_center_columns_makes_score_worse_1():
    assert get_score("asey") == 7


def test_keys_on_center_columns_makes_score_worse_2():
    assert get_score("scn") == 6
