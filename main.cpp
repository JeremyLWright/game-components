/**
 * @brief Entry Point for Game Componenets
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */

#include "controllers/GameController.h"
using namespace Practicum;

int main(int argc, const char *argv[])
{
    Controller::GameController::Ptr game = Controller::GameController::construct();
    game->Run();
    return 0;
}
