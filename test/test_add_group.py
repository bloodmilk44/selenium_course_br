from model.group import Group


def test_createnewgroup(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="ggg43g34g43g34", header="g34g43g43g43", footer="egwgegewgwegwe"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)