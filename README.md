# Type Tonic Tip Kontrolü Projesi 🚀

Bu proje, Python'da dinamik özellik yönetimi ve tür doğrulama işlevselliği sağlayan bir `Type` sınıfı içermektedir.

## Özellikler ✨

- **Dinamik Özellik Yönetimi**: Özelliklerin dinamik olarak atanmasına olanak tanır.
- 
- **Tür Doğrulama**: Atanan değerlerin belirli türlerde olmasını sağlar.
  - E-posta adresi doğrulama 📧
  - JSON formatı doğrulama 📄
  - String doğrulama 📝
 
# Örnek Kullanım
from typeTonic import var
i
mport json

Özellik atama

var.isim = "burak"

print(var.isim) 

Liste oluşturma ve güncelleme

var.list = ["burak", "emre"]

print(var.list) 

var.list.append("deneme")

print(var.list)  

JSON doğrulama

var.sendData = {"deneme": "123"}

print(var.isJson(json.dumps(var.sendData)))  


