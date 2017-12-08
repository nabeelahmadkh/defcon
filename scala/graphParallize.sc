import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import scala.util.MurmurHash
import scala.io.Source

//val df_1 = sqlContext.read.format("com.databricks.spark.csv").option("header", "false").load("../Downloads/2008.csv")
val bufferedSource = io.Source.fromFile("/home/srinivas_thuniki/test.edgelist.csv")
for (line <- bufferedSource.getLines) {
        val colsArray(source, target, extras) = line.split(" ").map(_.trim)
        // do whatever you want with the columns here
        // println(s"${cols(0)}|${cols(1)}|${cols(2)}|${cols(3)}")
    }
bufferedSource.close
~                    