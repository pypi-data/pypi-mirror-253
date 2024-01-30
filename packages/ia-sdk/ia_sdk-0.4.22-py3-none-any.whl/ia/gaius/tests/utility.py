from ia.gaius.data_language import CLEAR_WM, LEARN
# from ia.gaius.pvt.pvt_utils import make_modeled_emotives_
from ia.gaius.prediction_models import prediction_ensemble_modeled_emotives
class Tester:

    def __init__(self, **kwargs):
        self.bottle = kwargs['bottle']
        self.utype = kwargs['utype']  # either 'value' or 'polarity'
        self.learning_strategy = kwargs['learning_strategy']

    def next_test_prep(self):
        """Anything to reset in between multiple test runs."""
        return

    def train(self, sequence):
        record = {'phase': 'training', 'historical_expecting': sum([sum(data['emotives'].values()) for data in sequence])}
        self.bottle.clear_wm()
        for data in sequence:
            self.bottle.observe(data)
        self.bottle.learn()
        return record

    def test(self, sequence):
        record = {'phase': 'testing'}
        historical_expecting = sum([sum(data['emotives'].values()) for data in sequence])
        record['historical_expecting'] = historical_expecting
        self.bottle.clear_wm()
        for data in sequence:
            self.bottle.observe(data)

        record['node_predictions'] = {}
        predicton_error = True  # If any of the nodes are right, then don't bother learning if on_error learning strategy is employed.
        hive_prediction = []
        answer = self.bottle.get_predictions()
        # HERE IS WHERE WE MODEL OUR PREDICTIONS #######
        utility_preds = []
        for node, ensemble in answer.items():
            predicted_value = prediction_ensemble_modeled_emotives(ensemble)
            if isinstance(predicted_value, dict) and len(predicted_value) != 0:
                predicted_value = sum(list(predicted_value.values()))/ len(predicted_value)
            else:
                predicted_value = 0
            utility_preds.append(predicted_value)
            record['node_predictions'][node] = predicted_value

        hive_prediction = sum(utility_preds)/len(utility_preds)
        record['node_predictions']['hive'] = hive_prediction
        if hive_prediction == historical_expecting:
            predicton_error = False

        if self.learning_strategy == 'continuous' or (
                self.learning_strategy == 'on-error' and predicton_error):
            # NOTE!: Unlike regular symbols for the classification tests, utilities pass through
            # all nodes, so we don't need to send directly to egress nodes.  Simply send through ingress nodes.
            data = {"strings": [], "vectors": [], "emotives": {'utility': historical_expecting}}
            self.bottle.observe(data)
            self.bottle.learn()
        return record
