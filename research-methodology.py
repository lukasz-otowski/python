problem = [
    'facts review',
    'recognize problem',
    'putting the problem'
    ]
theoretic_model = [
    'choosing important factors',
    'ejecting central hypothesis and also ancillary assumptions about dependency between factors',
    'if it is possibly, expression a model in mathematical and logical language'
    ]
detail_hypothesis = [
    'searching consequences of theory which will may be verified',
    'put forecasts'
    ]
check_hypothesis = [
    'planning a method of verification forecasts',
    'execute verification',
    'systematization the data',
    'eject conclusions from research'
    ]
inject_new_result = [
    'executing a comparison between conclusions and forecasts',
    'modification of the model',
    'derive suggestion for further researches'
    ]

methodology = [problem, theoretic_model, detail_hypothesis, check_hypothesis, inject_new_result]


def write_methodology(list):
    for i in list:
        print('\n')
        for write in i:
            print(write)

write_methodology(methodology)
