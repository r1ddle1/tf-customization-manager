#include "mainwindow.hpp"
#include "requesttfpathdialog.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

/*    if (!false) { // if there's no cfg file (work in progress)
        RequestTfPathDialog r;
        if (!r.exec()) {
            return -1;
        }
        QString tf_path = r.tf_path;
    }
    else  { */
        MainWindow w;
        w.show();
    // }

    return a.exec();
}
