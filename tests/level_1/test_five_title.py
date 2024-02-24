from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('title', 0) == 'title'
    assert change_copy_item('title') == 'Copy of title'
    assert change_copy_item('Copy of (0)') == 'Copy of (1)'
    assert change_copy_item('Copy of (a)') == 'Copy of (a) (2)'
    assert change_copy_item('Copy of') == 'Copy of (2)'
