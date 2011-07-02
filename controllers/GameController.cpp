#include "GameController.h"
#include "views/ConsoleView.h"
namespace Practicum {
    namespace Controller {
        GameController::Ptr GameController::construct()
        {
            GameController::Ptr c(new GameController());
            c->self = c;
            return c;
        }

        GameController::GameController() {}
        GameController::~GameController() {}

        void GameController::Run()
        {
            //Open the Game's Models
            
            //Open the Game's Main View.
            View::ConsoleView::Ptr userView = View::ConsoleView::construct();
            userView->SendMessage("Welcome to the C++ Choose Your Own Adventure.");
            vector<string> menu;
            menu.push_back("Load Game.");
            menu.push_back("Quit");
            do {
                if(userView->GetUserOption(menu) == 1)
                    return;
            } while(1);

            return;

        }
    }
}
