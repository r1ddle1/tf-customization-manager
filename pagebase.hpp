#ifndef PAGEBASE_HPP
#define PAGEBASE_HPP

#include <QWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QScrollArea>

#include <iostream>

class PageBase : public QWidget
{
    Q_OBJECT
public:
    PageBase(QString browser_name);
    virtual ~PageBase();

    virtual void on_refresh_db_clicked() = 0;

protected:
    QLabel *_last_refresh_label;
    QVBoxLayout *_options_layout;
    QScrollArea *_scroll_area;

    std::vector<QWidget*> _pages;
    int _current_page_index = 0;

    void on_go_back_button_pressed();  // <-
    void on_go_forward_button_pressed();  // ->

private:
    QLabel *_current_page_label;

    void create_options_part(QHBoxLayout* main_layout);
    void create_browser_part(QHBoxLayout* main_layout, QString &browser_name);
};

#endif // PAGEBASE_HPP
