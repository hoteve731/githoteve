# 딜리트 하지 않고, 중복일 경우 메뉴를 리스트에 추가 자체를 시키지 않는 버전

import random
import time

print ('5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요. 동일한 메뉴는 안돼요!')
print ()

foodlist = []

while True:
    menu = input ('메뉴추가: ')

    if menu not in foodlist:
        foodlist.append(menu)
        print ('현재 메뉴 수 = ', len(foodlist))
        print ()
    else:
        print ('이미 있는 메뉴에요! 다른 메뉴를 입력해주세요') 
        print ('현재 메뉴 수 = ', len(foodlist))
        print()
        continue
        
    
    if len(foodlist) > 4:
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print()
        print(foodlist)
        print('과연 오늘의 메뉴는?')

        print()
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print()

        randomnumber = [1,2,3,4,5]
        foodnumber = random.choice(list(randomnumber))-1
        

        print('오늘의 메뉴는', foodnumber + 1, '번째 메뉴,', foodlist[foodnumber], '입니다.' )
        print()
        break