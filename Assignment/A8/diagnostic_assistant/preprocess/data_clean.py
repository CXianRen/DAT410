import pandas as pd

from diagnostic_assistant.preprocess.load_data import get_symptom_severity


def remove_hyphen(df):
    for col in df.columns:
        df[col] = df[col].str.replace('_', ' ')
    return df


def remove_trailing_spaces(df):
    cols = df.columns
    data = df[cols].values.flatten()

    s = pd.Series(data)
    s = s.str.strip()
    s = s.values.reshape(df.shape)

    return pd.DataFrame(s, columns=df.columns)


def encode_symptoms(df):
    cols = df.columns
    df_severity = get_symptom_severity()
    df_severity['Symptom'] = df_severity['Symptom'].str.replace('_', ' ')

    vals = df.values
    symptoms = df_severity['Symptom'].unique()

    for i in range(len(symptoms)):
        vals[vals == symptoms[i]] = df_severity[df_severity['Symptom'] == symptoms[i]]['weight'].values[0]

    return pd.DataFrame(vals, columns=cols)


def pre_process_data(df):
    df = remove_hyphen(df)
    df = remove_trailing_spaces(df)
    df = df.fillna(0)

    df = encode_symptoms(df)

    # fix no rank to zero
    df = df.replace('dischromic  patches', 0)
    df = df.replace('spotting  urination', 0)
    df = df.replace('foul smell of urine', 0)

    print(df.head())

    return df


def pre_process_diabetes_data(df):
    df = df.fillna(0)
    return df

