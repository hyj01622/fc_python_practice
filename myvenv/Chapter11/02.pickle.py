import pickle

# 피클 저장
data = {
    "plan1" : 'do something',
    "plan2" : 'do anything'
}

f = open('data.pickle', 'wb')

pickle.dump(data, f)

f.close()



# # 피클 읽기
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)
