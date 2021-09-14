'''
Schema:
Plan: id: int (pk),
     name: varchar
     tasks: List[Task]

Task: id: int
plan_id: int (fk)
desc: varchar
complete: int 0 or 1

'''
import psycopg2
from .config_parser import config



def create_tables():
    commands = (
        """
        CREATE TABLE plans(
            plan_id SERIAL PRIMARY KEY,
            plan_name VARCHAR(255) NOT NULL 
        )
        """,
        """
        CREATE TABLE tasks(
            task_id SERIAL PRIMARY KEY,
            plan_id INTEGER,
            description VARCHAR(255),
            complete INTEGER,
            FOREIGN KEY(plan_id)
                REFERENCES plans (plan_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    conn = None
    try:

        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for c in commands:
            cur.execute(c)

        cur.close()
        #commit changes
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_plan(sql, plan_name):
    #sql = """INSERT INTO """
    conn = None
    # returning plan_id
    plan_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (plan_name,))
        plan_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return plan_id

def insert_task(sql, plan_id, description, complete):
    conn = None

    task_id = None
    try:
        params =config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (plan_id, description, complete))
        task_id = cur.fetchone()[0] # of 4 cols
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return task_id


def main():
    #create_tables()
    pass
if __name__ == "__main__":
    main()
