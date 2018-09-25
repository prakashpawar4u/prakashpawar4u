import pytest

@pytest.fixture

def bookmark(app):
    return Bookmark.create(user_id =1, works_id = 1)

