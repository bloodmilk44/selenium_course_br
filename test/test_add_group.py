from model.group import Group


def test_createnewgroup(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list_db()
    app.group.create(group)
    new_groups = db.get_group_list_db()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
