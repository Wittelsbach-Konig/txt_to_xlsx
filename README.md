# TXT to XLSX GUI Converter

Простое кроссплатформенное GUI-приложение на Python для преобразования `.txt` файлов (с координатами аэродинамических профилей) в `.xlsx` Excel-файлы.  
Реализовано с использованием **PyQt6**, с поддержкой **Drag & Drop**, выбора директории и запоминания пути.

---

## Формат входного .txt файла

```txt
Airfoil name : #Название

Upper X      Upper Y
 x1           y1
 x2           y2
 ...          ...

Lower X      Lower Y
 x1           y1
 x2           y2
 ...          ...

```

---

## 📦 Возможности

- Перетаскивание `.txt` файла в окно
- Ручной выбор файла
- Конвертация данных в два листа Excel (`Upper Surface` и `Lower Surface`)
- Автоматическое название выходного файла из `Airfoil name`
- Сохранение последней выбранной директории
- Поддержка `.xlsx` (с помощью `pandas + openpyxl`)
- Иконка в окне и на панели задач
- Сборка `.exe` с помощью PyInstaller

---

## 📁 Установка и запуск

### 🔧 1. Установка окружения через [`uv`](https://github.com/astral-sh/uv)

```bash
uv venv
```

### 🚀 2. Запуск

```bash
uv run main.py
```

---

### 🏗 Сборка .exe (Windows)

```bash
pyinstaller txt_to_xlsx_gui/main.py ^
  --name=txt2xlsx_gui ^
  --icon=static/icon.ico ^
  --noconsole ^
  --onefile
```

Результат: dist/txt2xlsx_gui.exe

## 📂 Структура проекта

```bash
txt_to_xlsx_gui/
├── main.py               # Главный интерфейс
├── converter.py          # Преобразование .txt в .xlsx
├── settings.py           # Запоминание последнего пути
├── static/
|   ├──icon.ico           # Иконка приложения
├── README.md
└── requirements.txt
```

## 💡 Примечания

При первом запуске создаётся файл ~/.txt_to_xlsx_settings.json для сохранения пути
