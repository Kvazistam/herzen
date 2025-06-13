import cv2
import tkinter as tk
from PIL import Image, ImageTk
import face_detection
from tkinter import filedialog

class FaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Распознавание лиц")

        self.faceNet = face_detection.prepare_net()
        
        # Поле для отображения видео
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()
        
        # Кнопка для загрузки изображения
        btn_image = tk.Button(root, text="Распознать лицо с фото", command=self.open_image)
        btn_image.pack(pady=10)

        # Запуск камеры
        self.video = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        hasFrame, frame = self.video.read()
        if hasFrame:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resultImg, faceBoxes = face_detection.highlightFace(self.faceNet, frame)
            image = Image.fromarray(resultImg)
            photo = ImageTk.PhotoImage(image=image)
            
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo  # Чтобы объект не удалился сборщиком мусора

        # Вызываем эту функцию снова через 20 мс
        self.root.after(20, self.update_frame)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            face_detection.image_detect(file_path, self.faceNet)

    def __del__(self):
        self.video.release()

root = tk.Tk()
app = FaceApp(root)
root.mainloop()
