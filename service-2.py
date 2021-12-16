from sys import stderr

import pandas as pd
from sqlalchemy import create_engine, orm

from region import Base, Region


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@database:3306/db')
    session = orm.Session(engine)
    Base.metadata.create_all(engine)

    df = pd.read_csv('/resources/regions.csv')
    for _, row in df.iterrows():
        region = Region(id=row["id"], name= row["name"], population=row["population"])
        session.add(region)
    session.commit()

    print('Rows added. Now table contains:', file=stderr)
    for region in session.query(Region).all():
        print(f' - id={region.id}, name="{region.name}", '
              f'population={region.population}', file=stderr)
