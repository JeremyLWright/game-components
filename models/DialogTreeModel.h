/**
 * @brief Encapsulate a Dialog Tree Loaded from the Database.
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef _DIALOGTREEMODEL
#define _DIALOGTREEMODEL
#include <tr1/memory>
#include <string>
using std::string;

namespace Practicum {
    namespace Models {
        class DialogTreeModel
        {
            public:
            typedef std::tr1::shared_ptr<DialogTreeModel> Ptr;
            typedef std::tr1::weak_ptr<DialogTreeModel> WeakPtr;
                virtual string GetStatement() = 0;
                virtual string GetOptions() = 0;
            private:

        };
    }
}

#endif /* end of include guard: _DIALOGTREEMODEL */
