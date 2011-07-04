/**
 * @brief A Simple Graph implemented with an adjency list.
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */

#ifndef GRAPH_80KJSEOO
#define GRAPH_80KJSEOO
#include <string>
#include <stdint.h>
#include <tr1/memory>
#include <list>
#include <map>

using std::string;
using std::map;
using std::list;

namespace Practicum {
    namespace Models {
        class Graph
        {
        public:
            typedef std::tr1::shared_ptr<Graph> Ptr;
            typedef std::tr1::weak_ptr<Graph> WeakPtr;
            static Graph::Ptr construct();
            virtual ~Graph();
            void addDirectedEdge(string fromNode, string toNode, int32_t weight);
            void addNode(string nodeName);
        private:
            struct Node {
                Node(){}
                Node(string name, int32_t weight):
                    Name(name),
                    Weight(weight) 
                {
                }
                string Name;
                int32_t Weight;
            };
            Node nilNode;
            map<string, list<Node> > adjacencyList;
            Graph();
            Graph::WeakPtr self;
        
        };
    }
}


#endif /* end of include guard: GRAPH_80KJSEOO */

