from silx.gui import qt as Qt


class GroupBox(Qt.QGroupBox):
    def __init__(self, *args, **kwargs):
        super(GroupBox, self).__init__(*args, **kwargs)
        self.setStyleSheet(
            """
            GroupBox {
               border: 2px solid gray;
               margin-top: 2ex;
               border-radius: 5px
            }

            GroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                background-color:
                    qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 lightgray, stop: 1 gray);
                border-radius: 5px;
            }
            """
        )


class SubGroupBox(Qt.QGroupBox):
    def __init__(self, *args, **kwargs):
        super(SubGroupBox, self).__init__(*args, **kwargs)
        self.setStyleSheet(
            """
            SubGroupBox {
               border: 1px inset gray;
               border-radius: 2px;
               padding-top: 3.5ex;
            }

            SubGroupBox::title {
                subcontrol-origin: padding;
                subcontrol-position: top left;
                border-radius: 0px;
                border: 1px outset gray;
                background-color:
                    qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 gray, stop: 1 lightgray);
            }
            """
        )
