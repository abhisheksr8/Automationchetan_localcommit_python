from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipelineautomationchetan_release_api_1730176548837.config.ConfigStore import *
from pipelineautomationchetan_release_api_1730176548837.functions import *

def customer_details_selection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        col("email"), 
        col("country_code"), 
        col("account_open_date"), 
        col("account_flags")
    )
