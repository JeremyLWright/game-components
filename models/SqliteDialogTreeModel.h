/**
 * @brief Sqlite Implementation of a Dialog Tree
 *
 * @par
 * Copyright Jeremy Wright (c) 2011
 * Creative Commons Attribution-ShareAlike 3.0 Unported License.
 */
#ifndef _SQLITEDIALOGTREEMODEL
#define _SQLITEDIALOGTREEMODEL

#include "DialogTreeModel.h"
#include <tr1/memory>

namespace Practicum {
    namespace Models {
        class SqliteDialogTreeModel : public DialogTreeModel
        {
        public:
            typedef std::tr1::shared_ptr<SqliteDialogTreeModel> Ptr;
            typedef std::tr1::weak_ptr<SqliteDialogTreeModel> WeakPtr;
            static SqliteDialogTreeModel::Ptr construct(int treeIdx);
            virtual ~SqliteDialogTreeModel();
            virtual bool GetStatement(string& dialog);
            virtual string GetOptions();
        private:
            SqliteDialogTreeModel();
            SqliteDialogTreeModel(int treeIdx);
            SqliteDialogTreeModel::WeakPtr self;
            int _treeIdx;
        };
    }
}

#endif /* end of include guard: _SQLITEDIALOGTREEMODEL */
