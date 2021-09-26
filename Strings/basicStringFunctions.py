
def setStringLength(string,length,align:"left"):
    """

    :param string: A str which is you want to set length
    :param length: Integer
    :param align: left, mid or right
    :return:
    """

    real_str_len=len(string)
    if real_str_len<length:

        if align=="left":
            text_which_add=""
            for i in range(0,length-real_str_len):
                text_which_add += " "
            return string + text_which_add

        elif align=="right":
            text_which_add = ""
            for i in range(0, length - real_str_len):
                text_which_add += " "
            return text_which_add + string

        elif align=="mid":
            left_text=""
            rigth_text=""
            for i in range(0, (length - real_str_len)):
                if i%2==0:
                    left_text += " "
                elif i%2==1:
                    rigth_text += " "
            return left_text + string + rigth_text

        if not align in ("left", "mid", "right"):
            print("Align must be \"left\", \"mid\" or \"right\" !!")
            return



    elif real_str_len>length:
        print("kesilecek")
    #TODO: string ifadenin içierisinde dizi gibi gezin mid için de hangisi ortaysa o indexten başla falan bir sağ bir sol saf matematik



print(setStringLength("naber",7,align="mid"))