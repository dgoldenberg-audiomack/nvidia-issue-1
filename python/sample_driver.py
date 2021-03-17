import sys

from pyspark.sql import SparkSession


def main(args):
    spark = SparkSession.builder.appName("my_app").getOrCreate()

    print()
    print("Hello, world!")
    print()

    spark.stop()


if __name__ == "__main__":
    main(sys.argv)

