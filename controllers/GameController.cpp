#include "GameController.h"
#include "views/ConsoleView.h"
#include "models/SqliteDialogTreeModel.h"
#include "models/DialogTreeModel.h"
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
            Models::DialogTreeModel::Ptr dialogModel = Models::SqliteDialogTreeModel::construct(1);
            //Open the Game's Main View.
            View::ConsoleView::Ptr userView = View::ConsoleView::construct();
            string s;
            while(dialogModel->GetStatement(s))
            {
                userView->SendMessage(s);
            }
            //            userView->SendMessage("Welcome to the C++ Choose Your Own Adventure.");
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
