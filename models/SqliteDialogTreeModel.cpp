#include "SqliteDialogTreeModel.h"
#include <sstream>
#include <iostream>
extern "C" {
#include "sqlite3.h"
#include <stdio.h>
}
using std::cout;
using std::endl;
using std::stringstream;
using std::istringstream;
namespace {
    template <class T>
        bool from_string(T& t,
                const std::string& s,
                std::ios_base& (*f)(std::ios_base&))
        {
            std::istringstream iss(s, istringstream::in);
            return !(iss >> f >> t).fail();
        }
    char const * DB_NAME = "World.db";
    sqlite3* db_conn;

}


namespace Practicum {
    namespace Models {
        SqliteDialogTreeModel::SqliteDialogTreeModel(){}
        
        SqliteDialogTreeModel::SqliteDialogTreeModel(int treeIdx):
        _treeIdx(treeIdx)
        {
        }
        
        SqliteDialogTreeModel::~SqliteDialogTreeModel()
        {
            sqlite3_close(db_conn);
        }

        SqliteDialogTreeModel::Ptr SqliteDialogTreeModel::construct(int treeIdx)
        {
            int ret = sqlite3_open(DB_NAME, &db_conn);
            if(ret == SQLITE_OK)
            {
                cout << "Opened DB." << endl;
            }
            else
                cout << "Failed to open DB" << endl;
            SqliteDialogTreeModel::Ptr c(new SqliteDialogTreeModel(treeIdx));
            c->self = c;
            return c;

        }

        bool SqliteDialogTreeModel::GetStatement(string& dialog)
        {
            if(!_treeIdx)
                return false; 
        
                stringstream s;
                s << "SELECT * FROM dialog WHERE id=" << _treeIdx;
                const string& tmp = s.str();
                const char* query = tmp.c_str();
                sqlite3_stmt* compiled_query;
                char const* unused;
                sqlite3_prepare_v2(db_conn, query, tmp.size(), &compiled_query, &unused);
                s.clear();
        
            stringstream dialogStream;
            while(SQLITE_DONE != sqlite3_step(compiled_query))
            {
                _treeIdx = sqlite3_column_int(compiled_query, 2);
                dialogStream << sqlite3_column_text(compiled_query, 1);
            }
            sqlite3_finalize(compiled_query);
            dialog = dialogStream.str();
            return true;
        }

        string SqliteDialogTreeModel::GetOptions()
        {
            return "";
        }

    }
}
