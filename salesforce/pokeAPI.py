import pokebase
import requests
import json
import pandas as pd

# def main():
resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
x = json.loads(resp.text)
# (x["abilities"])
df = pd.DataFrame((x["abilities"])) 
# print(df)
    

# if __name__ == '__main__':
#     main()

# def main():
#     resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
#     x = json.loads(resp.text)
#     # (x["abilities"])
#     df = pd.DataFrame((x["abilities"])) 
#     df.to_sql('[wtf]', sqlcon, index=False, if_exists="append", schema="carson")
#     # print(df)
    

# if __name__ == '__main__':
#     main()