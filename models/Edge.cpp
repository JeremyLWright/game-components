/**
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#include "Edge.h"

namespace Models {

Edge::Ptr Edge::construct()
{
    Edge::Ptr c(new Edge());
    c->self = c;
    return c;
}

Edge::Edge(){}
Edge::~Edge(){}

}

