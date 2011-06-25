import pydot
import sqlite3

conn = sqlite3.connect('../models/World.db')

graph = pydot.Dot('graphname', graph_type='digraph')
nodes = conn.cursor()
nodes.execute('''select id from nodes''')
for node in nodes:
    c = conn.cursor()
    c.execute('''select FR.id, '-->', T.id
                from edges 
                join nodes  FR on FR.id=edges.from_node_id
                join nodes  T on T.id=edges.to_node_id
                where edges.from_node_id = %d;'''%(node))
    for row in c:
        graph.add_edge(pydot.Edge(str(row[0]), str(row[2])))

graph.write_png("mygraph.png")

