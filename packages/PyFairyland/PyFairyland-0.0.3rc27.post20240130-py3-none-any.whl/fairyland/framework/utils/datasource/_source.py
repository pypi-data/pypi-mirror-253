# coding: utf8
""" 
@File: _source.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-12
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import typing
import types
from typing import Union, Any, Callable
import pymysql
import psycopg2
from dotenv import load_dotenv

from fairyland.framework.modules.journal import Journal

load_dotenv()
_DATASOURCE = os.getenv("DATASOURCE", "MySQL")


class BaseDataSource:
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        """
        Initialize datasource info.
            初始化数据源信息。
        @param host: Database host address. | 数据库主机地址
        @type host: str
        @param port: Database port. | 数据库端口
        @type port: int
        @param user: Database username. | 数据库用户名
        @type user: str
        @param password: Database password. | 数据库密码
        @type password: str
        @param database: Database name to connect to. | 要连接的数据库名称
        @type database: str
        """
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database
        self.__connect: Union[
            pymysql.connections.Connection,
            psycopg2.extensions.connection,
            None,
        ]
        self.__cursor: Union[
            pymysql.cursors.Cursor,
            psycopg2.extensions.cursor,
            None,
        ]
        # self._init_connect()

    def _connect(self, default: bool = False) -> Union[pymysql.connections.Connection, psycopg2.extensions.connection]:
        """
        Initialize datasource connection.
            初始化连接
        @return: Database Connect Object. | 数据库连接对象
        @rtype: DataBase Object. | 数据库连接对象
        """
        if default:
            try:
                connect = pymysql.connect(
                    host=self._host,
                    port=self._port,
                    user=self._user,
                    password=self._password,
                    database=self._database,
                    charset="utf8mb4",
                    connect_timeout=10,
                )
                Journal.success("MySQL Connect: OK")
            except Exception as error:
                Journal.error(error)
                raise
            return connect
        else:
            raise NotImplementedError

    def _init_connect(self, default: bool = False) -> None:
        """
        Initialize datasource connection and create the database cursor.
            初始化连接并创建游标
        @return: None
        @rtype: None
        """
        self.__connect = self._connect(default=default)
        self.__cursor = self.__connect.cursor()

    def __connect_cursor(
        self,
    ) -> Union[pymysql.cursors.Cursor, psycopg2.extensions.cursor]:
        """
        Create the database cursor.
            创建数据库游标
        @return: DataBase Cursor Object. | 数据库游标对象
        @rtype: DataBase Cursor Object. | 数据库游标对象
        """
        return self.__connect.cursor()

    def __close_connect(self) -> None:
        """
        Close the database connection.
            关闭数据库连接。
        """
        if self.__connect:
            self.__connect.close()
            self.__connect = None
            Journal.debug("Database has been disconnected.")

    def __close_cursor(self) -> None:
        """
        Close the database cursor.
            关闭数据库游标。
        """
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
            Journal.debug("Database has disconnected the cursor.")

    def __reconnect(self) -> None:
        """
        Reconnect to the database.
            重连数据库。
        """
        if not self.__connect or not self.__cursor:
            Journal.debug("Wait for Database to reconnect.")
            if self.__connect and self.__cursor:
                self.__close_cursor()
                self.__cursor = self.__connect.cursor()
                Journal.debug("Database cursor has been reset.")
            elif self.__connect and not self.__cursor:
                self.__cursor = self.__connect.cursor()
                Journal.debug("Database cursor is connected.")
            elif not self.__connect and not self.__cursor:
                self.__connect = self._connect()
                self.__cursor = self.__connect_cursor()
                Journal.warning("Database has been reconnected.")

    def __close(self) -> None:
        """
        Completely close the database connection and cursor.
            完全关闭数据库连接和游标。
        """
        if self.__connect and self.__cursor:
            self.__close_cursor()
            self.__close_connect()
            Journal.warning("Database has been disconnected the all.")
        elif self.__connect and not self.__cursor:
            self.__close_connect()
            Journal.warning("Database has been disconnected the all.")

    def __trace_sql_statement(self, query, args) -> str:
        """
        Generate and return a debug SQL statement.
            生成并返回调试SQL语句。
        @param query: SQL query statement. | SQL查询语句
        @type query: str
        @param args: SQL query parameters. | SQL查询参数
        @type args: Union[tuple, list, dict, None]
        @return: Debug information. | 调试信息
        @rtype: str
        """
        return f"SQL -> {query} | Parameters -> {args}"

    def __operation(
        self,
        query: Union[str, tuple, list, set],
        parameters: Union[tuple, list, dict, None] = None,
    ) -> Union[tuple[tuple[Any], ...]]:
        """
        Execute SQL operations.
            执行 SQL 操作。
        @param query: SQL statement(s). SQL语句
        @type query: Union[str, tuple, list, set]
        @param parameters: SQL parameters. | SQL参数
        @type parameters: Union[tuple, list, dict, None]
        @return: Operation result. | 操作结果
        @rtype: Depends on the SQL operation
        """
        try:
            self.__reconnect()
            if isinstance(query, str):
                Journal.trace(self.__trace_sql_statement(query, parameters))
                if _DATASOURCE == "MySQL":
                    self.__cursor.execute(query=query, args=parameters)
                elif _DATASOURCE == "PostgreSQL":
                    self.__cursor.execute(query=query, vars=parameters)
                results = self.__cursor.fetchall()
            elif isinstance(query, (tuple, list, set)):
                results_list = []
                for query_str, query_parameters in zip(query, parameters):
                    Journal.trace(self.__trace_sql_statement(query_str, query_parameters))
                    if _DATASOURCE == "MySQL":
                        self.__cursor.execute(query=query_str, args=query_parameters)
                    elif _DATASOURCE == "PostgreSQL":
                        self.__cursor.execute(query=query_str, vars=query_parameters)
                    results_list.append(self.__cursor.fetchall())
            else:
                raise TypeError("Wrong SQL statement type.")
            self.__connect.commit()
        except Exception as error:
            Journal.debug("Failed to execute the rollback")
            self.__connect.rollback()
            Journal.error(error)
            raise
        finally:
            self.__close_cursor()
        return results if "results" in locals() else tuple(results_list)

    def execute(
        self,
        sql: Union[str, tuple, list, set],
        parameters: Union[tuple, list, dict, None] = None,
    ) -> Union[tuple[tuple[Any], ...], None]:
        """
        Execute single or multiple SQL statements.
            执行单个或多个 SQL 语句。
        @param sql: SQL statement or a set of statements. | SQL语句或语句集
        @type sql: Union[str, tuple, list, set]
        @param parameters: Parameters for the SQL statement(s). | SQL语句的参数
        @type parameters: Union[tuple, list, dict, None]
        @return: Execution result. | 执行结果
        @rtype: Depends on the SQL operation
        """
        if not isinstance(sql, str) and isinstance(sql, (list, tuple, set)) and not parameters:
            parameters = tuple([None for _ in range(len(sql))])
        return self.__operation(query=sql, parameters=parameters)

    def close(self):
        """
        Close the database connection and cursor.
            关闭数据库连接和游标。
        """
        self.__close()
