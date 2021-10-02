from configparser import ConfigParser

def config(filename='/media/nobu/NTFSUbuWin/1_TAP/BackendIAAS/fastAPITutorial/postgres/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to postgresql
    db={}
    if parser.has_section(section):
        params = parser.items(section)
        for p in params:
            db[p[0]] = p[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db