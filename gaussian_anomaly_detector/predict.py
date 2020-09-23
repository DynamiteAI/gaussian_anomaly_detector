import os
import hashlib

import joblib
import pandas

from gaussian_anomaly_detector import const


def predict_gaussian_anomaly_detector(input_df: pandas.DataFrame, domain: str, train_fields=(), include_fields=()):
    """

    :param input_df: The input dataframe
    :param domain: The domain (model name)
    :param train_fields: The features (numeric only)
    :param include_fields: The fields to include with the prediction (for correlation)

    :return: A list of predictions with included fields
    """
    feature_group_id = hashlib.md5(str(list(train_fields).sort()).encode()).hexdigest()
    drop_fields = [field for field in input_df.columns if field not in train_fields]
    train_df = input_df.drop(drop_fields, axis=1)

    model_directory = os.path.join(const.DYNAMITE_CONF_ROOT, 'models', 'gaussian_anomaly_detector', feature_group_id)
    model_pkl_file = os.path.join(model_directory, domain + '.pkl')

    model = joblib.load(model_pkl_file)
    predictions = model.predict(train_df)
    reasons = model.get_reason()
    include_fields_lists = []
    for field in include_fields:
        include_fields_lists.append(input_df[field].tolist())
    return zip(predictions, reasons, *include_fields_lists)
