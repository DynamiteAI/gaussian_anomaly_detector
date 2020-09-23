import typing
import pandas

from dynamite_analyzer_framework import analyzers
from dynamite_analyzer_framework.inputs import Input
from dynamite_analyzer_framework.outputs import Message, Output

from gaussian_anomaly_detector import train, predict

GaussianAnomalyDetectorAnalyzerClassType = typing.TypeVar('GaussianAnomalyDetectorAnalyzerClassType')


class GaussianAnomalyDetectorAnalyzer(analyzers.Analyzer):

    def __init__(self, input_inst: Input, output_inst: Output, load_model=True, domain='main',
                 train_fields=('duration', 'orig_bytes', 'resp_bytes'),
                 include_fields=('uid', 'community_id', 'duration', 'orig_bytes', 'resp_bytes')):
        self.train_fields = train_fields
        self.include_fields = include_fields
        self.load_model = load_model
        self.domain = domain
        super(GaussianAnomalyDetectorAnalyzer, self).__init__(input_inst, output_inst)

    def evaluate(self) -> GaussianAnomalyDetectorAnalyzerClassType:
        input_df = pandas.DataFrame(self.input.data)
        if self.load_model:
            predictions = predict.predict_gaussian_anomaly_detector(input_df, domain=self.domain,
                                                                    train_fields=self.train_fields,
                                                                    include_fields=self.include_fields)
        else:
            train.train_gaussian_anomaly_detector(input_df, domain=self.domain, train_fields=self.train_fields)
            predictions = predict.predict_gaussian_anomaly_detector(input_df, domain=self.domain,
                                                                    train_fields=self.train_fields,
                                                                    include_fields=self.include_fields)

        for prediction in list(predictions):
            prediction_dict = dict(
                score=prediction[0],
                reason=prediction[1]
            )

            for i in range(0, len(self.include_fields)):
                prediction_dict[self.include_fields[i]] = prediction[i + 2]
            self.output.add_message(
                Message(dataset_name=self.domain, score=prediction_dict['score'], msg=prediction_dict['reason'],
                        data_extra=prediction_dict))
        return self
