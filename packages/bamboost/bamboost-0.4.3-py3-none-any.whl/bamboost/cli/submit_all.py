from bamboost import Manager, Simulation
import sys


def submit_all(db):
    for sim in db:
        sim: Simulation
        if sim.metadata['submitted'] == False:
            sim.submit()


if __name__ == "__main__":

    db_path = str(sys.argv[1])
    db = Manager(db_path)
    submit_all(db)
