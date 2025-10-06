def addthreenumbers(n1=0, n2=0, n3=0):
    return n1 + n2 + n3

def subtracttwonumbers(n1=0, n2=0):
    return n1 - n2

def multiplythreenumbers(n1=1, n2=1, n3=1):  # fixed n3=1
    return n1 * n2 * n3

def dividetwonumbers(n1, n2):
    try:
        return n1 / n2   # fixed from 1/2 → actually divide inputs
    except ZeroDivisionError:
        print("Error! Can't divide by zero")
        return None
    except ValueError:
        print("Error! Not a numerical value")
        return None
    except Exception as e:
        print(f"Error! {e}")
        return None
