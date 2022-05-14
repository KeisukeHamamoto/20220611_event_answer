def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    # 配列の先頭を格納
    left = 0
    # 配列の終端を格納
    right = len(sorted_array)-1

    while left <= right:
        # 配列の中心値を格納
        center = (left + right) //2
        # 探索対象をピンポイントで見つけたら返却そうでない場合は範囲を狭めていく
        if sorted_array[center] == target_number:
            return center
        elif sorted_array[center] > target_number:
            right = center - 1
        else:
            left = center + 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
