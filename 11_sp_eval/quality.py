import utils
import confmat
 
 
def compute_quality_for_corpus(corpus_dir):
    """
    Сalculates the quality of predictions in the corpus
    Return filter score
    """
    truth = utils.read_classification_from_file(corpus_dir + '/' + '!truth.txt')
    prediction = utils.read_classification_from_file(corpus_dir + '/' + '!prediction.txt')
    CM = confmat.BinaryConfusionMatrix('SPAM', 'OK')
    CM.compute_from_dicts(truth, prediction)
    result = CM.as_dict()
    return quality_score(result['tp'], result['tn'], result['fp'], result['fn'])
 
 
def quality_score(tp, tn, fp, fn):
    """
    Return filter score
    """
    result = tp + tn + 10 * fp + fn
    return (tp + tn) / result
