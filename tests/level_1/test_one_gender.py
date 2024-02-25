from functions.level_1.one_gender import genderalize


def test_genderalize__male():
    assert genderalize('verb_male', 'verb_female', 'male') == 'verb_male'


def test_genderalize__not_male():
    assert genderalize('verb_male', 'verb_female', '') == 'verb_female'
    assert genderalize('verb_male', 'verb_female', 'kjljlkjlkj') == 'verb_female'
