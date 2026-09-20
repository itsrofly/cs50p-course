from project import get_json, list_status, get_verbs
import pandas as pd
import pytest

def test_get_json():
    with pytest.raises(TypeError):
        get_json("cs50.harvard.edu/students.json")

    with pytest.raises(TypeError):
        get_json()

    assert type(get_json("https://srrofly.github.io/IrregularVerbs/verbs.json")) == dict

def test_get_verbs():
    with pytest.raises(ValueError):
        get_verbs("Verbs")

    assert type(get_verbs(get_json("https://srrofly.github.io/IrregularVerbs/verbs.json"))) == dict

def test_list_status():
    with pytest.raises(TypeError):
        list_status()

    with pytest.raises(ValueError):
        list_status("list")

    assert isinstance(list_status(get_json("https://srrofly.github.io/IrregularVerbs/verbs.json")), pd.DataFrame) == True