
# qr_code_bot

Телеграм-бот для генерации QR-кодов из ссылок.  
Реализован напрямую через Telegram Bot API с использованием библиотеки `requests`, без `aiogram` и `pyTelegramBotAPI`.

Проект сделан в учебных целях в рамках задания по программированию.

---

## Возможности

- генерация QR-кода из любой ссылки
- команды `/start` и `/me`
- обработка геолокации
- сохранение уникальных пользователей в CSV
- ежедневный текстовый отчёт о работе бота
- поддержка нескольких администраторов
- планировщик задач (`schedule`)

---

## Структура проекта

```text
qr_bot/
├── run.py                  # точка входа
├── requirements.txt
├── README.md
├── .env                    # токен бота и администраторы
├── data/
│   ├── users.csv           # сохранённые пользователи
│   └── daily_report.txt    # отчет за день
├── temp/                   # временные файлы (QR-коды)
└── utils/
    ├── telegram_api.py     # работа с Telegram Bot API
    ├── handlers.py         # обработка сообщений
    ├── users.py            # работа с CSV
    ├── qr.py               # генерация QR-кодов
    ├── report.py           # отчеты
    ├── scheduler.py        # планировщик задач
    └── logger.py           # логирование
```


## **Требования**

- Python 3.10+
    
- Telegram Bot Token
    
- доступ к интернету

## **Установка и запуск**

### **1. Клонировать репозиторий**
`git clone https://github.com/USERNAME/qr_code_bot.git
`cd qr_code

### **2. Создать виртуальное окружение**

`python -m venv .venv
`source .venv/bin/activate   # macOS / Linux
`.venv\Scripts\activate      # Windows`

### **3. Установить зависимости**

`pip install -r requirments.txt`

### **4. Создать файл** 

### **.env**

  `BOT_TOKEN=ваш_telegram_bot_token
`ADMIN_IDS=123456789,987654321`

