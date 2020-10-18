#include "mainwindow.hpp"
#include "requesttfpathdialog.h"
#include "configmanager.h" // TODO: remove me plz if I'm in other already included shit

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    if (!ConfigManager::config_exists()) { // If there's no cfg file
        RequestTfPathDialog r;
        if (!r.exec()) {
            return -1;
        }
        QString tf_path = r.tf_path;
        std::cout << ConfigManager::set_value(TF_PATH_KEY, tf_path);
    }

    MainWindow w;
    w.show();

    return a.exec();
}
