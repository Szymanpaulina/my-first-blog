print("Hello, Django girls!")
print('Hello, Paulina!')
if 3 > 2:
    print("To dziala!")
    if 5 > 2:
        print('5 jest jednak większe od 2')
    else:
        print('5 nie jest większe od 2')
name = 'Sonja'
if name == 'Ola':
    print('Hej OLa!')
elif name == 'Sonja':
    print('Hej Sonia!')
else:
    print('Hej nieznajoma!')
glosnosc = 57
if glosnosc < 20:
    print('Prawie nic nie słychać.')
elif 20 <= glosnosc < 40:
    print('O muzyka leci w tle.')
elif 40 <= glosnosc < 60:
    print('Ideanie, mogę usłyszeć wszystkie detale')
elif 60 <= glosnosc < 80:
    print('Dobre na imprezy')
elif 80 <= glosnosc < 100:
    print('Troszeczkę z głośno!')
else:
    print('Ojoj! Moje uszy! :(')



def hej():
    print('Hej')
    print('Jak się masz?')


hej()


def hej(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonia':
        print('Hej Sonia!')
    else:
        print('Hej nieznajoma')


hej('Paulina')



def hej(imie):
    print('Hej ' + imie + '!')


hej('Paulina')





def hej(imie):
    print('Hej ' + imie + '!')


dziewczyny = ['Rachel' , 'Monica' , 'Phoebe' , 'Ola' , 'Paulina']

for imie in dziewczyny:
    hej (imie)
    print('Kolejna dziewczyna')
