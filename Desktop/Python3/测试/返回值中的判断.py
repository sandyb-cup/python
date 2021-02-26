def return_congiration():
    a = 1
    b = None
    c = 2
    d = 3
    return (a) if b else (d) # 如果b是真值那返回的数是a， 如果值是一个false or None 值的话就返回d值
def main():
    v = return_congiration()
    print(v)
if __name__ == "__main__":
    main()
    