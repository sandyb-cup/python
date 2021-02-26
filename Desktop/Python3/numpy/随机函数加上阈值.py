import numpy as np
def test_computer():
    
    np.random.seed(1)

    arr_num = np.random.rand(10,1) # 随机在0到1之间取值 值的分布符合高斯分布
    
    print(arr_num)

    arr_lim = arr_num < 0.5 # 设置一个阈值 如果这个随机值小于这个阈值的返回一个bool值 False or True

    arr_multiply_num = np.random.rand(10, 1)

    arr_multiply_num_result = arr_lim * arr_multiply_num #  他的随机失活值符合高斯分布
    
    
    return arr_multiply_num_result
def test_seed():
    np.random.seed(1)
    
    arr_num = np.random.rand(10, 1)
    
    print(arr_num)

def main():
    test_computer()
    test_seed()
if __name__ == '__main__':
    main()
    
    



