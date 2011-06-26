/**
 * @brief Encasulate a Node for the Map Graph
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef NODE_PJF8JRFC
#define NODE_PJF8JRFC

#include <tr1/memory>
#include <list>
#include "Edge.h"
namespace Models {
using std::list;

class Node
{
public:
    typedef std::tr1::shared_ptr<Node> Ptr;
    typedef std::tr1::weak_ptr<Node> WeakPtr;
    static Node::Ptr construct();
    virtual ~Node();
private:
    Node();
    Node::WeakPtr self;
    list<Edge::Ptr> edges;

};
}

#endif /* end of include guard: NODE_PJF8JRFC */
