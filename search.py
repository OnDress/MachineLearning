import random

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    return random.randint(0,99)

def feature_search(data):
    current_set_of_features = set()
    for i in range(1, len(data.columns)):
        print("On the " + str(i) + "th level of the search tree" )
        feature_to_add_at_level = []
        best_so_far_accuracy = 0
        for k in range(1, len(data.columns)):
            if k not in current_set_of_features:
                print("--Considering adding the " + str(k) + "th feature")
                accuracy = leave_one_out_cross_validation(data,current_set_of_features,k)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_level = k
        current_set_of_features.add(feature_to_add_at_level)
        print("On level " + str(i) + " I added feature " + str(feature_to_add_at_level) + " to current set")
