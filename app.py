from typeTonic import var
import json

var.isim = "burak"
print(var.isim)

var.list = ["burak","emre"]
print(var.list)
var.list.append("deneme")
print(var.list)
var.sendData = {"deneme":"123"}

print(var.isJson(json.dumps(var.sendData)))

