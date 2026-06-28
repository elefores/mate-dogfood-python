import pytest
from pydantic import ValidationError

from src.models import User


def test_valid_user_round_trips_to_payload():
    user = User(id=1, name="Ada", email="ada@example.com")
    payload = user.as_payload()
    assert payload["id"] == 1
    assert payload["email"] == "ada@example.com"


def test_invalid_email_is_rejected():
    with pytest.raises(ValidationError):
        User(id=2, name="Grace", email="not-an-email")
