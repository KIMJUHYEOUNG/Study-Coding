from pyspark import SparkContext

sc = SparkContext()

path = r"C:\Users\KJH\Desktop\spark\20news-bydate-train/*"

#rdd = sc.wholeTextFiles(path)
text = rdd.map()
print(text.count)
# Out: [0, 2, 4, 6, 8, 10, 12, 14,# 16, 18]