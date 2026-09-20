from seasons import get_time
from datetime import date
import pytest


def test_lessFiveYears():
    time = date.today()

    y,m,d = str(time).split("-")
    y = int(y) - 5

    time = get_time(f"{y:04}-{m}-{d}")
    assert f"{time} minutes" == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"

def test_invalidInput():
    with pytest.raises(SystemExit):
        get_time("2022/06/04")