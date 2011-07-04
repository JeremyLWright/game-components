/**
 * @brief Single View that implements the Console IO.
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef _CONSOLEVIEW
#define _CONSOLEVIEW

#include <string>
#include <vector>
#include <tr1/memory>
using std::string;
using std::vector;

namespace Practicum {
    namespace View {
        class ConsoleView
        {
            public:
                typedef std::tr1::shared_ptr<ConsoleView> Ptr;
                typedef std::tr1::weak_ptr<ConsoleView> WeakPtr;
                static ConsoleView::Ptr construct();
                virtual ~ConsoleView();
                /**
                 * Output a Message to the user.
                 */
                virtual void SendMessage(string msg);

                /**
                 * Output a set of options to the user, and wait for
                 * a response.
                 * @return The index of the option selected by the user.
                 */
                virtual int GetUserOption(vector<string> options);
            private:
                ConsoleView();
                ConsoleView::WeakPtr self;

        };

    }
}

#endif /* end of include guard: _CONSOLEVIEW */

