/**
 * @brief Encapsulate a graph edge for the Map.
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef EDGE_VC7WBFGP
#define EDGE_VC7WBFGP

#include <tr1/memory>
#include "Node.h"
namespace Models {
    
class Edge
{
public:
    typedef std::tr1::shared_ptr<Edge> Ptr;
    typedef std::tr1::weak_ptr<Edge> WeakPtr;
    static Edge::Ptr construct();
    virtual ~Edge();
private:
    Edge();
    Edge::WeakPtr self;
    Node::Ptr destination;
};
}

#endif /* end of include guard: EDGE_VC7WBFGP */

