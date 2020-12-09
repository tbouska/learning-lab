#!/usr/bin/env python3
# server.py
from ariadne import gql, QueryType, make_executable_schema, ObjectType, load_schema_from_path
from ariadne.asgi import GraphQL
import uvicorn

type_defs = load_schema_from_path("ariadne_intro/schema/")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return f"Hello, {user_agent}"

class User():
    def __init__(self, username, name):
        self.username = username
        self.name = name
        self.type = ObjectType("User")
        self.type.set_field("username", lambda _,info: self.username)
        self.type.set_field("name", lambda _,info: self.name)


bob = User("bob", "Tomas Bouska")
query.set_field("user", lambda _,info: bob.type)

schema = make_executable_schema(type_defs, query, bob.type)
app = GraphQL(schema, debug=True)

def main():
    uvicorn.run("ariadne_intro.server:app", host="127.0.0.1", port=5000)
