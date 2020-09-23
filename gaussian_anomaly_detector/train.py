import os
import hashlib

import joblib
import pandas

from gaussian_anomaly_detector import const
from gaussian_anomaly_detector.gaussian_anomaly_detector import GaussianAnomalyDetector


def makedirs(path, exist_ok=True):
    if exist_ok:
        if not os.path.exists(path):
            os.makedirs(path)
    else:
        os.makedirs(path)


def train_gaussian_anomaly_detector(input_df: pandas.DataFrame, domain: str, train_fields=(), contamination=0.05,
                                    log_transform=True):
    """
    :param input_df: The input dataframe
    :param domain: The domain (model name)
    :param train_fields: The features (numeric only)
    :param contamination: The amount of contamination of the data set, i.e. the proportion of outliers in the data set.
                          Used when fitting to define the threshold on the decision function
    :param log_transform: If True, then dataset will log (to base e) transformed
    """

    feature_group_id = hashlib.md5(str(list(train_fields).sort()).encode()).hexdigest()
    drop_fields = [field for field in input_df.columns if field not in train_fields]
    train_df = input_df.drop(drop_fields, axis=1)

    model_directory = os.path.join(const.DYNAMITE_CONF_ROOT, 'models', 'gaussian_anomaly_detector', feature_group_id)
    model_pkl_file = os.path.join(model_directory, domain + '.pkl')

    makedirs(model_directory)

    model = GaussianAnomalyDetector(contamination=contamination, log_transform=log_transform)

    joblib.dump(model.fit(train_df), model_pkl_file)
