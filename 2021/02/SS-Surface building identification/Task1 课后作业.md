# Task1

1. 统计所有图片整图中没有任何建筑物像素占所有训练集图片的比例

    ```python
    train_mask['mask'].isnull().sum()/train_mask.shape[0]
    # 0.17346666666666666
    ```

2. 统计所有图片中建筑物像素占所有像素的比例

    ```python
    from tqdm.notebook import tqdm
    import numpy as np
    from PIL import Image

    train_mask["mask"]=train_mask["mask"].fillna("")
    l = len(train_mask)

    ratio_ls = []
    for i in tqdm(range(l)):
        if train_mask["mask"].iloc[i]!="":
            number = np.array(train_mask["mask"][i].split(" ")).astype('int')[1::2].sum()
            pic_path = PATH + "train/" + train_mask["name"].iloc[i]
            pic = np.array(Image.open(pic_path))
            ratio = number/(pic.shape[0]*pic.shape[1])
        else:
            ratio = 0

        ratio_ls.append(ratio)

    pd.Series(ratio_ls).mean()
    # 0.15708140207926433
    ```

3. 统计所有图片中建筑物区域平均区域大小

    ```python
    train_mask["mask"]=train_mask["mask"].fillna("")
    l = len(train_mask)

    sum_ls = []
    for i in tqdm(range(l)):
        if train_mask["mask"].iloc[i]!="":
            number = np.array(train_mask["mask"][i].split(" ")).astype('int')[1::2].sum() 
        else:
            number = 0

        sum_ls.append(number)

    pd.Series(sum_ls).mean()
    # 41177.94706666667
    ```