from pathlib import Path

from flask import Flask, request
from PIL import Image
import json

app = Flask(__name__)


def params_to_json(image_path):
    try:
        # Открываем изображение
        img = Image.open(image_path)
        if img:
            json_data = json.dumps({"height": img.height, "width": img.width}, indent=4)
            return json_data
        else:
            return None

    except Exception as e:
        print(f"Ошибка при чтении метаданных изображения: {e}")
        return None


def exif_to_json(image_path):
    try:
        # Открываем изображение
        img = Image.open(image_path)

        # Получаем метаданные EXIF
        exif_data = img.getexif()

        # Преобразуем метаданные в формат JSON
        if exif_data:
            for k, v in exif.items():
            
            return json_data
        else:
            return None

    except Exception as e:
        print(f"Ошибка при чтении метаданных изображения: {e}")
        return None


@app.route('/size2json', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'Изображение не найдено', 400

    image_file = request.files['image']

    # Проверяем, что файл не пустой
    if image_file.filename == '':
        return 'Неверный файл', 400

    # Сохраняем изображение на сервере
    image_file.save('uploads/' + image_file.filename)
    image_path = "uploads/" + str(image_file.filename)
    json_params_data = params_to_json(image_path)
    if json_params_data:
        print(json_params_data)
    else:
        print("Не удалось получить метаданные EXIF изображения")

    return json_params_data


@app.route('/exif2json', methods=['POST'])
def upload_image():
    # Пример вызова функции для преобразования метаданных изображения "image.jpg" в JSON
    image_path = "image.jpg"
    json_exif_data = exif_to_json(image_path)
    if json_exif_data:
        print(json_exif_data)
    else:
        print("Не удалось получить метаданные EXIF изображения")

    return json_exif_data_data


if __name__ == '__main__':
    path = Path("uploads\diagramm_drawio.png")
    img = Image.open(path)
    print(img.height)
    exif = img.getexif()
    for k, v in exif.items():
        print("Tag", k, "Value", v)
