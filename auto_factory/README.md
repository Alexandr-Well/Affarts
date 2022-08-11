ТЕСТОВОЕ 

Есть автомобильный завод,
нужна система для хранения стоимости деталей машины и расчета итоговой стоимости автомобиля.
Каждая деталь имеет:
    1) Тип (фара, решётка, ручка и т.д.)
    2) цену
    3) необходимое количество на один автомобиль,
    4) набор индивидуальных параметров.
Задача:
Подготовить таблицы базы данных для расчета стоимости автомобиля.
Учитывать, что стоимость автомобиля состоит из стоимости деталей и наценки производителя.
Все расчеты необходимо описать внутри классов django моделей.
Для упрощения можно сделать базу данных, исходя из того, что автомобиль состоит из капота, фары, руля и кресла.
Расчеты и результаты лучше всего хранить в ещё одной отдельной таблице

Если по пунктам, то вроде уже все сделано


## модель непосредственно детали: Detail
```
    1) Тип (фара, решётка, ручка и т.д.)
    2) цену
```
## расшириная модель детали: CurrentAutoDetail, так ка комплектации могут быть разные
## и колиичество деталий необходимых для авто могут быть разными

```
    3) необходимое количество на один автомобиль,
    4) набор индивидуальных параметров.
```

4) дальше нигде не упомянался по заданию, я его не использовал

## Подготовить таблицы базы данных для расчета стоимости автомобиля - модели готовы.
## Учитывать, что стоимость автомобиля состоит из стоимости деталей и наценки производителя. - модель Auto делает это
## Все расчеты необходимо описать внутри классов django моделей все ращеты описаны в классах.
## Расчеты и результаты лучше всего хранить в ещё одной отдельной таблице - сделано: модель AutoPrice считает сумму в момент сохранения

# файлы с кодом: models.py, scrypt.py , admin.py в app_factory