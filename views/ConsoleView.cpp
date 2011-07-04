#include "ConsoleView.h"
#include <iostream>
using std::cout;
using std::endl;
using std::cin;
namespace Practicum {
    namespace View {
        ConsoleView::Ptr ConsoleView::construct()
        {
            ConsoleView::Ptr c(new ConsoleView());
            c->self = c;
            return c;
        }

        ConsoleView::ConsoleView(){}
        ConsoleView::~ConsoleView(){}
        void ConsoleView::SendMessage(string msg)
        {
            cout << msg << endl;
        }

        int ConsoleView::GetUserOption(vector<string> options)
        {
            int option_idx = 1;
            for(vector<string>::const_iterator i = options.begin();
                    i < options.end();
                    ++i, option_idx++)
            {
                cout << option_idx << ") " << *i << endl;
            }

            int selection;
            cout << "Choose: ";
            cin >> selection;
            return (selection-1);
        }

    }
}
