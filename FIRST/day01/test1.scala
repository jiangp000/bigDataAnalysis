package day01

import scala.io.Source

class test1 {

}

object Test1{
  def main(args: Array[String]): Unit = {
    val lines = Source.fromFile("C:\\Users\\Administrator.DESKTOP-CGIO78B\\IdeaProjects\\scalatest\\src\\main\\scala\\data\\test.txt", "gbk").getLines().toArray;
    var str=""
    var i=0
    for(line<-lines) {

      var lineWithBlank=line+" "
      str=str+lineWithBlank

    }
    println(str)

    var result=str.toLowerCase()


    println(result)
    // 将所有的字母都转化为 小写字母

    val line =List(result)

    //    val line=List("hello world java hello reduce hello scala java nad people 's republic of china");
    var words=line.flatMap(_.split("\\s+"))
    println(words)

//    把每个单词生成元组

    var tuples=words.map((_,1))
    println(tuples)



    var grouped=tuples.groupBy(_._1)
    println(grouped)



    var sumed=grouped.view.mapValues(_.size)


    var sorted=sumed.toList.sortBy(_._2)

    println(sorted)

    //默认从低往高排   可以反转一下

    var result999=sorted.reverse

    println(result999)

    result999.foreach(s=>println(s))


//    var temp="qwrrQWRTTT"
//
//    val toLower=(x:String,y:String)=>{
//      if()
//    }

//    var a= Array("111", "222", "222", "333", "555", "777")
//    println(a)
//    val c=a.reduce(__)
//    println(c)

  }
}