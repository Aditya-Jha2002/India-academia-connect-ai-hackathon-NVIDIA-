import pandas as pd
from sklearn.model_selection import StratifiedKFold
import os

if __name__ == '__main__':
    input_path = '/Users/sunita/Documents/Nvidia-Hackathon-Dataset/input/'
    df = pd.read_csv(os.path.join(input_path,'train.csv'))
    df['kfold'] = -1
    df = df.sample(frac = 1).reset_index(drop=True)
    y = df.label.values
    kf = StratifiedKFold(n_splits = 5)
    for fold_, (_, _) in enumerate(kf.split(X=df, y=y)):
        df.loc[:,"kfold"] = fold_,
    df.to_csv(os.path.join(input_path, "train_folds.csv"), index = False)