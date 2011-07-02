/**
 * @brief Entry Point for Game Componenets
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */

#include "views/ConsoleView.h"
#include <vector>
#include <string>
using std::string;
using std::vector;
using namespace Practicum;

int main(int argc, const char *argv[])
{
    View::ConsoleView::Ptr userConsole = View::ConsoleView::construct();
    userConsole->SendMessage("Welcome to the C++ Choose Your Own Adventure.");
    vector<string> menu;
    menu.push_back("Load Game.");
    menu.push_back("Quit");
    do {
        if(userConsole->GetUserOption(menu) == 1)
        return 0;
    } while(1);


    return 0;
}
