#ifndef MAINWINDOW_HPP
#define MAINWINDOW_HPP

#include <QDialog>
#include <QVBoxLayout>
#include <QPushButton>
#include <QSpacerItem>
#include <QStackedWidget>

#include "hudspage.hpp"
#include "soundspage.hpp"


class MainWindow : public QDialog
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
};
#endif // MAINWINDOW_HPP
