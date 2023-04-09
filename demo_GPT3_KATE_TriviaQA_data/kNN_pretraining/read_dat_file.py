import pickle

PIK_kNN = "trivia_qa_train_78785_dev_full_random_0.dat"
with open(PIK_kNN, "rb") as f:
    kNN_data = pickle.load(f)
    print(type(kNN_data))
    for key, values in kNN_data.items():
        print("key: ",key)
        print("values: ",values)
    kNN_dev_train = kNN_data["kNN_dev_train"]
    print(kNN_dev_train.shape)
    print(kNN_dev_train[0])