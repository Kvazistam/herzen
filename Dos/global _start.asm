global _start

section .data
input_message_ax: db "ВВЕДИТЕ СОДЕРЖИМОЕ РЕГИСТРА AX ",24
input_message_dx: db "ВВЕДИТЕ СОДЕРЖИМОЕ РЕГИСТРА DX",10,24
output_message_ax: db "AX = ",10,24
output_message_dx: db " DX = ",24

section .text

_start:
	xor ax,ax
	xor dx,dx
	mov ah,09
	mov dx, output_message_ax
	int 21
	mov ah,09
	mov dx, output_message_ax
	int 21
	call .input_hex
	call .input_hex
	mov bl,24
	mov ah,2
	int 21
	call .input_hex
	call .input_hex
	mov bl,24
	mov ah,2
	int 21
	pop bx
	pop ax
	mov ah, al
	add ax, bx
	pop bx
	pop dx
	mov dh, dl
	add dx, bx
	call .print_bin
	ret

	ret
.print_bl:
	push ax
	push bx
	xor bx,bx
	mov bl,al
	mov ah,2
	push bx
	pop ax
	pop bx
	ret
.input_hex:
	push ax
	push dx
.start_hex
	mov ah,8
	int 21
	mov dl,al
	cmp al,30
	jb .error_value
	cmp al,39
	ja .al_grant_39
.print_char:
	jc .start_hex
	xor bx,bx
	mov bl,al
	mov ah,2
	int 21
	push bx
	pop dx
	pop ax
	ret

.error_value:
	stc
	jmp .start_hex
	
.al_grant_39:
	cmp al,41
	jb error_value
	cmp al,46
	ja .error_value
	sub al,37
	clc
	jmp .print_char
 
.print_bin
	push ax
	push dx
	mov si, ax
	mov di, dx
	xor ax,ax
	xor dx,dx
	mov ah,09
	mov dx, output_message_ax
	int 21
	mov ah,02
	mov cx, 10
.print_bin_si	
	mov dl, 00
	rcl si,1
	adc dl,30
	int 21
	loop .print_bin_s
	mov ah,09
	mov dx, output_message_dx
	int 21
	mov ah,02
	mov cx, 10
.print_bin_di
	mov dl, 00
	rcl di,1
	adc dl,30
	int 21
	loop .print_bin_di
	pop dx
	pop ax
	ret


