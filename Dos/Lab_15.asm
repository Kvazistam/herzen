org 100h ; Так как мы пишем COM-программу

section .data
    Sector db 16 dup (10h)
            db 16 dup (11h)
            db 16 dup (12h)
            db 16 dup (13h)
            db 16 dup (14h)
            db 16 dup (15h) ; Сектор данных
    CurrentSector dw 0     ; Текущий сектор
    InputBuffer db 20, 0   ; Буфер для ввода строки
    msg db 'Hello, World!$', 0h   ; Строка для вывода
    error_save db 'Error save$', 0h

section .bss
CursorX resb 1
CursorY resb 1
CurrentByte resb 1
CurrentNibble resb 1

section .text
start:
    mov ax, 0x3
    int 0x10         ; Очистка экрана

    ; Основной цикл диспетчера команд
main_loop:
    call get_key
    mov ah, 0x0E        ; BIOS функция для вывода символа
    int 0x10 
    cmp al, '1'     ; Проверка нажатия цифры '1'
    je command_f1
    cmp al, '2'     ; Проверка нажатия цифры '2'
    je command_f2
    cmp al, '3'     ; Проверка нажатия цифры '3'
    je command_f3
    cmp al, '4'     ; Проверка нажатия цифры '4'
    je command_f4
    cmp al, '5'     ; Проверка нажатия цифры '5'
    je command_f5
    cmp al, '6'     ; Проверка нажатия цифры '6'
    je command_f6
    cmp al, '0'     ; Проверка нажатия цифры '0' (для выхода)
    je exit_program
    jmp main_loop

command_f1:
    call display_initial_sector
    jmp main_loop

command_f2:
    call save_sector
    jmp main_loop

command_f3:
    call display_next_sector
    jmp main_loop

command_f5:
    call display_previous_sector
    jmp main_loop

command_f6:
    call display_sector_n
    jmp main_loop

command_f10:
    jmp exit_program

command_f4:
    call edit_sector
    jmp main_loop

exit_program:
    mov ax, 0x4C00
    int 0x21

; Процедура редактирования сектора
edit_sector:
    ; Инициализация курсора
    mov byte [CursorX], 0
    mov byte [CursorY], 0
    mov byte [CurrentByte], 0
    mov byte [CurrentNibble], 0
; Процедура установки курсора на экране
move_cursor:
    ; Вычисление позиции курсора в видео-памяти
    mov ah, 2       ; BIOS функция установки позиции курсора
    mov bh, 0       ; Номер страницы
    mov dh, [CursorY] ; Строка
    mov dl, [CursorX] ; Столбец
    int 0x10        ; Вызов BIOS прерывания
    ret
edit_loop:
    call display_sector
    call move_cursor

    ; Чтение клавиши
    mov ah, 0
    int 0x16

    cmp al, 0x3E   ; <F4>
    je exit_edit

    cmp al, 0x1B   ; <Esc>
    je exit_edit

    cmp al, 0x4D   ; Right arrow
    je move_right

    cmp al, 0x4B   ; Left arrow
    je move_left

    cmp al, 0x50   ; Down arrow
    je move_down

    cmp al, 0x48   ; Up arrow
    je move_up

    ; Проверка на ввод цифры
    cmp al, '0'
    jb edit_loop
    cmp al, 'F'
    ja edit_loop

    ; Редактирование тетрады
    call write_digit_sector
    jmp edit_loop

move_right:
    inc byte [CursorX]
    inc byte [CurrentByte]
    cmp byte [CursorX], 32
    jb edit_loop
    mov byte [CursorX], 0
    inc byte [CursorY]
    jmp edit_loop

move_left:
    dec byte [CursorX]
    dec byte [CurrentByte]
    cmp byte [CursorX], -1
    jae edit_loop
    mov byte [CursorX], 31
    dec byte [CursorY]
    jmp edit_loop

move_down:
    inc byte [CursorY]
    add byte [CurrentByte], 32
    cmp byte [CursorY], 16
    jb edit_loop
    mov byte [CursorY], 0
    jmp edit_loop

move_up:
    dec byte [CursorY]
    sub byte [CurrentByte], 32
    cmp byte [CursorY], -1
    jae edit_loop
    mov byte [CursorY], 15
    jmp edit_loop

exit_edit:
    ret

; Процедура вывода начального сектора на экран
display_initial_sector:
    mov ah, 0x09        ; BIOS функция для вывода строки
    mov dx, msg         ; Адрес строки
    int 0x21            ; Вызов BIOS прерывания
    mov byte [CurrentSector], 0
    call display_sector
    ret

