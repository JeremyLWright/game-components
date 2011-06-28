#include <gtest/gtest.h>
#include <limits.h>
#include "Graph.h"

using Practicum::Models::Graph;

TEST(Models, One)
{
    Graph::Ptr g = Graph::construct();

    g->addNode("Frodo");
    g->addNode("Gandalf");
    g->addNode("Pip");
    g->addNode("Strider");
    
    g->addDirectedEdge("Frodo", "Gandalf", 1);
    g->addDirectedEdge("Frodo", "Pip", 1);
    g->addDirectedEdge("Frodo", "Strider", 1);
    g->addDirectedEdge("Gandalf", "Pip", 1);
    g->addDirectedEdge("Pip", "Strider", 1);
}
