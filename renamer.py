import pandas as pd

# returns new df with renamed columns
def rename(df, table_name_str):
    old_cols = df.columns.values.tolist()
    new_cols = []
    for x in old_cols:
        a=x.lstrip(table_name_str)
        a = a.lstrip('\.')
        new_cols.append(a)
    to_pass = dict(zip(old_cols,new_cols))
    new_df = df.rename(columns=to_pass)
    return new_df

# new_snowman = rename(snowman_df, 'kt_users_customizing_snowman_binary')