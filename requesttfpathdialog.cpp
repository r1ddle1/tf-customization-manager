#include "requesttfpathdialog.h"

RequestTfPathDialog::RequestTfPathDialog(QWidget *parent) : QDialog(parent)
{
    QVBoxLayout *main_layout = new QVBoxLayout();

    QLabel *label = new QLabel("Sorry but I don't know where TF2 is located. "
                               "Please type its location below");

    QHBoxLayout *h_layout = new QHBoxLayout();

    _line_edit = new QLineEdit();
    QPushButton *select_location_btn = new QPushButton("Select location");
    QPushButton *ok_btn = new QPushButton("Ok");

    connect(select_location_btn,
            &QPushButton::clicked,
            this,
            &RequestTfPathDialog::on_select_path_btn_clicked);

    connect(ok_btn,
            &QPushButton::clicked,
            this,
            &RequestTfPathDialog::on_ok_btn_clicked);

    h_layout->addWidget(_line_edit);
    h_layout->addWidget(select_location_btn);
    h_layout->addWidget(ok_btn);

    main_layout->addWidget(label);
    main_layout->addLayout(h_layout);

    setLayout(main_layout);
}

void RequestTfPathDialog::on_select_path_btn_clicked()
{
    QString path = QFileDialog::getExistingDirectory(
                this,
                tr("Select tf path"),
                "~/");

    _line_edit->setText(path);
}

void RequestTfPathDialog::on_ok_btn_clicked()
{
    if (is_tf_path(_line_edit->text())) {
        accept();
        return;
    }

    QMessageBox::critical(this,
                          "Error",
                          "Sorry but this path is not correct "
                          "('tf' folder should be in it)");
}
