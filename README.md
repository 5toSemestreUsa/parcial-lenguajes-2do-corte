
# Dependencies
```antlr4-python3-runtime==4.13.1```

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



# How to run
```
% cd Pt1
% python3 calc.py
% type your expression
>> 12/5 * 5/6  
2/1
>> (5/3 / (3/6/9/3)*5/2-6/145 *2/1)
3613/145

% python calc.py t.expr
193
17
9
```