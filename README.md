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

**Задание**

Для начала работы над задачей выполните первые шаги:
- Настройте виртуальное окружение.
- Создайте новый Django-проект.

**Задание**

- После успешного создания проекта сделайте первую настройку. 
Для этого cоздайте **первое приложение** с названием `catalog`.
- Внесите начальные настройки проекта.
- Сделайте настройку урлов (URL-файлов) для нового приложения.

**Задание**

- Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.

```bash
Для создания шаблонов лучше использовать UIkit Bootstrap. 
Это удобный набор элементов, которые уже стилизованы и готовы к использованию. 
UIkit Bootstrap помогает избежать самостоятельной верстки макетов.
Если возникнут проблемы при создании собственного интерфейса, 
возьмите за основу данный шаблон: https://github.com/oscarbotru/.
```

**Задание**

В приложении в контроллере реализуйте два контроллера:
- Контроллер, который отвечает за отображение домашней страницы.
- Контроллер, который отвечает за отображение контактной информации.

**Дополнительное задание**

Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.

**Задание**

Подключите СУБД PostgreSQL для работы в проекте. Для этого:

- Создайте базу данных в ручном режиме.
- Внесите изменения в настройки подключения.

**Задание**

В приложении каталога создайте модели:

- `Product`
- `Category`

Опишите для них начальные настройки.

**Задание**

Для каждой модели опишите следующие поля:

`Product`:
- наименование,
- описание,
- изображение (превью),
- категория,
- цена за покупку,
- дата создания,
- дата последнего изменения.

`Category`:
- наименование,
- описание.

```bash
Для поля с изображением необходимо 
добавить соответствующие настройки в проект, а также 
установить библиотеку для работы с изображениями Pillow.
```
**Задание**

Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:

- Создайте миграции для новых моделей.
- Примените миграции.
- Внесите изменения в модель категорий, добавьте поле `created_at`, примените обновление структуры с помощью миграций.
- Откатите миграцию до состояния, когда поле `created_at` для модели категории еще не существовало, и удалите лишнюю миграцию.

**Задание**

Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.

При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

**Задание**

- Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
- Сформируйте фикстуры для заполнения базы данных.
- Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.

```bash
Последний пункт можно реализовать в связке с инструментом 
работы с фикстурами, можно описать вставку данных отдельными запросами.
```
