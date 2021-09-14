'''
The actual uploading and downloading from database
to Plan and Task tables

Schema:
Plan: id: int (pk),
     name: varchar

Task:
id: int
plan_id: int (fk)
desc: varchar
complete: int 0 or 1

'''
from postgres.create_tables import insert_plan, insert_task
# dummy data
data = [{"plan_name": "Move out of house", "tasks":[{"description":"get storage",
                                               "complete": "False"},
                                              {"description":"get ispace",
                                                "complete": "False"}]},
        {"plan_name": "Cook rice", "tasks":[{"description":"wash rice",
                                               "complete": "False"},
                                              {"description":"plug in cooker",
                                                "complete": "False"}]}]

def make_sql(data=None):
    sqls = []
    #iterate data
    for plan in data:
        plan_name = plan['plan_name'] # json is name
        sql_plan = """INSERT INTO plans (plan_name)
                 VALUES(%s) RETURNING plan_id;"""

        plan_id = insert_plan(sql_plan, plan_name)
        print(f'plan_id: {plan_id}')
        tasks = plan['tasks']

        for task in tasks:
            description = task['description']
            #todo: adjjust this for actual dict False or false
            complete = task['complete']
            if complete == "True":
                complete = 1
            else:
                complete = 0

            sql_task = """INSERT INTO tasks (plan_id, description, complete)
                     VALUES(%s, %s, %s) RETURNING task_id;"""

            task_id = insert_task(sql_task, plan_id, description, complete)
            print(f'task_id: {task_id}')

if __name__ == "__main__":
    make_sql(data)
    print('done')


