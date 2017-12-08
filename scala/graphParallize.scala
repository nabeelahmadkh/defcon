import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import scala.util.MurmurHash
import scala.io.Source
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.sql.SparkSession
import org.apache.spark.graphx.GraphLoader

//TESTING CODE
//val df_1 = sqlContext.read.format("com.databricks.spark.csv").option("header", "false").load("../Downloads/2008.csv")
val bufferedSource = io.Source.fromFile("/home/srinivas_thuniki/test.edgelist.csv")
for (line <- bufferedSource.getLines) {
        val colsArray(source, target, extras) = line.split(" ").map(_.trim)
        // do whatever you want with the columns here
        // println(s"${cols(0)}|${cols(1)}|${cols(2)}|${cols(3)}")
    }
bufferedSource.close
~                    

var fileName = "/home/srinivas_thuniki/test.edgelist"
for (line <- Source.fromFile(fileName)){
    val colsArray(source, target, extras) = line.split(" ").map(_.trim)
}
/***************************************************************/
//FOR RUNNING THE FILE FROM THE SCALA SHELL 
:load /home/nabeelahmadkh/graph.sc

//WORKING CODE FOR CREATING A SPARK CONTEXT AND LOADING A FILE 
val conf = new SparkConf().setMaster("local[2]").setAppName("Graph Processing")
val sc = new SparkContext(conf)
val sparkSession = SparkSession.builder.config(conf = conf).appName("spark session example").getOrCreate()
val base_df = sparkSession.read.option("header","false").csv("hdfs://cluster-c60f-m/user/srinivas_thuniki/test.edgelist")
val graph = GraphLoader.edgeListFile(sc, "hdfs://cluster-c60f-m/user/srinivas_thuniki/test.edgelist")

hadoop fs -cat //cluster-c60f-m/user/srinivas_thuniki/test