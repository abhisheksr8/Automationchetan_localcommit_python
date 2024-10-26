from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelineautomationchetan_release_api_1729960391236.config.ConfigStore import *
from pipelineautomationchetan_release_api_1729960391236.functions import *
from prophecy.utils import *
from pipelineautomationchetan_release_api_1729960391236.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Project_Automationchetan_python_RELEASE_API_1729960391236_dataSet = Project_Automationchetan_python_RELEASE_API_1729960391236_dataSet(
        spark
    )
    df_customer_details_selection = customer_details_selection(
        spark, 
        df_Project_Automationchetan_python_RELEASE_API_1729960391236_dataSet
    )

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Pipeline-Automationchetan_RELEASE_API_1729960391236")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline-Automationchetan_RELEASE_API_1729960391236")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Pipeline-Automationchetan_RELEASE_API_1729960391236",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()
