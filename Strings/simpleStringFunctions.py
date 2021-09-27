
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

        if align not in ("left", "mid", "right"):
            print("Align must be \"left\", \"mid\" or \"right\" !!")
            return



    elif real_str_len>length:

        if align=="left":
            return string[0:length]
        elif align=="right":
            return string[-(length):]
        elif align=="mid":
            mid_index_of_text=int(real_str_len/2)
            if length%2==0:
                left_length=int(length/2)
                rigth_length=int(length/2)
            elif length%2==1:
                left_length=int(length/2)+1
                rigth_length=int(length/2)

            var_x=int(mid_index_of_text-left_length+1)
            var_y=int(mid_index_of_text+rigth_length+1)

            return string[var_x:var_y]
        if not align in ("left", "mid", "right"):
            print("Align must be \"left\", \"mid\" or \"right\" !!")
            return

def addCharOnString(string,char,amount,type:"pre-post"):
    """

    :param string: Text is which you want to add smth pre, post or both
    :param char: Must be just one character
    :param amount: int
    :param type: pre, post, pre-post
    :return:
    """
    if type not in ("pre","post","pre-post"):
        print("Type must be \"pre\", \"post\" or \"pre-post\" !!")
        return
    if not len(char)==1:
        print("Lenght of char must be 1")
    text_which_add=""
    for i in range(0,amount):
        text_which_add += f"{char}"
    if type == "pre":
        return text_which_add+string
    elif type == "post":
        return string+text_which_add
    elif type == "pre-post":
        return text_which_add+string+text_which_add

