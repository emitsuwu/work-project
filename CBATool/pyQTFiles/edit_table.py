from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re

class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor

class Model(QAbstractTableModel):
    ActivateRole = Qt.UserRole + 1

    def __init__(self, datain, headerdata, row_names, parent=None):
        """
        Args:
            datain: a list of lists\n
            headerdata:a list of strings
        """
        super().__init__()
        self.arraydata = datain
        self.headerdata = headerdata
        self.row_names = row_names

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return QVariant(self.headerdata[section])
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(self.row_names[section])
        return QVariant()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid(): return 0
        return len(self.arraydata)

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role=Qt.EditRole):
        r = re.compile(r"^[0-9]\d*(\.\d+)?$")
        if role == Qt.EditRole and value != "" and 0 < index.column() < self.columnCount():
            if index.column() in (0, 1):
                self.arraydata[index.row()][index.column()] = value
                self.dataChanged.emit(index, index, (Qt.DisplayRole, ))
                return True
            else:
                if index.column() == 2:
                    if r.match(value) and (0 < float(value) <= 1):
                        self.arraydata[index.row()][index.column()] = value
                        self.dataChanged.emit(index, index, (Qt.DisplayRole, ))
                        return True
                    else:
                        if r.match(value):
                            self.arraydata[index.row()][index.column()] = value
                            self.dataChanged.emit(index, index, (Qt.DisplayRole, ))
                            return True
        return False

    def print_arraydata(self):
        print(self.arraydata)

    def insert_row(self, data, position, rows = 1):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for i, e in enumerate(data):
            self.arraydata.insert(i+position, e[:])
        self.endInsertRows()
        return True

    def remove_row(self, position, rows = 1):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.arraydata = self.arraydata[:position] + self.arraydata[position + rows:]
        self.endRemoveRows()
        return True

    def append_row(self, data):
        self.insert_row([data], self.rowCount())


class Main(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        spacer_item = QSpacerItem(0, 20, QSizePolicy.Expanding)
        self.run_button = QPushButton("Run")
        self.tabledata = [['Baseline', 1, 2, 3, 4], ['Learning Rate', 11, 12, 13, 14],
                            ['% Decreased', 21, 22, 23, 24], ['# of Orders', 31, 32, 33, 34],
                            ['# of Parts', 41, 42, 43, 44]]
        self.table = self.create_table()
        delegate = NumericDelegate(self.table)
        self.table.setItemDelegate(delegate)
        row_1 = QHBoxLayout()
        row_2 = QHBoxLayout()
        row_1.addWidget(self.table)
        row_2.addSpacerItem(spacer_item)
        row_2.addWidget(self.run_button)
        main_layout = QVBoxLayout()
        main_layout.addLayout(row_1)
        main_layout.addLayout(row_2)
        self.centralwidget = QWidget()
        self.centralwidget.setLayout(main_layout)
        self.setCentralWidget(self.centralwidget)
        self.resize(1280, 720)

    def create_table(self):
        tv = QTableView()
        # set header for comments
        header = ['', 'Year 1', 'Year 2', 'Year 3', 'Year 4']
        row_names = ['a', 'b','c','d','e']
        tablemodel = Model(self.tabledata, header, row_names, self)
        stylesheet  = "QHeaderView::section{Background-color:lightgrey}"
        tv.setStyleSheet(stylesheet)
        tv.setModel(tablemodel)
        tv.resizeRowsToContents()
        return tv


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
