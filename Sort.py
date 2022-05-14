def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # 配列の左端を格納
    i = 0
    # 配列の右端を格納
    j = len(array) - 1

    # 左端が右端より小さい間ループ
    while(i < j):
        # 配列左端から基準値以上の要素を探索
        while(array[i] < pivot):
            i += 1
        # 配列の右端から基準値未満の要素を探索
        while(array[j] > pivot):
            j -= 1
        
        # 探索した要素を交換
        if(i < j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        else:
            break
    
    # 配列がこれ以上分割できないときは終了
    if not array[:i] or not array[i+1:]:
        return array
    # 再帰的に分割した領域をソートする
    else:
        array[:i] = sort(array[:i])
        array[i+1:] = sort(array[i+1:])
    
    return array
    # ここまで記述

if __name__ == '__main__':
    main()
