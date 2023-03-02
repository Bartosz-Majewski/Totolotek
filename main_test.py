from main import draw_numbers


def test_draw_numbers():
    # given

    # when
    for _ in range(501):
        drawn_numbers = sorted(list(draw_numbers()))
        # then
        assert len(drawn_numbers) == 6
        assert drawn_numbers[0] >= 1
        assert drawn_numbers[-1] <= 49
