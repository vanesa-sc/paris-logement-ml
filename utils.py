def data_process(df):


    if df == '1946-1970':

        return 1

    elif df == '1971-1990':

        return 2

    elif df =='Apres 1990':

        return 3

    else:

        return 4
    #df.replace({'1946-1970':'1', '1971-1990':'2','Apres 1990':'3', 'Avant 1946':'4'})

    #df.astype(int)



def data_procees_1(string):

    if string == 'meublé':

        return 1

    else:

        return 0
