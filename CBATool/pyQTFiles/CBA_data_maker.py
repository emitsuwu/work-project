import sqlite3
import pandas as pd
import sys
import os




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


scenario_path = resource_path('') + 'test.db'

dbConn = sqlite3.connect(scenario_path)


query = "SELECT part_id, part_name, part_cost FROM parts"



parts_df = pd.read_sql_query(query, dbConn)

part_ids = parts_df['part_id'].to_list()

part_names = parts_df['part_name'].to_list()

part_costs = parts_df['part_cost'].to_list()



print(part_ids)

print(part_names)

print(part_costs)

