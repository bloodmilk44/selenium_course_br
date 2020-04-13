from model.group import Group


def test_createnewgroup(app):
    app.group.create(Group(name="ggg43g34g43g34", header="g34g43g43g43", footer="egwgegewgwegwe"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
