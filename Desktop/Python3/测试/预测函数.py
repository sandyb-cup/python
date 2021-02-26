def predict(Y, Y_pre):
    y_code = 0
    assert len(Y)==len(Y_pre),'y的维度与预测值维度不一致！！'
    AssertionError:'y的维度与预测值维度不一致！！'
    for y in range(int(len(Y))):
        if Y[y] == Y_pre[y]:
            y_code+=1
    predict_num = y_code/len(Y)
    print('Y_predict is ',predict_num)                                                                                                                                                                                                                                                                                                                                                                                                                                                         
Y = [1,2,3,4]
Y_pre = [2,3,3,1]
def main():
    predict(Y, Y_pre)
if __name__ == '__main__':
    main()
