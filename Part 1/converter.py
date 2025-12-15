def main():
    print("Стандартный конвертер v2")
    
    while True:
        print("\nВыберите действие:")
        print("1. DEC -> BIN/HEX")
        print("2. HEX -> DEC/BIN")
        print("3. Сложение двоичных чисел")
        print("4. Выход")
        
        choice = input("Ваш выбор: ")
        
        try:
            if choice == '1':
                num = int(input("Введите число (DEC): "))
                print(f"BIN: {bin(num)[2:]}")
                print(f"HEX: {hex(num)[2:].upper()}")
                
            elif choice == '2':
                hex_val = input("Введите число (HEX): ")
                dec_val = int(hex_val, 16)
                print(f"DEC: {dec_val}")
                print(f"BIN: {bin(dec_val)[2:]}")
                
            elif choice == '3':
                bin1 = input("Введите первое число (BIN): ")
                bin2 = input("Введите второе число (BIN): ")
                sum_dec = int(bin1, 2) + int(bin2, 2)
                print(f"Сумма (BIN): {bin(sum_dec)[2:]}")
                
            elif choice == '4':
                break
            else:
                print("Неверная команда.")
                
        except ValueError:
            print("Ошибка ввода.")

if __name__ == "__main__":
    main()