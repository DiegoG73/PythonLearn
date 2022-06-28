#Removing repeated elements with sets
def removing_duplicates(theList):
    return(set(theList))

def run():
    thatList = [1,1,2,3,3,4,4]
    print(removing_duplicates(thatList))

if __name__ == '__main__':
    run()