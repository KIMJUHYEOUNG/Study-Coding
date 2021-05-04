이 pdf는 빅데이터분석 강의 때 만든 자료입니다. 연구 중인 도메인과 spark를 처음 사용했기 때문에 시간이 오래 걸렸습니다.  

# Advanced Text Processing with Spark
언어는 Spark를 사용하였고 feature hashing로 임베딩을 진행하였습니다. 전처리 작업 후에는 TF-IDF 알고리즘을 사용하여 각 문서에서 중요한 단어에 높은 가중치를 부여합니다. 
![image](https://user-images.githubusercontent.com/37894081/116959103-8db00000-acd7-11eb-8194-b705ab213f34.png)
![image](https://user-images.githubusercontent.com/37894081/116959120-96083b00-acd7-11eb-81db-5e6065162621.png)


# Word2vec
NLP에서 딥러닝을 사용하는 가장 기본적인 알고리즘입니다. 훈련은 hidden layer 1개를 사용하며, loss function은 cross-entropy를 사용합니다. 훈련을 통해 문장에서 다음에 들어올 단어를 예측합니다.
![image](https://user-images.githubusercontent.com/37894081/116959081-7d982080-acd7-11eb-8341-d53b207acff6.png)
