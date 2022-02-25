import pandas as pd
from find_sds.find_sds import find_sds



if __name__ == '__main__':
    chemical_inventory = "C:\\Users\\gauer\\Box\\TEAM ENGINEERING\\Inventory\\Inventory_solvent_cabinet.xlsx"

    df = pd.read_excel(chemical_inventory,  sheet_name='Sheet1', usecols=['CAS'], keep_default_na=False)
    df = pd.read_excel(chemical_inventory,  sheet_name='Sheet1', keep_default_na=False)
    cas_list = df['CAS'].tolist()
    # using list comprehension to perform removal of emptiness
    cas_list = [i for i in cas_list if i]

    print(cas_list)
    # cas_list = ['141-78-6', '110-82-7', '67-63-0']
    download_path = 'SDS'
    find_sds(cas_list=cas_list, download_path=download_path, pool_size=10)

# impossible approch, find CAS for each chemical - problem: multiple CAS per product, or no CAS at all
# if __name__ == '__main__':
#     import cirpy #https://cirpy.readthedocs.io/en/latest/
#     from cirpy import Molecule
#     mol = Molecule('acetone')
#     print(mol.cas)

#     chemical_inventory = "C:\\Users\\gauer\\Box\\TEAM ENGINEERING\\Inventory\\Inventory_solvent_cabinet.xlsx"
#     df = pd.read_excel(chemical_inventory,  sheet_name='Sheet1', keep_default_na=False)

#     # df['Normalized'] = np.where(df['Currency'] == '$', df['Budget'] * 0.78125, df['Budget'])
#     import numpy as np
#     # df['CAS cirpy'] = df['CAS']
#     df['CAS cirpy'] = ''
#     # df.loc[df['Product']] = Molecule(df['Product']).cas
#     # df.loc[df['Product']] = Molecule('acetone').cas
#     print(df)

#     # df['SDS cirpy'].fillna(Molecule(df['Product']).cas)
#     # df['CAS'].fillna(df['Product'])
#     print(df['CAS'][29])
#     print(df['Product'][29])
#     print(Molecule(df['Product'][26]).cas)

#     for index, row in df.iterrows():
#         print(row['Product'], row['CAS cirpy'])
#         if not row['CAS cirpy']:
#             print('empty')
#             try:
#                 row['CAS cirpy'] = Molecule(row['Product']).cas
#                 print(row['CAS cirpy'])
#             except:
#                 print('this did not work')

#     print(df)
