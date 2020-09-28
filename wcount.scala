import org.apache.spark.SparkContext
import org.apache.spark.lineage.LineageContext
import org.apache.spark.lineage.LineageContext._
import org.apache.spark.util.collection.CompactBuffer
//import org.apache.spark.lineage.rdd.Lineage//for casting
    //val logFile = "lineage/src/test/resources/README.md"
    val logFile = "wcount.txt"
    var lc = new LineageContext(sc)
    lc.setCaptureLineage(true)
    // Job
    val file = lc.textFile(logFile, 2)
    val r1=file.collect
    lc.setCaptureLineage(false)
    print("============================\n>>start 1st test\n")
    val l1=file.getLineage()
    val l2=l1.goBack()
    val r2=l2.collect
    val rr1=l2.show
    print(">>end 1st test\n============================\n")
    
    lc.setCaptureLineage(true)
    val file = lc.textFile(logFile, 2)
    val pairs = file.flatMap(line => line.trim().split(" ")).map(word => (word.trim(), 1))
    val r2=pairs.collect
    lc.setCaptureLineage(false)
    print("============================\n>>start 2nd test\n")
    val l3=pairs.getLineage()
    val l4=l3.goBack()
    val r3=l4.collect
    val rr2=l4.show
    print("\n")
    //no shuffle phase, just one goBack allowed
    /*val l5=l3.goBack()
    val r4=l5.collect*/
    print(">>end 2nd test\n============================\n")
    
    lc.setCaptureLineage(true)
    val file = lc.textFile(logFile, 2)
    val pairs = file.flatMap(line => line.trim().split(" ")).map(word => (word.trim(), 1))
    val result = pairs.reduceByKey(_ + _)//.asInstanceOf[Lineage[(String,Int)]]
    //val newresult = result.asInstanceOf[Lineage[(String,Int)]]
    val r4=result.collect
    lc.setCaptureLineage(false)
    print("============================\n>>start 3rd test\n")
    val l5=result.getLineage()
    val l6=l5.goBack()
    val r4=l6.collect
    val rr3=l6.show
    print("\n")
    val l7=l6.goBack()
    val r5=l7.collect
    val rr4=l7.show
    print(">>end 3rd test\n============================\n")
    
    
