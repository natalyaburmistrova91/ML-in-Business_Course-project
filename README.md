# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/datasnaek/mbti-type?select=mbti_1.csv

Задача: предсказать по тексту (постам/отзывам/комментариям/запросам), написанному человеком, его социотип по типологии Майерс — Бриггс.

Используемые признаки:

- posts (text)

Преобразования признаков: tfidf

Модель: GradientBoostingClassifier

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/natalyaburmistrova91/ML-in-Business_Course-project.git
$ cd GB_docker_flask
$ docker build -t gb_docker_flask .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models gb_docker_flask
```

### Переходим на localhost:8181
