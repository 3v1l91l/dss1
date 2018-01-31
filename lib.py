import pandas as pd
import os

def load_data(data_path='.'):
    costs_df = pd.read_csv(os.path.join(data_path, 'Costs.csv'), parse_dates=['date_created'], dayfirst=False)
    relations_df = pd.read_csv(os.path.join(data_path, 'Relations.csv'), usecols=['name', 'chanel', 'id_partner'])
    users_df = pd.read_csv(os.path.join(data_path, 'Users.csv'), 
                           usecols=['id', 'Reg_date', 'name', 'id_partner'], parse_dates=['Reg_date'], dayfirst=False)
    visits_df = pd.read_csv(os.path.join(data_path, 'Visits.csv'), parse_dates=['Visit_date'], dayfirst=False)
    orders_df = pd.read_csv(os.path.join(data_path, 'Orders.csv'), parse_dates=['Order Date'], dayfirst=False)

    return users_df, costs_df, relations_df, visits_df, orders_df