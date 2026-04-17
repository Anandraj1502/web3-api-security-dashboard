from sklearn.ensemble import IsolationForest
def train_model(X):
    m=IsolationForest(n_estimators=100,contamination=0.07,random_state=42)
    m.fit(X)
    return m
def predict(m,X):
    return m.predict(X)
