from googletrans import Translator

translator = Translator()

sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")

from googletrans import Translator

translator = Translator()

result = translator.translate(sentence,'de')
result2 = translator.translate(sentence,'ja')
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print("입력어- ",detected.lang,":",sentence)
print("번역어1 - ",result.dest,":",result.text)
print("번역어2 - ",result2.dest,":",result2.text)
print("=================================")