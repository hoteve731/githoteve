# 딜리트(리무브) 후 어팬드 하는 버전 (아마 출제의도는 이 방향인 것 같습니다.)
# 예를 들어 음식1 - 음식2 상태에서 음식1을 다시 입력하면 기존 음식1이 지워지고 리스트에 음식2-음식1 순서대로 다시 추가됨

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
        foodlist.remove(menu)
        foodlist.append(menu)

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