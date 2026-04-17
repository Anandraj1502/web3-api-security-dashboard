from sklearn.preprocessing import LabelEncoder, MinMaxScaler
def preprocess_data(df):
    df=df.copy()
    le=LabelEncoder()
    df['request_type']=le.fit_transform(df['request_type'])
    df['api_key']=le.fit_transform(df['api_key'])
    X=df[['chain_id','request_type','api_key','oracle_latency','chain_latency']]
    return MinMaxScaler().fit_transform(X)
