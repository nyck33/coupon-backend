'''
convert json to dict

download from db:
Make json compatible with Flutter frontend
Schema:
Plan: id: int (pk), //take out
     name: varchar

Task: id: int  //take out
plan_id: int (fk) //use to form list of dicts
desc: varchar //string
complete: int 0 or 1  //to bool T or F
'''
import postgres_repo

