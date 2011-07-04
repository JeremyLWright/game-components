/**
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#include "Graph.h"

namespace Practicum {
    namespace Models {
        Graph::Ptr Graph::construct()
        {
            Graph::Ptr c(new Graph());
            c->self = c;
            return c;
        }

        Graph::Graph(){}
        Graph::~Graph(){}

        void Graph::addDirectedEdge(string fromNode, string toNode, int32_t weight)
        {
            adjacencyList[fromNode].push_back(Node(toNode, weight));
        }

        void Graph::addNode(string nodeName)
        {
            adjacencyList[nodeName] = list<Node>(); //Insert an empty list to the graph.
        }

    }
}
