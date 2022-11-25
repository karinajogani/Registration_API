from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://ecwojjnmttzbnk:9899f8bd09a3bea7a3686cd72630236682be048788a7adea56e072719a822923@ec2-52-21-136-176.compute-1.amazonaws.com:5432/d50qft23533lgl",
                       echo=True
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()