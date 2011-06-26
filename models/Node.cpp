/**
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */

#include "Node.h"

namespace Models {
Node::Ptr Node::construct()
{
    Node::Ptr c(new Node());
    c->self = c;
    return c;
}

Node::Node() {}
Node::~Node() {}

}
