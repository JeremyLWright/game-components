/**
 * @brief Agent Class for the Game Components
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef AGENT_MMR4JC51
#define AGENT_MMR4JC51
#include <stdint.h>
#include <tr1/memory>
#include <string>
namespace Models {

using std::string;


class Agent
{
    public:
        typedef std::tr1::shared_ptr<Agent> Ptr;
        typedef std::tr1::weak_ptr<Agent> WeakPtr;
        typedef enum {
            DEAD = 0,
            ALIVE,
        } eState;

        static Agent::Ptr construct();
        virtual ~Agent();
        void Modify_Health(int32_t points);
    private:
        Agent();
        Agent::WeakPtr self;
        uint32_t id;
        string name;
        uint32_t health;
        eState state;
        Inventory::Ptr inventory;
        Node::Ptr current_position;


};

}
#endif /* end of include guard: AGENT_MMR4JC51 */
