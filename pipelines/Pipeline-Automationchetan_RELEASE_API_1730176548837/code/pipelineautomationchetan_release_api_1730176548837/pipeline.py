from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelineautomationchetan_release_api_1730176548837.config.ConfigStore import *
from pipelineautomationchetan_release_api_1730176548837.functions import *
from prophecy.utils import *
from pipelineautomationchetan_release_api_1730176548837.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Project_Automationchetan_python_RELEASE_API_1730176548837_dataSet = Project_Automationchetan_python_RELEASE_API_1730176548837_dataSet(
        spark
    )
    df_customer_details_selection = customer_details_selection(
        spark, 
        df_Project_Automationchetan_python_RELEASE_API_1730176548837_dataSet
    )

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Pipeline-Automationchetan_RELEASE_API_1730176548837")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline-Automationchetan_RELEASE_API_1730176548837")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Pipeline-Automationchetan_RELEASE_API_1730176548837",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()
