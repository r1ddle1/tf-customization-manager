#ifndef PAGEBASE_HPP
#define PAGEBASE_HPP

#include <QWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QScrollArea>

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

private:
    void create_options_part(QHBoxLayout* main_layout);
    void create_browser_part(QHBoxLayout* main_layout, QString &browser_name);
};

#endif // PAGEBASE_HPP
