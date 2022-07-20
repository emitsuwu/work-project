import sqlite3
import pandas as pd
import sys
import os



class Connection(object):
    def __init__(self):
        scenario_path = resource_path('') + 'test.db'

        self.dbConn = sqlite3.connect(scenario_path)

def resource_path(relative_path):
    """
        returns the path to a file by combining
        the relative path to the base path
        Args:
            relative path (str): relative path to a resource file
        Returns:
            os.path.join(path):
                full path to resource file
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, relative_path)
    return os.path.join(path)

connections = Connection()


def get_cba_part_data(part_name):


    query = f"SELECT part_id, part_cost FROM parts WHERE part_name = '{part_name}'"



    parts_df = pd.read_sql_query(query, connections.dbConn)



    print(parts_df)


    return parts_df


def get_cba_parts_list():


    query = f"SELECT part_name FROM parts "



    part_names_df = pd.read_sql_query(query, connections.dbConn)

    part_names_list = part_names_df['part_name'].to_list()

    return part_names_list

# get_cba_part_data("Leaf Part")
