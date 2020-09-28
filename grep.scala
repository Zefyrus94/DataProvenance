import org.apache.spark.SparkContext
import org.apache.spark.lineage.LineageContext._
import org.apache.spark.lineage.LineageContext
import org.apache.spark.util.collection.CompactBuffer

    val logFile = "lineage/src/test/resources/README.md"
    val lc = new LineageContext(sc)
    lc.setCaptureLineage(true)
    val lines = lc.textFile(logFile, 2)
    val result = lines.filter(line => line.contains("spark"))
    //assert(result.collect().size == 11)
    print(">>>result's size: "+result.collect().size+"\n")
    //System.exit(1)
    lc.setCaptureLineage(false)
    var linRdd = result.getLineage()
    linRdd = linRdd.filter(_ == 0L)
    print(">>>linRdd: "+linRdd.collect()(0)+"\n")
    //assert(linRdd.collect()(0) == (0, (0, 9)))
    linRdd = linRdd.goBack()
    print(">>>linRdd: "+linRdd.collect()(0)+"\n")
    //assert(linRdd.collect()(0) == ((0, 9), 0))
    print(">>>linRdd: "+linRdd.show.collect()(0)+"\n")
    //assert(linRdd.show.collect()(0) == "<http://spark.apache.org/>")
    linRdd = linRdd.goNext()
    print(">>>linRdd: "+linRdd.collect()(0)+"\n")
    //assert(linRdd.collect()(0) == (0, 9))
