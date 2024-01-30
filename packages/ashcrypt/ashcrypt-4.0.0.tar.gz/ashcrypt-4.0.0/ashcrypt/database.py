"""Module to interact with an SQLite database"""

import os
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime
from typing import Generator, Optional, Union


@dataclass
class Database:
    """
    Represents an SQLite database class with various methods to interact with a given database.
    """

    dbname: str = field()
    tablename: Optional[str] = field(default="Classified")
    _conn: sqlite3.Connection = field(init=False, repr=False)
    _c: sqlite3.Cursor = field(init=False, repr=False)

    def __post_init__(self):
        self._conn = sqlite3.connect(self.dbname)
        self._c = self._conn.cursor()
        self.addtable()

    @property
    def size(self) -> Union[int, tuple]:
        """Returns the database size in MB"""
        try:
            with self._conn:
                self._c.execute(
                    "SELECT page_count * page_size FROM pragma_page_count() , pragma_page_size"
                )
                size_info = self._c.fetchone()
                size = size_info[0] / 1024 / 1024
                return size
        except sqlite3.Error as e:
            return -1, e

    @property
    def last_mod(self) -> Union[datetime, tuple]:
        """Returns the last time the Database has been altered with"""
        try:
            time_stat = datetime.fromtimestamp(os.stat(self.dbname).st_mtime)
            return time_stat

        except OSError as e:
            return -1, e

    @property
    def default_routing(self) -> str:
        """Get the default routing information of the Database class."""
        return self.tablename

    @default_routing.setter
    def default_routing(self, tablename: str):
        """Setter method to set the current table name to operate on
        if the table has been added to the database then it will switch to it,
         else it will pass"""
        tables = [tab[0] for tab in self.show_tables()]
        if tablename in tables:
            self.tablename = tablename

    def query(self, *querys: str) -> list:
        """Executes one or more SQL queries and return the results.
        Provides feedback on whether each given query ran successfully or not.
        Also provides where the Error has occurred and what type of Error it is."""
        result = []
        for i, query in enumerate(querys):
            if not isinstance(query, str):
                result.append({f"query {i}": (-1, TypeError)})
            try:
                with self._conn:
                    self._c.execute(query)
                    if self._c.rowcount == 1:
                        result.append({f"query {i}": ["SUCCESS", self._c.fetchone()]})
                    else:
                        result.append({f"query {i}": ["SUCCESS", self._c.fetchall()]})

            except sqlite3.Error as e:
                result.append({f"query {i}": ("FAILURE", e.__str__())})
        return result

    def addtable(self, tablename: Optional[str] = None) -> Union[int, tuple]:
        """Creates a new table in the database with the given table name.
        If the table name is not provided, it uses the default table name  : 'Classified'.
        """
        if tablename is None:
            try:
                with self._conn:
                    self._c.execute(
                        f"CREATE TABLE IF NOT EXISTS {self.tablename} "
                        "(ID INTEGER PRIMARY KEY, Name Text , Content BLOB ,Key TEXT )"
                    )
                return 1
            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(
                        f"CREATE TABLE IF NOT EXISTS {tablename} "
                        "(ID INTEGER PRIMARY KEY,"
                        "Name TEXT ,"
                        "Content BLOB ,"
                        "Key TEXT )"
                    )
                    self.tablename = tablename
                return 1

            except sqlite3.Error as e:
                return -1, e

    def insert(
        self,
        name: str,
        content: Union[bytes, str],
        key: str = "STANDALONE",
        tablename: Optional[str] = None,
    ) -> Union[int, tuple]:
        """Inserts a new row into the specified table or the default table."""
        if tablename is None:
            try:
                with self._conn:
                    self._c.execute(
                        f"INSERT INTO {self.tablename} (Name , Content ,Key) VALUES (? , ? , ?) ",
                        (name, content, key),
                    )

                return 1
            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(
                        f"INSERT INTO {tablename} (Name, Content ,Key) VALUES (? , ? , ?) ",
                        (name, content, key),
                    )
                return 1
            except sqlite3.Error as e:
                return -1, e

    def update(
        self,
        column_name: str,
        new_column_val: str,
        id_: int,
        tablename: Optional[str] = None,
    ) -> Union[int, tuple]:
        """Updates a specific column of a row based on the given ID in the specified table or the default table."""
        if tablename is None:
            try:
                with self._conn:
                    self._c.execute(
                        f"UPDATE {self.tablename} SET {column_name} = ? WHERE ID = ? ",
                        (new_column_val, id_),
                    )
                    return 1

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(
                        f"UPDATE {tablename} SET {column_name} = ? WHERE ID = ? ",
                        (new_column_val, id_),
                    )
                    return 1

            except sqlite3.Error as e:
                return -1, e

    def content(self, tablename: Optional[str] = None) -> Union[Generator, tuple]:
        """Yields all rows from the specified table or the default table
        if no arguments are passed ( as a Generator object ) ."""
        if tablename is None:
            try:
                with self._conn:
                    self._c.execute(f"SELECT * FROM {self.tablename} ")
                    for row in self._c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(f"SELECT * FROM {tablename} ")
                    for row in self._c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return -1, e

    def content_by_id(
        self, id_: int, tablename: Optional[str] = None
    ) -> Union[Generator, tuple]:
        """Yields a specific row from the specified table or the default table based on a given ID.
        ( Generator object )"""
        if tablename is None:
            try:
                with self._conn:
                    self._c.execute(
                        f"SELECT * FROM {self.tablename} WHERE ID = ? ", (id_,)
                    )
                    for row in self._c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(f"SELECT * FROM {tablename} WHERE ID = ? ", (id_,))
                    for row in self._c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return -1, e

    def show_contents(self, *tablenames: str) -> Union[Generator, tuple]:
        """Yields all rows from specified tables or the default table.
        ( Generator object )"""
        if tablenames:
            try:
                for arg in tablenames:
                    with self._conn:
                        self._c.execute(f"SELECT * FROM {arg} ")
                        for row in self._c.fetchall():
                            yield {arg: row}

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(f"SELECT * FROM {self.tablename} ")
                    for row in self._c.fetchall():
                        yield {self.tablename: row}

            except sqlite3.Error as e:
                return -1, e

    def show_tables(self) -> Union[Generator, tuple]:
        """Yields the names of all tables in the Database. ( Generator object )"""
        try:
            with self._conn:
                self._c.execute("SELECT name FROM sqlite_master WHERE type= 'table' ")
                for row in self._c.fetchall():
                    yield row

        except sqlite3.Error as e:
            return -1, e

    def dropall(self) -> Union[int, tuple]:
        """Drops ALL tables in the Database."""
        try:
            with self._conn:
                self._c.execute("SELECT name FROM sqlite_master WHERE type= 'table' ")
                for table in self._c.fetchall():
                    self._c.execute(f"DROP TABLE {table[0]}")
                return 1

        except sqlite3.Error as e:
            return -1, e

    def drop_table(self, *tablenames: str) -> Union[int, tuple]:
        """Drops a/many specific table(s) in the Database."""
        if tablenames:
            try:
                for arg in tablenames:
                    with self._conn:
                        self._c.execute(f"DROP TABLE {arg}")
                return 1
            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(f"DROP TABLE {self.tablename}")
                    return 1

            except sqlite3.Error as e:
                return -1, e

    def drop_content(
        self, id_: int, tablename: Optional[str] = None
    ) -> Union[int, tuple]:
        """Deletes a row from the specified table or the default table based on the given ID."""
        if tablename is None:
            try:
                with self._conn:
                    self._c.execute(f"DELETE FROM {self.tablename} WHERE ID = {id_}")
                return 1

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self._conn:
                    self._c.execute(f"DELETE FROM {tablename} WHERE ID = {id_}")
                return 1

            except sqlite3.Error as e:
                return -1, e
