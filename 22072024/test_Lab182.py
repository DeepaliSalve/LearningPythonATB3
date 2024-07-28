import pytest

@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0


@pytest.mark.smoke
def test_sub2():
    assert 1 - 1 == 0


@pytest.mark.sanity
def test_sub3():
    assert 0 - 0 != 0

@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 != 0
