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
    string DIALOG_QUERY(int id) 
    {
        stringstream query;
        query << "SELECT * FROM dialog where id=";
        query << id;
        return query.str();

    }
    sqlite3* db_conn;
    int lock;
    int nextStatementId;
    stringstream statement;

    int callback(void* unused ,int argc,char** argv ,char** colName)
    {
         int i;
         statement.clear();
         statement << argv[1];
         from_string<int>(nextStatementId, argv[0], std::dec);
         for(i=0; i<argc; i++)
         {
             printf("%s = %s\n", colName[i], argv[i] ? argv[i] : "NULL");
         }
         printf("\n");
         lock = 0;
         return 0;
    }


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
            lock = 0;
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

        string SqliteDialogTreeModel::GetStatement()
        {
            lock = 1;
            {
                stringstream s;
                s << "SELECT * FROM dialog where id=" << _treeIdx;
                const string& tmp = s.str();
                const char* query = tmp.c_str();
            char * zErrMsg;
            int rc = sqlite3_exec(db_conn, query, callback, 0,&zErrMsg);
            if(rc != SQLITE_OK)
                cout << zErrMsg << endl;
            else
                while(lock == 1); //Wait for the callback to complete. 
            }

            return statement.str();
        }

        string SqliteDialogTreeModel::GetOptions()
        {
            return "";
        }

    }
}