; Процедура сохранения сектора в память
save_sector:
    clc
    ; Установка параметров для записи сектора
    mov ah, 0x03          ; BIOS функция для записи сектора
    mov al, 1             ; Число секторов для записи (1)
    mov ch, 0             ; Номер цилиндра (0)
    mov cl, 2             ; Номер сектора (2)
    mov dh, 0             ; Номер головки (0)
    mov dl, 0x80          ; Номер диска (0x80 - первый жесткий диск)
    mov bx, Sector        ; Адрес буфера с данными сектора
    int 0x13              ; Вызов BIOS прерывания

    ; Проверка ошибки
    jc save_error         ; Если CF установлен, произошла ошибка

    ret

save_error:
    mov ah, 0x09        ; BIOS функция для вывода строки
    mov dx, error_save         ; Адрес строки
    int 0x21            ; Вызов BIOS прерывания
    ; Реализация обработки ошибки сохранения
    ret

; Процедура вывода следующего сектора на экран
display_next_sector:
    inc word [CurrentSector]
    call display_sector
    ret

; Процедура вывода предыдущего сектора на экран
display_previous_sector:
    dec word [CurrentSector]
    call display_sector
    ret

; Процедура вывода сектора N на экран
; Процедура вывода сектора N на экран
display_sector_n:
    call get_sector_number
    call display_sector
    ret

; Процедура ввода номера сектора
get_sector_number:
    mov dx, InputBuffer
    mov ah, 0x0A
    int 0x21             ; Ввод строки с клавиатуры

    ; Преобразование введенной строки в число
    mov bx, InputBuffer + 2  ; Пропустить длину строки и ввод
    xor ax, ax               ; Обнулить регистр AX
    xor cx, cx               ; Обнулить регистр CX

convert_loop:
    mov cl, [bx]             ; Загрузить следующий символ
    cmp cl, 0                ; Проверить конец строки
    je convert_done
    sub cl, '0'              ; Преобразовать символ в число
    add ax, cx               ; Добавить к AX
    mov cx, 10
    mul cx                   ; Умножить на 10 (сдвиг разряда)
    inc bx                   ; Перейти к следующему символу
    jmp convert_loop

convert_done:
    mov [CurrentSector], ax
    ret

;Процедура вывода сектора на экран
display_sector:
    ; Установка начальной позиции курсора
    xor bh, bh          ; Высота экрана (0 для текстового режима)
    mov ah, 2           ; BIOS функция установки позиции курсора
    mov dh, 0           ; Строка (номер начиная с 0)
    mov dl, 0           ; Столбец (номер начиная с 0)
    int 0x10            ; Вызов BIOS прерывания для установки курсора

    mov cx, 512         ; Количество байт для вывода (размер сектора)
    mov si, Sector      ; Указатель на начало сектора

print_loop:
    lodsb               ; Загрузка байта из DS:SI в AL и инкремент SI

    mov ah, 0x0E        ; BIOS функция вывода символа в текстовом режиме
    mov bh, 0           ; Страница экрана
    mov bl, 0x07        ; Цвет символов (стандартный цвет)
    int 0x10            ; Вызов BIOS прерывания для вывода символа

    loop print_loop     ; Повторяем, пока не выведем все 512 байт

;     ret
; display_sector:
;     xor bx,bx ; Обнуление BX
;     mov cx,16 ; Счетчик байтов
;     .M: mov dl, [Sector+bx] ; Получить один байт
;     call Write_byte_hex ; Вывод шестн. числа
;     mov DL, ' ' ; Вывод на экран
;     call Write_char ; пробела
;     inc bx ; Возврат за следующим
;     loop .M ; байтом
;     int 20h ; Возврат в DOS 
; Процедура записи цифры в сектор
write_digit_sector:
    mov bx, [CurrentByte]
    mov al, [Sector + bx]

    ; Преобразование введенной цифры
    cmp al, '9'
    jbe is_digit
    sub al, 7

is_digit:
    sub al, '0'

    ; Редактирование тетрады
    cmp byte [CurrentNibble], 0
    je edit_high_nibble

    ; Редактирование младшей тетрады
    and byte [Sector + bx], 0xF0
    or byte [Sector + bx], al
    jmp end_edit

edit_high_nibble:
    shl al, 4
    and byte [Sector + bx], 0x0F
    or byte [Sector + bx], al

end_edit:
    xor byte [CurrentNibble], 1
    ret

; Процедура инициализации диспетчера команд
init_dispatcher:
    ; Инициализация необходимых переменных и состояния
    ret

; Процедура получения нажатой клавиши
get_key:
    ; Ожидание нажатия клавиши и возврат значения в AL
    mov ah, 0
    int 0x16
    ret