from xrx_text_utils import text_pos, left_align, right_align


def test_text_pos():
    text_line = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert text_pos("1", text_line) == "1"
    assert text_pos("1-2", text_line) == "12"
    assert text_pos("1-36", text_line) == "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert (
        text_pos("1-13712347536456746", text_line)
        == "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )


def test_left_align():
    assert left_align("TEST", 10) == "TEST      "
    assert left_align("TESTTESTTEST", 12) == "TESTTESTTEST"
    assert left_align("", 10) == "          "
    assert left_align("TESTTESTTEST", 10) == "TESTTESTTE"


def test_right_align():
    assert right_align("TEST", 10) == "      TEST"
    assert right_align("TESTTESTTEST", 12) == "TESTTESTTEST"
    assert right_align("", 10) == "          "
    assert right_align("TESTTESTTEST", 10) == "STTESTTEST"
