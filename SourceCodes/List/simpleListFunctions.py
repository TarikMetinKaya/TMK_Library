
def deleteValueFromAllList(list, element):
    """
    Usage:
    a=[1,4,2,5,1,1,1,2,6]
    deleteValueFromAllList(a,1)
    Output: [4,2,5,2,6]

    :param list: A list
    :param element: An element which is you want to delete from all list
    :return: Filtered List
    """
    list = [x for x in list if x != element]
    return list

