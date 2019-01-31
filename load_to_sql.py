import pandas as pd
from sqlalchemy import create_engine
from new_scrape import stock_dict

rds_connection_string = "root:YOURPASSWORDHERE@127.0.0.1/scrape_db"
engine = create_engine(f'mysql://{rds_connection_string}')

scrape_df = pd.DataFrame.from_dict(stock_dict)
# scrape_df

scrape_df.to_sql(name='scrape_db', con=engine, if_exists='append', index=False)