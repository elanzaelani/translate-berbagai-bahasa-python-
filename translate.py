from googletrans import Translator

translator = Translator()
text = input("Masukan Text :")
bahasa = input("Terjemahkan Ke bahasa(ar,en,ja,ko,id): ")
hasil = translator.translate(text,dest=bahasa)

print ("Dari",hasil.src, ":",text)
print ("ke",hasil.dest ,":", hasil.text)
print("Dibaca :", hasil.pronunciation)
