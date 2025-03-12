

target_number =5 


attempts = 3  

for attempt in range(attempts):
    user_input = int(input("أدخل رقمًا: "))

    if user_input == target_number:
        print("مبروك! لقد أدخلت الرقم الصحيح.")
        break
    elif user_input > target_number:
        print("لقد أدخلت رقمًا أكبر.")
    else:
        print("لقد أدخلت رقمًا أصغر.")
    
    if attempt < attempts - 1:
        print("حاول مرة أخرى.")
    else:
        print("انتهت المحاولات. الرقم الصحيح هو:", target_number)

