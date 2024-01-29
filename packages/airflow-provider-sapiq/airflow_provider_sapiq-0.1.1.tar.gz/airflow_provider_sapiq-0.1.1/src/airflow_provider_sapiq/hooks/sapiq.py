"""SAP IQ hook module."""
from __future__ import annotations

import sqlanydb

from airflow.providers.common.sql.hooks.sql import DbApiHook

class SapIQHook(DbApiHook):
    """Interact with SAP IQ."""

    DEFAULT_SQLALCHEMY_SCHEME = 'sqlalchemy_sqlany'
    conn_name_attr = 'sapiq_conn_id'
    default_conn_name = 'sapiq_default'
    conn_type = 'sapiq'
    hook_name = 'SAP IQ'
    supports_autocommit = True
    placeholder = "?"

    @staticmethod
    def get_ui_field_behaviour():
        """Returns custom field behaviour"""
        return {
            "hidden_fields": ["extra", "schema"],
            "relabeling": {
                "login": "User Id"
            },
            "placeholders": {
                "login": "guest",
                "password": "guest",
                "port": "2638",
                "host": "host",
            },
        }

    def get_conn(self) -> sqlanydb.Connection:
        """Return sap iq connection object"""
        conn = self.get_connection(self.sapiq_conn_id)  # type: ignore
        conn_config = {
            "userid": conn.login,
            "password": conn.password or '',
            "host": f'{conn.host}:{conn.port}',
        }
        conn = sqlanydb.connect(**conn_config)
        return conn

    def get_uri(self) -> str:
        """URI invoked in :py:meth:`~airflow.hooks.dbapi.DbApiHook.get_sqlalchemy_engine` method.

        Extract the URI from the connection.

        :return: the extracted uri.
        """
        from urllib.parse import quote_plus, urlunsplit
        conn = self.get_connection(getattr(self, self.conn_name_attr))
        login = ''
        if conn.login:
            login = f'{quote_plus(conn.login)}:{quote_plus(conn.password)}@'
        host = conn.host
        if conn.port is not None:
            host += f':{conn.port}'
        schema = conn.schema or ''
        uri = urlunsplit(
            (self.DEFAULT_SQLALCHEMY_SCHEME, f'{login}{host}', schema, '', ''))
        return uri
