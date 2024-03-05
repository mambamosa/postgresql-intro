import logging

from sqlalchemy import create_engine, MetaData, Table


def get_engine(conn_url: str):
    engine = create_engine(conn_url)

    return engine

def get_connection_url(user: str, passwd: str, host: str, port: int, db: str) -> str:
    return f"postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}"

    return conn_url

def main():
    # Create and get the connection URL.
    conn_url = get_connection_url(
        user="your_username",
        passwd="your_password",
        host="your_hostname",
        port=5432,
        db="postgres"
    )

    # Initialize the SQLAlchemy engine.
    logging.info("[SQLALCHEMY] Initializing SQLAlchemy engine configuration.")
    engine = get_engine(conn_url)
    logging.info("[SQLALCHEMY] Retrieving tables in PostgreSQL.")
    print(engine.table_names())

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
