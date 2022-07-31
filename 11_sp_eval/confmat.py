class BinaryConfusionMatrix:
    def __init__(self, pos_tag, neg_tag):
        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
 
    def as_dict(self):
        """
        Return tp, tn, fp, fn as a dictionary
        """
        return {'tp': self.tp, 'tn': self.tn, 'fp': self.fp, 'fn': self.fn}
 
    def update(self, truth, prediction):
        """Compare the truth with the prediction and increment the related counter."""
        if truth != self.pos_tag and truth != self.neg_tag:
            raise ValueError
        if prediction != self.pos_tag and prediction != self.neg_tag:
            raise ValueError
        if truth == prediction:
            if self.pos_tag == prediction:
                self.tp += 1
            else:
                self.tn += 1
        else:
            if self.neg_tag == truth:
                self.fp += 1
            else:
                self.fn += 1
 
    def compute_from_dicts(self, truth_dict, pred_dict):
        """
        Calculates the entire confusion matrix based on the values stored in the dictionaries.
        """
        for i in truth_dict.keys():
            self.update(truth_dict[i], pred_dict[i])
