
def sort_asc(lista):
    return sorted(lista)

def sort_desc(lista):
    return sorted(lista,reverse=True)

if __name__ == '__main__':
    lista = [4,7,2,3,4,8,9,10]
    print("Program wykonuje operacje na listach")
  
    while True:
        print("\n-----------------")
        print("Lista: "+str(lista))

        print(" 's' - sortuj malejąco")
        print(" 'S' - sortuj rosnąco")
        print(" 'q' - wyjscie")

        c = input("Wybierz operację: ")
        if c != 'q':
            if c == 's':
                lista = sort_desc(lista)
            elif c == 'S':
                lista = sort_asc(lista)
           
        else:
            break