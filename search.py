import random
import math

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correct = 0
    columns = []
    for num in current_set:
        columns.append(num)
    columns.append(feature_to_add)
    for i in range(0,len(data.index)):
        object_to_classify = data.iloc[i,columns]
        label_object_to_classify = data.iloc[i,0]
        nearest_neighbor_label = 0

        nearest_neighbor_distance = float("inf")
        nearest_neighbor_location = float("inf")
        for k in range(0,len(data.index)):
            if k != i:
                comparison = data.iloc[k,columns]
                sum = 0
                for l in range(0,len(comparison.index)):
                    sum += (float(object_to_classify.iloc[l]) - float(comparison.iloc[l]))**2
                distance = math.sqrt(sum)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data.iloc[nearest_neighbor_location,0]
        if label_object_to_classify == nearest_neighbor_label:
            number_correct += 1
    return number_correct/data.shape[0]

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
                print(accuracy)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_level = k
        current_set_of_features.add(feature_to_add_at_level)
        print("On level " + str(i) + " I added feature " + str(feature_to_add_at_level) + " to current set")
