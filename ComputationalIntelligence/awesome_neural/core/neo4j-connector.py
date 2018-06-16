from neo4j.v1 import GraphDatabase


class NeoConnector:
    def __init__(self):
        self._driver = GraphDatabase.driver(
            'bolt://localhost',
            auth=('neo4j', '1234')
        )