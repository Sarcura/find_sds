import pandas as pd
from find_sds.find_sds import find_sds

chemical_inventory = "C:\\Users\\gauer\\Box\\TEAM ENGINEERING\\Inventory\\Inventory_solvent_cabinet.xlsx"

df = pd.read_excel(chemical_inventory,  sheet_name='Sheet1', usecols=['CAS'], keep_default_na=False)
cas_list = df['CAS'].tolist()
# using list comprehension to perform removal of emptiness
cas_list = [i for i in cas_list if i]

print(cas_list)
# cas_list = ['141-78-6', '110-82-7', '67-63-0']
download_path = 'SDS'

if __name__ == '__main__':
    find_sds(cas_list=cas_list, download_path=download_path, pool_size=10)