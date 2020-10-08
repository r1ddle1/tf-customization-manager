#ifndef REQUESTTFPATHDIALOG_H
#define REQUESTTFPATHDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QVBoxLayout>
#include <QLineEdit>
#include <QFileDialog>
#include <QLabel>
#include <QMessageBox>

#include "utils.hpp"
#include <iostream>

class RequestTfPathDialog : public QDialog
{
    Q_OBJECT
public:
    explicit RequestTfPathDialog(QWidget *parent = nullptr);
    QString tf_path;

signals:

private:
    QLineEdit *_line_edit;
    void on_select_path_btn_clicked();
    void on_ok_btn_clicked();
};

#endif // REQUESTTFPATHDIALOG_H
