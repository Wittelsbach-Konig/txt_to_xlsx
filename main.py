import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from converter import convert_txt_to_xlsx
from settings import get_last_save_path, set_last_save_path


class TxtToXlsxApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Конвертер TXT в XLSX")
        self.setFixedSize(640, 480)
        self.setAcceptDrops(True)

        self.setWindowIcon(QIcon("static/icon.ico"))

        font = QFont()
        font.setPointSize(14)
        self.setFont(font)

        self.txt_path: Path | None = None
        self.output_path: Path = get_last_save_path()

        self.layout = QVBoxLayout()  # type: ignore

        self.drop_area = QLabel("Перетащите сюда .txt файл")
        self.drop_area.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.drop_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drop_area.setFixedHeight(250)
        self.layout.addWidget(self.drop_area)  # type: ignore

        self.info_label = QLabel("Или выберите файл вручную")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.info_label)  # type: ignore

        self.select_button = QPushButton("Выбрать .txt файл")
        self.select_button.setFixedHeight(40)
        self.select_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.select_button)  # type: ignore

        self.save_button = QPushButton("Конвертировать и сохранить .xlsx")
        self.save_button.setFixedHeight(40)
        self.save_button.clicked.connect(self.save_file)
        self.layout.addWidget(self.save_button)  # type: ignore

        self.setLayout(self.layout)  # type: ignore

    def dragEnterEvent(self, event) -> None:  # type: ignore
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event) -> None:  # type: ignore
        for url in event.mimeData().urls():
            file_path = Path(url.toLocalFile())
            if file_path.suffix == ".txt":
                self.txt_path = file_path
                self.drop_area.setText(f"Выбран файл: {self.txt_path}")

    def open_file_dialog(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Открыть TXT файл", "", "Text Files (*.txt)"
        )
        if path:
            self.txt_path = Path(path)
            self.drop_area.setText(f"Выбран файл: {self.txt_path}")

    def save_file(self) -> None:
        if not self.txt_path:
            QMessageBox.warning(
                self, "Файл не выбран", "Пожалуйста, выберите .txt файл."
            )
            return

        path = QFileDialog.getExistingDirectory(
            self,
            "Выберите папку для сохранения",
            str(self.output_path),
        )
        if path:
            self.output_path = Path(path)
            set_last_save_path(self.output_path)
            try:
                saved_file = convert_txt_to_xlsx(
                    self.txt_path, self.output_path
                )
                QMessageBox.information(
                    self, "Успех", f"Сохранено в файл:\n{saved_file}"
                )
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", str(e))


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/icon.ico"))  # <=== Важно!
    window = TxtToXlsxApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
