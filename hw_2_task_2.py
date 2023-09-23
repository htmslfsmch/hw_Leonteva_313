Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("train.csv", "r")
... spisok = list(f.readlines())
... f.close()
... 
... all = 0
... male = 0
... female = 0
... 
... m = []
... for i in range(1, len (spisok)):
...     m = spisok[i].split(',')
...     if m[1] == '1' and m[5] == 'male':
...         male += 1
...     if m[1] == '1' and m[5] == 'female':
...         female += 1
... all = male + female
... print("общее число выживших:", all , "," " выживших мужчин:", male , "," " выживших женщин:", female)
