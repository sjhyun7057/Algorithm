def solution(n, arr1, arr2):
    def change_bin_num(n, arr):
        idx = 0
        bin_n = n 
        for num in arr:
            new_num = ''
            while bin_n > 0:
                bin_n -= 1
                if num//(2**bin_n):
                    num = num%(2**bin_n)
                    new_num += '1'
                else:
                    new_num += '0'
            arr[idx] = new_num
            idx += 1
            bin_n = n
        return arr
    
    arr1, arr2 = change_bin_num(n,arr1), change_bin_num(n, arr2)
    
    shop_list = []
    for bin1, bin2 in zip(arr1, arr2):
        shop = ''         
        for b1, b2 in zip(bin1, bin2):
            if int(b1) or int(b2):
                shop += '#'
            else:
                shop += ' '
        shop_list.append(shop)
    return shop_list
