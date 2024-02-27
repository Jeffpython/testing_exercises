import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__correct_link():
    url = 'https://github.com/Jeffpython/testing_exercises/pull/1'
    assert is_github_pull_request_url(url)


@pytest.mark.xfail(reason="this link can be taken as correct")
def test__is_github_pull_request_url__link_without_protocol():
    url = 'github.com/Jeffpython/testing_exercises/pull/1'
    assert is_github_pull_request_url(url)


@pytest.mark.xpass(reason="the link is not correct")
def test__is_github_pull_request_url__link_with_incorrect_protocol():
    url = 'ftp://github.com/Jeffpython/testing_exercises/pull/1'
    assert is_github_pull_request_url(url)


def test__is_github_pull_request_url__link_with_incorrect_domain_name():
    url = 'https://xgithub.com/Jeffpython/testing_exercises/pull/1'
    assert not is_github_pull_request_url(url)


@pytest.mark.xpass(reason="pull number is required")
def test__is_github_pull_request_url__link_without_pull_number():
    url = 'https://github.com/Jeffpython/testing_exercises/pull/'
    assert is_github_pull_request_url(url)


@pytest.mark.xpass(reason="the pull number must be correct")
def test__is_github_pull_request_url__link_with_incorrect_pull_number():
    url = 'https://github.com/Jeffpython/testing_exercises/pull/a'
    assert is_github_pull_request_url(url)


def test__is_github_pull_request_url__blank_string():
    url = ''
    assert not is_github_pull_request_url(url)
