# Предмет: Языки написания спецификаций.

## Задание 2. Создание диаграмм для ВКР

### 1. Диаграммы 

#### 1.1. Диаграмма вариантов использования.

Code: 
```plantumlcode
@startuml
class User {
  +id: int
  +username: str
}

class Story {
  +id: int
  +title: str
  +content: str
  +created_at: datetime
}

class Character {
  +name: str
  +role: str
}

class Template {
  +id: int
  +structure: str
}

class StoryService {
  +generate_story()
}

class LLMService {
  +generate_text(prompt: str): str
}

class Database {
  +save_story(story: Story)
  +get_user_stories(user_id: int)
}

class FastAPIController {
  +create_story()
  +get_stories()
}

FastAPIController --> StoryService
StoryService --> LLMService
StoryService --> Database
Story --> Character
StoryService --> Template
@enduml
```


out: 

![use_cases](https://www.plantuml.com/plantuml/png/RL51QiCm4Bph5Jh6c7p0XvAIKYYaK4XxDbjxQGMIR7R7eQNqxyMs53TnBaBIpCxEpkuK91Y2DuqdLVkcBFR7M5kwjh8kOhmEoX8fS6KLOdvDuXxHoVUA30UVcDQMJHV14SjRcC1jJQXiIs2um8lY_fE46cGBIqzhI-dyjO5N3hqdyCg3GeO6WznqV6GvkIOLVN1a8N2j8xGf5kxXy7oR2Vx2ffSkzFDOnLMJ1mAzawOofLCMdyvgDb7CagZ7R2VSiMwcHvhZdvL7Kjo_FEsx2Ecyp_7CMPwT9y6iDTMlAxVRkuiOp4Kc8xeCliRoR3CoVPrtjcRd_PWTntO8_Wy0 "use_cases")


#### 1.2 Диаграмма классов.
Code: 
```plantumlcode
@startuml

class Character {
  +name: str
  +role: str
}

class StoryTemplate {
  +id: int
  +structure: str
}

class Story {
  +id: int
  +title: str
  +content: str
  +created_at: datetime
}

class User {
  +id: int
  +username: str
}

class Admin {
  +access_level: int
  +add_template(template: StoryTemplate)
  +remove_template(template: StoryTemplate)
}

class StoryService {
  +generate_story()
  +build_prompt()
}

class LLMService {
  +generate_text(prompt: str): str
}

User --> Story
Story --> Character
StoryService --> Story
StoryService --> StoryTemplate
StoryService --> LLMService

Admin --|> User

@enduml
```


out: 

![class_diagram](https://www.plantuml.com/plantuml/png/ZL6xRiCm3Dpr5HeT5Fu13q6AhkcKPZPOYMW5IB91dOqMRV-ziEL7N6VefXFlIDxnb422BdYbZAUKzDCx2Hcmw2-bzKEam9LEa058uoVmCzClQEJpXKFh2PmbpbRQHGpF1EaCEhchsh7XuDTXfedWY1KB4zZMX4fR0iC5NZjUqxpnJSCkiQm65kwZ3IvcCXd3ATMUU_QBZAojCLagvaUrjNeOy-3GzFmFxjRuXQLtPahhZICBWUiqb8gnxsldlArRQKABuaPzFZ_Vru8_K6J-wFMmE1vpASjZdgnoy0DUxgmsE_sXxhvdJ_lokfnIEU6o_3wEXr7gnD5smVy2 "class_diagram")


#### 1.3 Диаграмма последовательности.
Code:
```plantumlcode
@startuml
actor Пользователь
participant FastAPI
participant StoryService
participant LLMService
participant Database

Пользователь -> FastAPI: POST /generate
FastAPI -> StoryService: generate_story(params)
StoryService -> LLMService: generate_text(prompt)
LLMService --> StoryService: текст сказки
StoryService -> Database: save_story()
Database --> StoryService: OK
StoryService --> FastAPI: готовая сказка
FastAPI --> Пользователь: JSON ответ
@enduml
```

Out:

![sequence_diagram](https://www.plantuml.com/plantuml/png/TP51QiCm44NtEiKiuuNftekGGYcqJUk0iozJLnH3R0jf4jfbl0xa2Bc2IGafBlWCeniLXmWhJRBKrvzvNryZGwXfdiy4fbHgu0st_6jNlEUMjrpRYdVTMIZKbAMPmeBW7WtTJXvEj8HA_PL8lSXIUN8n7ZzVak-Gy0sD5E8Q4iAX8qKmYPCft7p8GceaAOvwP_714JZ7g-daWKADkGc4R-g6-b3U2CbF6YXTvee2qJiWFACS8ZPsQIkmIswuvZqt_7E6SO-CmE32PGg4aoziZf_-BV5Bu6zkRNLiQUsZwxwHS7Zr4oDuJE8NE2pPyivMOYIBzta--mC0 "sequence_diagram")

#### 1.4 Диаграмма состояний.
Code:
```plantumlcode
@startuml

state "Создан запрос" as Created : пользователь вводит параметры
state "Формирование prompt" as Prompt : сбор структуры Кэмпбелла
state "Генерация (LLM)" as Generating : вызов LLaMA
state "Постобработка" as Post : очистка и форматирование текста
state "Сохранена" as Saved : запись в PostgreSQL
state "Ошибка" as Error : ошибка генерации
state "Просмотр" as Viewed : пользователь читает результат

[*] --> Created

Created --> Prompt
Prompt --> Generating

Generating --> Post : успех
Generating --> Error : ошибка модели

Post --> Saved

Saved --> Viewed : открыть

Viewed --> Generating : перегенерация

Error --> Generating : повтор
Error --> [*]

Viewed --> [*]

@enduml
```

Out:

![state_diagram](https://www.plantuml.com/plantuml/png/VLBDIXn14BxtKnIUek0BU0W62Lv6I11o4Gy33YAukp8x9jVPtfW4L3nuyv0Gy05wHuTjrjdUL_ZgZK9LhxC_I6xJtJNVR-tsYpGlBZldnlIBjCXe0tyHCCOp7AQ4CHncN2BmO8FIFktbMLfa9xH3c27WXMymHa05nnQrd0aLAWGymxELASSb71hKRBdawvRd4O5BDF02BmYOmgEcYxpNkIYKxPD-qWxn02CP9nueoX0JjZmKFC83twB132CHW1Uubk8UDQQeHG3_WESxUfSa1vkAlPzripmjphgdOgRYwsY4aYGz-D0Y_17dR14mKXkYmc825_Nr-g8EWN_2wzm4Zk29ly_DIIph1ZMfYOwxvTJvIYccAZeI7APVOzZQWt98m4fyccU7dvCMu3V_WiUerVOnptjv5DS-49vM4u5VE8qjen67N2h6bxFis__BLkCMJjebBb5Zp4DvaKksnXnj7TFszllNnJ7cTOFaClPhvZNBpQ8LOvOQqk4ODWzvW1bglbeVUDjnexiec-6DKGoPrM2DYVdAnSAg5YoRnPPlZ9a_h8gBaTHg-6bzoOo9Ijxw9Q2IRU9oQUPewtY5Hi-xMVVaidF-3m00 "state_diagram")

#### 1.5. Диаграмма деятельности.
Code:
```plantumlcode
@startuml
start

:Ввод параметров героя;
:Выбор жанра;

:Формирование структуры Кэмпбелла;

:Зов к приключению;
:Отказ от пути;
:Встреча с наставником;
:Преодоление испытаний;
:Кульминация;
:Возвращение героя;

:Формирование prompt;

:Генерация через LLaMA;

if (Результат устраивает?) then (да)
  :Сохранение в БД;
else (нет)
  :Изменение параметров;
endif

stop
@enduml
```

Out:

![activity_diagram](https://www.plantuml.com/plantuml/png/VP9DJXj148NtVOfQcYimYy0U3e74e23PniB3VZoZW28d87ua40j8f1oWcT3nPCOUN-6h6qNLOmaM4RjMzLUltYlLpZGxECtEHaCN7yvjSqD5nwkmnckEPqdGGdCwAk4tmPvwbHYgSrxeD1V-u5aPdfZ6BokofExRx8-Q83ep9IrfjD1ISvqBZ_gT9MjU2BIq6uNxVbmZh3Mdfg7LIxqWc99UslGdBMZmB8HE2mDBBQXxOt4GGI_meZDXXRSQdYfwQUXO6lfic0Mce-tb2KAjCzOwZnrM-clievQq-is2HS5pwiqYw5XGMNxz-YRoRbaVB6LoUZAQP16vZRqXwaHniSZHuKBszWxsTnFdZezam0yhzNRCenQYvIQqfuxgGOjFMv9zJiSou1M_vKIs-KcdNoArUZDQ2TVS9IuTJbCPH0j5Zp-mi0Du3__dBXANZW-FZvoRPYSJjvEE3yz6mty0 "activity_diagram")


### 2. UI.

+ код можно посмотреть тут [ссылка на репозиторий](https://github.com/Kvazistam/Fairytalegeneratorui)
+ Сам сайт можно посмотреть тут. [ссылка на сайт](https://dusk-galaxy-70917595.figma.site/)

