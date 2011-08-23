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
    for exit in db[room]["Exits"].keys():
        if(db[room]["Exits"][exit] != ""):
            e = pydot.Edge(room, db[room]["Exits"][exit],label=str(exit))
            graph.add_edge(e)

graph.write_svg("mygraph.svg")

