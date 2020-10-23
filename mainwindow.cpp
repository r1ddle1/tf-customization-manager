#include "mainwindow.hpp"

MainWindow::MainWindow(QWidget *parent)
    : QDialog(parent)
{
    setWindowTitle("Team Fortress Customization Manager");

    QVBoxLayout *main_layout = new QVBoxLayout();

    // Upper part
    QHBoxLayout *switch_buttons_layout = new QHBoxLayout();
    main_layout->addLayout(switch_buttons_layout);

    QPushButton *huds_button = new QPushButton("HUDs");
    QPushButton *sounds_button = new QPushButton("Sounds");
    QPushButton *cfgs_button = new QPushButton("CFGs");

    switch_buttons_layout->addItem(new QSpacerItem(40,
                                                   20,
                                                   QSizePolicy::Expanding));
    switch_buttons_layout->addWidget(huds_button);
    switch_buttons_layout->addWidget(sounds_button);
    switch_buttons_layout->addWidget(cfgs_button);
    switch_buttons_layout->addItem(new QSpacerItem(40,
                                                   20,
                                                   QSizePolicy::Expanding));

    // Lower part
    QStackedWidget *stacked_widget = new QStackedWidget();

    // Add pages to stacked widget
    auto huds_page = new HudsPage();
    auto sounds_page = new SoundsPage();
    auto cfgs_page = new CfgsPage();


    stacked_widget->addWidget(huds_page);
    stacked_widget->addWidget(sounds_page);
    stacked_widget->addWidget(cfgs_page);

    main_layout->addWidget(stacked_widget);

    setLayout(main_layout);

    // Connect switch buttons
    // I don't understand why '=' instead of '&' works
    // If you do know plz answer me using adress on my GH page
    connect(huds_button,
            &QPushButton::clicked,
            this,
            [=] () { stacked_widget->setCurrentIndex(0); });

    connect(sounds_button,
            &QPushButton::clicked,
            this,
            [=] () { stacked_widget->setCurrentIndex(1); });

    connect(cfgs_button,
            &QPushButton::clicked,
            this,
            [=] () { stacked_widget->setCurrentIndex(2); });

}

MainWindow::~MainWindow()
{
}

