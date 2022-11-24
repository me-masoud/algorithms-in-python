def sync_data():
    try:
        goal = frappe.get_doc('Goal', doc.related_goal)
        tasks = frappe.db.get_list('Task', filters={'related_goal': doc.related_goal},
                                   fields=[
                                       'responsible_person',
                                       'status',
                                       'name'

                                   ])
    except:
        return 0

    goal.related_tasks = []

    for item in tasks:
        goal.append('related_tasks', {
            'task': item.name,
            'responsible': item.responsible_person,
            'status': item.status,
            'goal': doc.related_goal,
        })
    goal.save()


def sync_deleted_data(goal_name):
    goal = frappe.get_doc('Goal', goal_name)
    tasks = frappe.db.get_list('Task', filters={'related_goal': goal_name},
                               fields=[
                                   'responsible_person',
                                   'status',
                                   'name'

                               ])

    goal.related_tasks = []

    for item in tasks:
        goal.append('related_tasks', {
            'task': item.name,
            'responsible': item.responsible_person,
            'status': item.status,
            'goal': doc.related_goal,
        })
    goal.save()


if doc.related_goal:

    task_old = frappe.get_doc('Task', doc.name, fields=['name', 'related_goal'])

    if doc.related_goal != task_old.related_goal:
        frappe.msgprint("ssss")
        sync_deleted_data(task_old.related_goal)

    # sync_data()
