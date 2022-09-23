### Домашка 29

##### В этой работе мы изучаем сериализацию в Django, а также методы поиска и фильтрации в запросах.

Работа с пользователями выполнена через GenericView.

CRUD для локаций реализован с использованием ViewSet и Route.

Также выполнены различные поисковые запросы по объявлениям согласно условию задания.
___
Для запуска контейнера и наполнения базы необходимо в терминале выполнить следующие команды:
```
docker-compose up -d
./manage.py migrate
./manage.py loaddata fixtures/ad.json fixtures/category.json fixtures/location.json fixtures/user.json
```