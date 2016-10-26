shopping_list = ["apple"]
def return_list(shopping_list):
    # print shopping_list
    shopping_list.sort()
    print shopping_list

def check_dupe_item(item):
    if item in shopping_list:
        print "we already have that! try something else."
    else:
        shopping_list.append(item)
    return shopping_list

def remove_item_already_in_list(item):
    if item in shopping_list:
        shopping_list.append(item)
    else:
        print "we DO NOT have that in shopping list! try something else."
    return shopping_list



def main():
    item = "cookies" #raw_input("what should we add to the list?").lower()

        # #if item in shopping_list:
        #     print "we already have that! try something else."
        # else:
        #     shopping_list.append(item)
        #     # print shopping_list
        #     print "We've added " + item + " to your list."
        #     return_list(shopping_list)
    print check_dupe_item(item)
 

if __name__=='__main__':
    main()
