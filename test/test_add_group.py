from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

  
def test_createnewgroup(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="ggg43g34g43g34", header="g34g43g43g43", footer="egwgegewgwegwe"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()


  
