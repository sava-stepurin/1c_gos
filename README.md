# Классификация текстов

## Условие
Разработать скрипт, который будет с адекватным качеством классифицировать тексты по стилю (“разговорный”, “техническая литература”, “художественная литература”). 

(качество может быть ограничено лимитированным временем).

Обучающий датасет не предоставляется 

## Датасеты
* Разговорный (твиты) - https://www.kaggle.com/jp797498e/twitter-entity-sentiment-analysis/version/2?select=twitter_training.csv
* Техническая литература (статьи из NIPS) - https://www.kaggle.com/benhamner/nips-papers
* Художественная литература (список произведений) - Alice in Wonderland, Emma, Dracula, A journey to the center of the Earth, The jungle book, The call of the wild, Moby Dick

## Обучение
Использовались WordPunctTokenizer, TfidfVectorizer и LogisticRegression на нескольких классах (на трех). Более подробно в [ноутбуке](https://github.com/sava-stepurin/1c_gos/blob/main/text_classification.ipynb)

## Применение
Для применения достаточно запустить файл inference.py, указав в нем путь до файла с текстом

`python inference.py --file_path example.txt`
