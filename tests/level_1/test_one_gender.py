from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('verb_male', 'verb_female', 'male') == 'verb_male'
    assert genderalize('verb_male', 'verb_female', 'female') == 'verb_female'
