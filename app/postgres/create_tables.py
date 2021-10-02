'''
Schema:
Plan: id: int (pk),
     name: varchar
     tasks: List[Task]

Task: id: int
plan_id: int (fk)
desc: varchar
complete: int 0 or 1
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
        """,

'''
import psycopg2
from .config_parser import config


def create_tables():
    commands = (
        """
        CREATE TABLE users(
            userId SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email: VARCHAR (255) NOT NULL,
            loginStatus: VARCHAR(255) NOT NULL,
            currentScreen: VARCHAR(255) NOT NULL,
            hotel: VARCHAR(255),
            room: VARCHAR(255),
            arrivalDate: VARCHAR(255),
            departDate: VARCHAR(255),
            avatarExists: BOOLEAN NOT NULL,
            avatarUrl: VARCHAR(255),
        """,
        """
        CREATE TABLE user_coupons(
            issueId: SERIAL PRIMARY KEY,
            couponId: INTEGER NOT NULL,
            couponType: VARCHAR(255) NOT NULL,
            hotelName: VARCHAR(255) NOT NULL,
            expiryDate: VARCHAR(255),
            couponAmount: VARCHAR(255),
            usedOn: VARCHAR(255), 
            isUsed: BOOLEAN NOT NULL,
            imageExists: BOOLEAN NOT NULL,
            details: VARCHAR(255) NOT NULL,
            imageUrl: VARCHAR(255),
            couponName: VARCHAR(255) NOT NULL 
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
