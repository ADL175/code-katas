"""Testing proper_parenthetics function."""


def test_side():
    """Test the watch_pyramid_from_the_side function."""
    from string_pyramid import watch_pyramid_from_the_side
    watch_pyramid_from_the_side('abc')
    assert watch_pyramid_from_the_side('abc') == '  c  \n bbb \naaaaa'
    assert watch_pyramid_from_the_side('abcde') == '    e    \n   ddd   \n  ccccc  \n bbbbbbb \naaaaaaaaa'


def test_top():
    """Test the watch_pyramid_from_above function."""
    from string_pyramid import watch_pyramid_from_above
    watch_pyramid_from_above('abc')
    # import pdb; pdb.set_trace()
    assert watch_pyramid_from_above('abc') == 'aaaaa\nabbba\nabcba\nabbba\naaaaa'
    assert watch_pyramid_from_above('abcde') == 'aaaaaaaaa\nabbbbbbba\nabcccccba\nabcdddcba\nabcdedcba\nabcdddcba\nabcccccba\nabbbbbbba\naaaaaaaaa'


def test_visible_count():
    """Test the count visible tiles."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abc') == 25
    assert count_visible_characters_of_the_pyramid('abcde') == 81


def test_all_count():
    """Test the count all tiles."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('abc') == 35
    assert count_all_characters_of_the_pyramid('abcde') == 165
