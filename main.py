from ApiConn import sf
from SqlConn import sqlcon
from pokeAPI import df
import pandas as pd

# df.to_sql('[wtf]', sqlcon, index=False, if_exists="append", schema="carson")

# data grabber
sf_data = sf.query_all("SELECT * from your own source")
#into a dataframe
sf_df = pd.DataFrame(sf_data)
# data giver(to sql)
sf_df.to_sql('[your table name]', sqlcon, index=False, if_exists="append", schema="your schema name")

