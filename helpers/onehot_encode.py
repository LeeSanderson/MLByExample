import pandas as pd 

def onehot_encode(df : pd.DataFrame, column_name: str) -> tuple[pd.DataFrame, list[str]]:
    categories = [f"{column_name}_{value}" for value in df[column_name].unique()]

    # remove the categorical variables (if we previous called onehot_encode)
    df = df.drop(categories, axis=1, errors="ignore") 
    temp_column_name = f"{column_name}_Temp"

    # get_dummies will remove the original column, so copy the data to temp column
    df[temp_column_name] = df[column_name] 
    df = pd.get_dummies(df, prefix=column_name, columns=[temp_column_name], dtype=float)
    return df, categories