# Урок 19. Знакомство с Django. Домашнее задание
<br>

> Запуск Jango проекта через **Run - "название проекта"**
> или командой **python manage.py runserver** 

> homework_django - config проекта

> catalog - первое приложение проекта

<br>

### **Цель проекта:**
<br>

> Создать проект интернет-магазина, который будете дорабатывать на каждом уроке в течение всего курса. 
Выполняйте каждое домашнее задание — и в конце курса у вас получится полноценный проект, 
который вы добавите в свое портфолио.

<br>

**Задание 1**

Для начала работы над задачей выполните первые шаги:
- Настройте виртуальное окружение.
- Создайте новый Django-проект.

**Задание 2**

- После успешного создания проекта сделайте первую настройку. 
Для этого cоздайте **первое приложение** с названием `catalog`.
- Внесите начальные настройки проекта.
- Сделайте настройку урлов (URL-файлов) для нового приложения.

**Задание 3**

- Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.

```bash
Для создания шаблонов лучше использовать UIkit Bootstrap. 
Это удобный набор элементов, которые уже стилизованы и готовы к использованию. 
UIkit Bootstrap помогает избежать самостоятельной верстки макетов.
Если возникнут проблемы при создании собственного интерфейса, 
возьмите за основу данный шаблон: https://github.com/oscarbotru/.
```

**Задание 4**

В приложении в контроллере реализуйте два контроллера:
- Контроллер, который отвечает за отображение домашней страницы.
- Контроллер, который отвечает за отображение контактной информации.

**Дополнительное задание**

Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.
