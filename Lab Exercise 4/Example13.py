#Example No. 13
#Q13:Write a python program to Access the value of key ‘history’ from the following dictionarysampleDict = {
#"class":{
#"student":{
#"name":"Mike",
#"marks":{
#"physics":70,
#"history":80
#}
#}
#}
#}


sampleDict = {
"class":{
"student":{
"name":"Mike",
"marks":{
"physics":70,
"history":80
}
}
}
}
print(sampleDict["class"]["student"]["marks"]["history"])
