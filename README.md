# HabitTracker

HabitTracker — это приложение для отслеживания привычек, позволяющее пользователям устанавливать цели и отслеживать их выполнение.

## Установка

Следуйте этим шагам для запуска проекта локально и на удаленном сервере.

### Локальный запуск

1. **Клонируйте репозиторий**:
bash
   git clone https://github.com/ArtemKazagashev89/HabitTracker.git
   cd HabitTracker
2. **Убедитесь, что у вас установлены Docker и Docker Compose**. Если нет, установите их:
bash
   sudo apt-get update
   sudo apt-get install docker.io docker-compose
3.  **Создайте файл `.env`** на основе `.env.example` и заполните его необходимыми значениями.

4. **Запустите проект**:
bash
   docker-compose up --build
5. **Откройте браузер** и перейдите по адресу [http://localhost:8000](http://localhost:8000).

### Развертывание на удаленном сервере

1. **Подключитесь к вашему серверу**:
bash
   ssh tema@158.160.139.124 
2. **Клонируйте репозиторий на сервере**:
bash
   git clone https://github.com/ArtemKazagashev89/HabitTracker.git
   cd HabitTracker
3. **Создайте файл `.env` на сервере** и заполните его необходимыми значениями.

4. **Запустите проект**:
bash
   docker-compose up --build -d
5. **Адрес сервера с развернутым приложением**:
   Откройте браузер и перейдите по адресу [http://10.130.0.24](http://10.130.0.24).

## Настройка сервера и CI/CD

### Установка необходимых инструментов

Установите Docker и Docker Compose на сервере:

bash
sudo apt-get update
sudo apt-get install docker.io docker-compose

### Настройка CI/CD

Добавьте файл конфигурации для GitHub Actions:

yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Build and Deploy
        run: |
          docker-compose build
          docker-compose up -d