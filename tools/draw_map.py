import pydot
import sqlite3
import sys
import json

modelName = sys.argv[1]
data = open(modelName, "r")
db = json.load(data)
data.close()


graph = pydot.Dot('graphname', graph_type='digraph')

for room in db.keys():
    if(db[room]["Exits"]["East"] != ""):
        e = pydot.Edge(room, db[room]["Exits"]["East"],label=str("East"))
        graph.add_edge(e)
    if(db[room]["Exits"]["West"] != ""):
        e = pydot.Edge(room, db[room]["Exits"]["West"],label=str("West"))
        graph.add_edge(e)
    if(db[room]["Exits"]["North"] != ""):
        e = pydot.Edge(room, db[room]["Exits"]["North"],label=str("North"))
        graph.add_edge(e)
    if(db[room]["Exits"]["South"] != ""):
        e = pydot.Edge(room, db[room]["Exits"]["South"],label=str("South"))
        graph.add_edge(e)

graph.write_svg("mygraph.svg")

