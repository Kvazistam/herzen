# подключаем библиотеку компьютерного зрения 
import cv2
def highlightFace(net, frame, conf_threshold=0.7):
        # делаем копию текущего кадра
        frameOpencvDnn=frame.copy()
        # высота и ширина кадра
        frameHeight=frameOpencvDnn.shape[0]
        frameWidth=frameOpencvDnn.shape[1]
        # преобразуем картинку в двоичный пиксельный объект
        blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
        # устанавливаем этот объект как входной параметр для нейросети
        net.setInput(blob)
        # выполняем прямой проход для распознавания лиц
        detections=net.forward()
        # переменная для рамок вокруг лица
        faceBoxes=[]
        # перебираем все блоки после распознавания
        for i in range(detections.shape[2]):
            # получаем результат вычислений для очередного элемента
            confidence=detections[0,0,i,2]
            # если результат превышает порог срабатывания — это лицо
            if confidence>conf_threshold:
                # формируем координаты рамки
                x1=int(detections[0,0,i,3]*frameWidth)
                y1=int(detections[0,0,i,4]*frameHeight)
                x2=int(detections[0,0,i,5]*frameWidth)
                y2=int(detections[0,0,i,6]*frameHeight)
                # добавляем их в общую переменную
                faceBoxes.append([x1,y1,x2,y2])
                # рисуем рамку на кадре
                cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
        return frameOpencvDnn,faceBoxes
def camera_detect(faceNet, num_cam = 0):
    # получаем видео с камеры
    video=cv2.VideoCapture(num_cam)
    # пока не нажата любая клавиша — выполняем цикл
    while cv2.waitKey(1)<0:
        # получаем очередной кадр с камеры
        hasFrame,frame=video.read()
        # если кадра нет
        if not hasFrame:
            # останавливаемся и выходим из цикла
            cv2.waitKey()
            break
        # распознаём лица в кадре
        resultImg,faceBoxes=highlightFace(faceNet,frame)
        # если лиц нет
        if not faceBoxes:
            # выводим в консоли, что лицо не найдено
            print("Лица не распознаны")
        # выводим картинку с камеры
        cv2.imshow("Face detection", resultImg)

def prepare_net(faceProto="model\\opencv_face_detector_uint8.pb", faceModel=u"model\\opencv_face_detector.pbtxt"):
    # запускаем нейросеть по распознаванию лиц
    faceNet=cv2.dnn.readNet(faceModel,faceProto)
    return faceNet

def image_detect(path_to_image, faceNet):
    # Загружаем изображение
    image = cv2.imread(path_to_image)
    if image is None:
        print("Ошибка: изображение не загружено.")
        return
    
    # Вызываем функцию распознавания лиц
    resultImg, faceBoxes = highlightFace(faceNet, image)

    # Выводим результат
    if not faceBoxes:
        print("Лица не распознаны")
    cv2.imshow("Face detection", resultImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    net = prepare_net()
    img_path = "fullman.png"
    # img_path = "10.png"
    # image_detective(img_path, net)
    camera_detect(net)