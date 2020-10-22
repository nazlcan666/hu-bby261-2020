def hesapla(kelime, paragraf):
  array = paragraf.split()
  toplam=0
  for klm in array:
      if klm== kelime:
          toplam+=1
  return toplam

text = 'Bir gün, istiklâl ve cumhuriyeti müdafaa mecburiyetine düşersen, vazifeye atılmak için, içinde bulunacağın vaziyetin imkân ve şeraitini düşünmeyeceksin! Bu imkân ve şerait, çok nâmüsait bir mahiyette tezahür edebilir. İstiklâl ve cumhuriyetine kastedecek düşmanlar, bütün dünyada emsali görülmemiş bir galibiyetin mümessili olabilirler.'
arama_sonucu = hesapla('ve', text)

print(arama_sonucu)
 