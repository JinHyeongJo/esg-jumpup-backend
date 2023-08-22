import math

# 커피자판기

coffee_options = {  
    "1" : {'name' : "아메리카노" , 'price' : 2500},
    "2" : {'name' : "까페라떼" , 'price' : 3000},
    "3" : {'name' : "카라멜 마끼야또" , 'price' : 4000}
}

print("     [메뉴표]")

for key, value in coffee_options.items():
    print(key, ':' ,  value)

coffee_choice = input("메뉴선택 : ")
while coffee_choice not in coffee_options:
    print("invalid menu, choose again")
    coffee_choice = input("메뉴선택 : ")

input_money = int(input("투입금액 : "))
price = coffee_options[coffee_choice].get('price')
name = coffee_options[coffee_choice].get('name')
change = input_money -price
a=500
print(f'잔돈 {a}')
if change < 0 :
    print("금액이 부족합니다")
elif change > 0 :    
    print(f"감사합니다 잔액: {change} ")
elif change == 0:
    print(f"감사합니다 {change}나왔습니다")









        


