/**
 * @brief Top-Level entry point for movements in the game.
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */

#ifndef MAP_T37T36B0
#define MAP_T37T36B0

#include <list>
#include <string>
#include <tr1/memory>
#include "Edge.h"
#include "Node.h"
namespace Models {
using std::list;
using std::string;

class Map
{
public:
    typedef std::tr1::shared_ptr<Map> Ptr;
    typedef std::tr1::weak_ptr<Map> WeakPtr;
    static Map::Ptr construct();
    virtual ~Map();
    list<Edge::Ptr> GetPath(Node::Ptr Source, Node::Ptr Dest);
    void LoadMap(string database);
private:
    Map();
    Map::WeakPtr self;
    
};

}

#endif /* end of include guard: MAP_T37T36B0 */
