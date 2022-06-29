import pandas as pd
'''
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark_Application1').getOrCreate()
print(spark)
'''
l_variable = [1, 2, 3, 4, 5]
df = pd.DataFrame(l_variable, columns=['Num'])
print(df)