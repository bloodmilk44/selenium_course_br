from model.group import Group


def test_createnewgroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="ggg43g34g43g34", header="g34g43g43g43", footer="egwgegewgwegwe"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
