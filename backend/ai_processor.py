import numpy as np
from sklearn.ensemble import IsolationForest

def process_events(events):
    data = np.array(events)
    model = IsolationForest(n_estimators=100, contamination=0.1)
    predictions = model.fit_predict(data)
    return [event for i, event in enumerate(events) if predictions[i] == 1]
