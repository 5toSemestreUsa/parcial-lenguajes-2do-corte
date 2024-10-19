
# Dependencies
```antlr4-python3-runtime==4.13.1```
## Intalacion de dependencias
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

# Punto 1 - Calculadora de fraccionarios

Esta calculadora realiza operaciones entre numeros fraccionarios de la forma n/m, y dando un resultado de la misma forma.

IMPORTANTE: El resultado es simplificado al minimo numerador y denominador posible, por ejemplo:
```
>> 12/5 * 5/6  // Daria por resultado en 60/30
2/1
```


tambien es posible realizar algunas operaciones mas complejas por ejemplo:
```
>> (5/3 / ( 3/6 / 9/3 ) * 5/2 - 6/145 * 2/1)
3613/145
```
## How to run
```
$ cd Pt1
$ python3 calc.py
$ type your expression
>> 12/5 * 5/6  
2/1
>> (5/3 / (3/6/9/3)*5/2-6/145 *2/1)
3613/145
```



# Punto 2 - MAP y FILTER
Este programa lo que realiza es ejecutar codigo Python3 dentro de MAP y FILTER, de manera que simula su funcionamiento desde ANTLR4.
De forma que la misma sintaxis de python3 puede ser usada para realizar operaciones y ver su resultado como una lista

## How to run MAP  
```
$ cd Pt1
$ python3 MapMain.py
>> map(lambda x: x + 2, [1, 2, 3, 4])
[3, 4, 5, 6]
>>
>> map(lambda x: x ** 2, (1, 2, 3, 4))
[1, 4, 9, 16]
>>
>> map(lambda x: x % 2 == 0, (1, 2, 3, 4))
[False, True, False, True]
>>
>> map(lambda x: x*2, ("1", "2", "3", "4"))
['11', '22', '33', '44']
>>
>> map(lambda x: x*5, {1,"si",2,"no",3,4,5})
[5, 10, 15, 20, 25, 'nonononono', 'sisisisisi']
>>
>> map(lambda x: x["item"], [{"item":5} ,{"item":12} , {"item":[1,2,3]} , {"item":"hola"} ])
[5, 12, [1, 2, 3], 'hola']
```


## How to run FILTER
```

$ cd Pt1
$ python3 MapMain.py
>> filter(lambda x: x % 2 == 0, (1, 2, 3, 4))
[2, 4]
>>
>> filter(lambda x: True, (1, 2, 3, 4))
[1, 2, 3, 4]
>>
>> filter(lambda x: False, (1, 2, 3, 4))
[]
```


