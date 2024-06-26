import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.fixture
def good_words():
    return {'good1', 'good2'}


@pytest.fixture
def bad_words():
    return {'bad1', 'bad2'}


def test__check_tweet_sentiment__return_good_if_text_has_more_good_words(good_words, bad_words):
    text = 'good1 good2 bad1'
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual == 'GOOD'


def test__check_tweet_sentiment__return_bad_if_text_has_more_bad_words(good_words, bad_words):
    text = 'good1 bad1 bad2'
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual == 'BAD'


def test__check_tweet_sentiment__return_none_if_text_has_good_words_equal_bad_words(good_words, bad_words):
    text = 'good1 bad1'
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual is None


def test__check_tweet_sentiment__return_bad_if_text_has_no_good_words(good_words, bad_words):
    text = 'bad1'
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual == 'BAD'


def test__check_tweet_sentiment__return_good_if_text_has_not_bad_words(good_words, bad_words):
    text = 'good1'
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual == 'GOOD'


def test__check_tweet_sentiment__return_none_if_text_has_not_good_and_bad_words(good_words, bad_words):
    text = 'text'
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual is None


def test__check_tweet_sentiment__return_none_if_text_is_blank(good_words, bad_words):
    text = ''
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual is None


def test__check_tweet_sentiment__return_bad_if_good_words_is_blank(bad_words):
    text = 'bad1'
    good_words = set()
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual == 'BAD'


def test__check_tweet_sentiment__return_good_if_bad_words_is_blank(good_words):
    text = 'good1'
    bad_words = set()
    actual = check_tweet_sentiment(text, good_words, bad_words)
    assert actual == 'GOOD'
