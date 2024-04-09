import randomgenerator
def ask_min_max_numbers():
    min_num = int(input("Enter a number between 1 and 100: "))
    max_num = int(input("Enter a number between 1 and 100: "))
    if(min_num <= max_num):
        print(min_num,max_num)
    return min_num,max_num



def select_random_number(min, max):
    min = int(input("Enter a number between min and max: "))
    max = int(input("Enter a number between min and max: "))
    data=randomgenerator.RandomNumber()
    val=data.randrange(min,max)
    print(val)
    user_input = input('Do you like number (yes/no): ')
    if user_input.lower() == 'yes':
        print('User typed yes')
    elif user_input.lower() == 'no':
        print('User typed no')
    else:
        print('Type yes or no')

    """
    Generate inside an infinite loop a random value between min and max. 
    Show it to the user. Only retur the value when the user answers 'yes'. 

    """
    '''Start een oneindige loop waarin je een random getal genereert tussen min en max.
    Toon het nummer en vraag of dit getal geselecteerd moet worden
    Indien de gebruiker 'yes' ingeeft, retourneer je het getal. 
    In alle andere gevallen zeg je dat je een een nieuw getal gaat maken en je blijft in de loop.
    '''
    return val  # fixture


def main():
    min, max = ask_min_max_numbers()
    number = select_random_number(min, max)
    message = 'number is: '+str(number)  # pretty print the result
    print(message)

if __name__ == '__main__':
    main()
