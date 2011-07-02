/**
 * @brief Start-up controller for the Game
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef _GAMECONTROLLER
#define _GAMECONTROLLER
#include <tr1/memory>
namespace Practicum {
    namespace Controller {
        class GameController
        {
            public:
                typedef std::tr1::shared_ptr<GameController> Ptr;
                typedef std::tr1::weak_ptr<GameController> WeakPtr;
                static GameController::Ptr construct();
                virtual ~GameController();
                virtual void Run();
            private:
                GameController();
                GameController::WeakPtr self;

        };
    }
}
#endif /* end of include guard: _GAMECONTROLLER */
