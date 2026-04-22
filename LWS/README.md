# Предмет: Языки написания спецификаций.

## Задание 2. Создание диаграмм для ВКР

### 1. Диаграммы 

#### 1.1. Диаграмма вариантов использования.

Code: 
```plantumlcode
@startuml
left to right direction
skinparam packageStyle rectangle

actor "Пользователь" as User
actor "Администратор" as Admin

rectangle "Система генерации сказок" {
  usecase "Сгенерировать сказку" as UC1
  usecase "Просмотреть историю сказок" as UC2
  usecase "Переписать/пересоздать сказку" as UC3
  usecase "Управлять шаблонами" as UC4
  usecase "Просмотреть статистику" as UC5
}

User --> UC1
User --> UC2
User --> UC3
Admin --> UC4
Admin --> UC5

UC1 ..> UC2 : «include»
UC3 ..> UC1 : «extend»
@enduml
```


out: 

![use_cases](https://www.plantuml.com/plantuml/png/ZL7DIiD06BplKtpqtah_BXwaqaUGFi2Ih3KqJKko0KM4fe9uAEeR5F7e9TO6GzEcq2UOVIF99hQD87YS_MQ-cVcsuqdkIdzeCrjSIf8ZSgt-bIJJSeKXhP73l87bZBdBXpJcne3tnOMyiGLbO-xqRS4OD-J8fGhcI96e6RwGOe5GJH5bk4BSevudt3tn1Kki4ME3M0LggYQQdAg9ffwRGyjXR6z05RpcH4HO8oHy8i86aTOz84PCAi0AeNPULUYM4VcUCBYNYm_yM4r-mgdPGRLIztdARhqadMTq5M2DLCUCjAm8a-fzJx-yzPP6UOksZh3DXBdr2RRvemgGuWlBlnCrIxlUiCrgOu54FUUIHuJuG88K6uJPNGjXwnzLT97i-7cb-CYtpUuOoxwDgjKpVPaZq3W6JQQ_h42j4ceprklMgLRJAZgbtRlb6BPlYbt2UjrcCQdhYRYMmZ5t2Ui8n_I7zZS0 "use_cases")


#### 1.2 Диаграмма классов.
Code: 
```plantumlcode
@startuml
skinparam classAttributeIconSize 0

class User {
  +id: int
  +username: str
  +email: str
  +created_at: datetime
  +get_stories(): List<Story>
}

class Admin {
  +access_level: int
  +add_template(template: StoryTemplate): bool
  +remove_template(template_id: int): bool
  +show_history(user_id): List<Story>
}

class Story {
  +id: int
  +title: str
  +content: str
  +created_at: datetime
  +user_id: int
  +template_id: int
  +add_character(c: Character): void
  +get_content(): Str
  +get_title(): Str
}

class Character {
  +id: int
  +name: str
  +role: str
  +description: str
}

class StoryTemplate {
  +id: int
  +name: str
  +structure: str
  +description: str
}

class StoryService {
  +generate_story(params: StoryParams): Story
  +build_prompt(template: StoryTemplate, chars: List<Character>): str
  +regenerate_story(story_id: int): Story
}

class LLMService {
  +generate_text(prompt: str, model: str): str
  +validate_response(text: str): bool
}

interface StoryRepository {
  +save(story: Story): bool
  +find_by_id(id: int): Story
  +find_by_user(user_id: int): List<Story>
  +delete(story_id: int): bool
}

class APIController {
  +create_story(request: StoryRequest): Response
  +get_stories(user_id: int): List[StoryDTO]
  +regenerate_story(story_id: int): Response
}


' Наследование
Admin --|> User : наследует

' Связи сущностей
Story "1" *-- "0..*" Character : содержит 
Story ..> StoryTemplate : основана на 
User "1" --> "0..*" Story : создал 

' Сервисные зависимости
APIController --> StoryService
StoryService --> StoryRepository
StoryService --> LLMService
StoryService ..> StoryTemplate : использует 

' Примечания
note right of StoryRepository: Реализация: PostgreSQL
note right of LLMService: Провайдер: LLaMA / OpenAI
note right of APIController
  Реализация: FastAPI
  Маршруты: 
      POST /generate, 
      GET /stories, 
      POST /regenerate/{id}
end note
@enduml
```


out: 

![class_diagram](https://www.plantuml.com/plantuml/png/ZLJRRXit47tdLmpy4YcrxFHrKGWHqWiCAB0QkKz5iQ1tnpRHtQLAKchIn80lG2z8WVn0WhH_81XMhS2r-ml3Foguv6gbbTr63y8EBsVEd3d3nzfmPSPvnlJteXXnnND8CgvrpnWbziS6Tn9P3CLF28yOAtVW6uqANZA0JqGQWIYC-nnhL0NFCG9jb5l0d8ji4IKAkS4qvYQ2b1iq8aUtVeWcraOgWRhLZg0ljFbiQAHwqMN7LRvUcel29-H9Wbh76KumMwJcQHeRp4SPDzYgFY8eOVP2s8vWNyhC7LUOomcktuX3DKj7zP7yCJuIZk2Bbgim5kbzBCjuJHOZJ5PhaiZ2O67-LvMGgaPfKAogJewuueb1rKeYU585xGWcKgILl26fatVeqxhLabYrjYXYWR5Mo4flbLmgAaMTA34oGXP-RLMIgWF_ZQYD6YTch3uQTeXg8fA0UeW5AgUFxrHfOnqSC2Y3TeZSwVsnoD9uf6G-ClVvPHESjZhqUY5BjrrhW8sivV-IYNo-1Uj-_-dTd0q-DotFfWJVX5ocw4UdJZVXcN0MYHNgaIoqy-rpKnqg3NlCc2WCgWEUeC_-34TIYzgOca_Gympqbhn-88eqtdS5j9erBEqwPxQMxTaOXx9n6HfSawEY66PwiFD45aR9BAlCveSXYAdmXp5g4rLrb54xWcUX-kRRSGUbRykhd-_jVlTHxLeW7pF67W2zewazfMkQqINTqWLDwORcD6F-DUfqNdNzGnW1tTH7xJdDx5a9y2TTs3TqHNEmf_RS_aOtT6jFxHdDw0FphyN6fnlmiDE1ZKTRMmytbgOl0djAjtH9Ctj2Vz7Sda6uihNLRSnL10xNeGUMqv8Hi9AUIz7fTAiK7YJ0Nz4bJUaQ0bsNwuBc3ik-fXdG5Kt3mfp-3kJdRBLr3djv8DdAT2vsQoUk7wWdOtNlpb8Tct_ebgxjxtJbrVRytzkJakRC_k9xPT-mGXe49GwF3CY39f48w0-QEG5exagrFxix4GoaDeSAXr_t6_Thdf5FvmN_uDiKGR_Fd_PW6tP7MFHs6fTNL6DmJ-ulkJQzmOxRVqjJUs9_jIVst9xPrn4mA7-3tU4UR5TctgoMl_fY3xR3D6okdgsjl_rIfCSCYnGSEVOOYtISP_y2 "class_diagram")


#### 1.3 Диаграмма последовательности.
Code:
```plantumlcode
@startuml
autonumber
actor "Пользователь" as User
participant "APIController" as API
participant "StoryService" as Service
participant "LLMService" as LLM
participant "StoryRepository" as DB

== Генерация сказки ==

User -> API: POST /generate {params}
activate API

API -> Service: generate_story(params)
activate Service

Service -> Service: build_prompt(template, characters)

Service -> LLM: generate_text(prompt)
activate LLM
LLM --> Service: StoryContent
deactivate LLM

Service -> DB: save(story: Story)
activate DB
DB --> Service: story_id: int
deactivate DB

Service --> API: Story
deactivate Service

API --> User: 201 Created {story: Story}
deactivate API

== Регенерация (опционально) ==

User -> API: POST /regenerate/{id}
API -> Service: regenerate_story(id)
Service -> LLM: generate_text(new_prompt)
LLM --> Service: updated_content
Service -> DB: update(story)
Service --> API: Story
API --> User: 200 OK {story}

== Обработка ошибки ==

alt Ошибка генерации
    LLM --> Service: error
    Service --> API: ErrorResponse
    API --> User: 500 Internal Error
end
@enduml
```

Out:

![sequence_diagram](https://www.plantuml.com/plantuml/png/XLDDQzj04BtlhnXyig4cRg4NWqFik0TJcPYuFPkDDBG2QILMAxV56DeSIW-57dfF-XFa5XEJOlKlZFvHsPNaI5P3RwETz-RZlT5PfBXKiUyn7gj0nFuLIiPj5KXeqIsbz3lxIdUKqazAiclQwkyMy0XUHoXPoALoRJVaGa5hE9kS1qB9mFDG6inmDgb3vYgG7-OebwwD1b74TPHbJQiOovh-eyebXa7awiY0nYF61WEWxxIbFMspZvHadscNVOFi4zrJGdTqJpiO31ZJaqFtL4_NXzd5_1MSl461aYk4LSWbzwErbi1TwXUz0nlE9ffHJDM74h-8z03jdDHv89LhiIAeaQzYrtCMeGpyKBKL-g775Ju1-osNt5OeeqwDPrdJIaE5xrKxvrRwQOaiQmhTQXyZatO4XM8Eri3L1kDH7oA-nBPPfk1LYez7R3ogbpR8XUlqmQtNrZOSIfSQcu9Lr44Uesltr1nJ7vxrdiAvHAxGWLLrc7MLR0pHLl-WBVrgsDscbFxec5BQKsBkTqzfvp7h9PRQdgnSPzsm-Y5VcEqwdV_O8_3TehIeuKeSEdh1XLqOSsH4diwjw3mcvR5iFRXuMIYsphMveOtMX3QKPjVw_e7Ix0ljQ7Fu3RYdW6uEZmaSYqax1W3Gs02b3AH9DSPxeLEN68M1YD10wgC-x_LW8XHAmRqSp50ux0o54_lUNm00 "sequence_diagram")

#### 1.4 Диаграмма состояний.
Code:
```plantumlcode
@startuml
skinparam state {
  BackgroundColor White
  BorderColor Black
}

[*] --> Created : старт

state "RequestCreated" as Created : Ввод параметров пользователем\nВалидация данных
state "PromptBuilding" as Prompt : Загрузка StoryTemplate\nСборка структуры Кэмпбелла\nФормирование prompt
state "LLMGeneration" as Generating : Вызов LLMService\nОжидание ответа модели
state "PostProcessing" as Post : Очистка текста\nФорматирование вывода
state "Persisted" as Saved : Запись в PostgreSQL\nИндексация для поиска
state "Error" as Error : Логирование ошибки\nПодготовка сообщения пользователю
state "Viewed" as Viewed : Отображение результата\nВозможность экспорта/регенерации

Created --> Prompt : данные валидны
Created --> Error : ошибка валидации

Prompt --> Generating : prompt готов
Prompt --> Error : шаблон не найден

Generating --> Post : успех (200)
Generating --> Error : таймаут / ошибка модели

Post --> Saved : обработка завершена
Post --> Error : форматирование не удалось

Saved --> Viewed : готово к показу
Viewed --> Generating : запрос на регенерацию
Viewed --> [*] : сессия завершена

Error --> Generating : повтор (≤3)
Error --> [*] : критическая ошибка
@enduml
```

Out:

![state_diagram](https://www.plantuml.com/plantuml/png/VLHDYnDB5DtNhoXSgI2Axbo8Z8YR2Eg8BinRD9DY39DqZzKTHKJeT9xFaOmAir4K5C4VqCdOapOVdRzmxb_mbxntRwKxxUJX9kbKxZtdddDFzVKmycpKwtPKkDVszpthTNKOUP7HBvJMMzxEtguDUdxhHj09h7xuk1qPFWziorXtjjNnTlRKIwKUdVzBNxXmJT-mnejCIr_LrAS4ASMKAEL0pzmpJtecZ5OrPxGNrkfnX34A_D1OSXjIp95HGZ4AZFcmm8mECU6VI2b1XXaop9i-Zf1YXXm_aD8_oEczvaSiiA0XlIhPxzYWknzjzTgTLjlV5NPtnEGVaEAOOXfWWYbIlHq5zlbzqztlU95f-lY64GgAvJzM9gLJIcX0CGqrFj5RpB74ICQQ8Mtw-2uTS-HEWqoK8zFxmbgErMZSlcLyOxse7VWoLVdJtnLRQEX4wqRZzhQnJzixFD0Nd3Z5Ar0Kb63CZY7LcBEJCafUoG_2w8uDTamOLlA3KCH_eTV8PLyYZwsTklNLLB3bfvLWJ4EtDQGLZx5XEoptk-qzTTjbWvV2SgZ_soTJxrgpVRVHzF4H2vbsIltw1cVynNlFgS-JbGmthGsieCiJetz6WUFDyGewG8uHfiYRFhxAeCVY59UvNQ90WH6zGSPT9UL6rEXTIV-WRPwjrBb7Ps4YC9pR4mU5J5EC31CQC9pS1cVf4GfCP4SdMA2GF1rgUYi6BDblBhmetSS2bZ4mEuDSgVBEy7rR9xXAlEobkX4B6lxMK5cszYQjrrSiAsJk-IsGBhrwxMEziaId0wGOOOO22ytpyqUAdxBcXL8rH57XWaW3qP_HAttsygLBvqwNLUY9O74c1vJeYwV4rCEl19gRgoIMQng90EcO89Mx4zE1s9sksohEl_zq3rWX3MG7CrdeeLAEa37MCLc7hz2OkgXDaN96rAfgmt2PRicCr1SRzVy5WzxL0VXrpAzWPDIdlelrfaZbn6qoybXZ7fHYVVRNc-zNpjLA7JQc52CNBrup2yjWbjecr7NZjthTphy0 "state_diagram")

#### 1.5. Диаграмма деятельности.
Code:
```plantumlcode
@startuml
skinparam activity {
  BackgroundColor White
  BorderColor Black
  ArrowColor Black
}

start

:Ввод параметров героя;
:Выбор жанра и тональности;

partition "Подготовка контекста" {
  :Загрузка StoryTemplate;
  :Формирование структуры Кэмпбелла;
  note right
    Зов к приключению
    Отказ от пути
    Встреча с наставником
    Преодоление испытаний
    Кульминация
    Возвращение героя
  end note
}

:Сборка final prompt;

partition "Генерация и валидация" {
  :Инициализация счётчика попыток (0);
  
  while (Попыток < 3) is (да)
    :Вызов LLaMA через LLMService;
    :Получение сырого текста;
    :Постобработка (очистка, форматирование);
    
    if (Результат устраивает?) then (да)
      :Сохранение в PostgreSQL;
      :Возврат готовой сказки пользователю;
      break
    else (нет)
      :Корректировка параметров / prompt;
      :Увеличение счётчика попыток (+1);
    endif
  endwhile (нет)
  
  if (Сказка не сгенерирована) then (да)
    :Сообщение о превышении лимита попыток;
    :Логирование ошибки;
  endif
}

stop
@enduml
```

Out:

![activity_diagram](https://www.plantuml.com/plantuml/png/VLJDQXDH5DxFKnnS9IYek6i4hMuZA1LSZysq7PhCXCbK4H6IYLebMb4NIWLhqGUOf8uP9-dDAtpdZUISEqb72sv2kFETd-_dtfkzs8tYlKxRwUtwGTUDt0wvcx7_o8-Vq5E7w9QxkRiTXNj1wtRO3YDwiEF7dfo7KSkBxDcjjhkvwn2jHr7uk7hqp76ql-EiuGCcCFX9M23bFbBCaN72VHXC22V8v2-_QmYKHnZ3S9_m2obE1Kx8YHCOd2B5ZD_W58O7d21lE4xNZM8_ziE0Bk18fk04Hj4J559RI24do51eKNf1oQtX4rASS9-7c2fo8mwZ9_UzJhVjnbv38Jza4yoHsrrb8UJ8I1ffPS493xdF8y8XlyKS2uoHOOOPKcaHXB57aR-z4pj4HFXaAHU41VUHey2C3tWVcJJc0mlwoeaiX2a94u4EXQpz-C7EHiRxI8a79AfOOfZeUa9uRi570bHH36Ps2392pWCiUAGrSlJReWzvgFBEaMlJbyZvNJaL1bDCn0r-VTPePPr3v0KjfIlEh-7OkgZ2Rlc1swPk57QwyJ-EVTHUcVRLSUAr2Zr3Zf_BqwLbdrMcbyXBm7HLnWFUv_USyBuga4hMJ4dIeA3QbRhuuH0ztl7R7jKqB6VVhzErElazgidGkfAsOPogOyscUsUTn2XLT4hDvfqDBthaRsfI12pzPZnSccbJCjBWdC1GDO6L4Zqm6Ekr66joPViQZ33HhmNIIyJFooYc4eM_urYt_VJ7tw8QlicAramPnmdni8nDYbmBCqvkr2dUyO8gPLdg68PVAFBqpEW9tGrxyNRaRTnhDbRGQYeIgbmyWz_40njY56BfGjLvO-LK4fb4VzdhOUIvk_hVQ_V47Gb5ShRKeR1NwOiA_zBdys_AvLNQbWs-OwBtCl_Rd_zdvkBLKbelQFbRDkFB-AmMT4hHZrTqKxcJqbxkHndlgcNfUU5LTir1vNOP-qfacF28NvNdEMdovKrApgsy3DON3Ts_hnOClqAEiJZIS9QizA4EkyvDBsZjTTf_0000 "activity_diagram")


### 2. UI.

+ код можно посмотреть тут [ссылка на репозиторий](https://github.com/Kvazistam/Fairytalegeneratorui)
+ Сам сайт можно посмотреть тут. [ссылка на сайт](https://dusk-galaxy-70917595.figma.site/)

