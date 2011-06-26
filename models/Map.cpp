/**
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */

#include "Map.h"
namespace Models {

Map::Ptr Map::construct()
{
    Map::Ptr c(new Map());
    c->self = c;
    return c;
}

Map::Map() 
{
}

Map::~Map()
{
}

list<Edge::Ptr> Map::GetPath(Node::Ptr Source, Node::Ptr Dest)
{
}

void Map::Load(string database)
{
}

}
