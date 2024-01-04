package lectures.basicspt2

object Expressions extends  App {

  //Ejemplo

  val x = 1 + 2 //----D esto es una expresión
  println(x)

  //Las expresiones tiene la misma jerarquía de toda la vida
  println(2 + 3 * 4)

  //Operadores

  // + - * / & | ^  << >> >>> (right shift with zero extension?)

  //si evaluas asì una variable el resultado será un booleano
  //porque estás comparando

  println(1 == x)

  //Operadores relacionales

  // != > >=  <  <=

  //Negación Lógica
  println(!(1 == x))

  //Operadores Lógicos

  // ! ||

  var aVariable = 2
  aVariable += 3 // también funciona con -= *= /=....Todos estos se conocen
  //como Side Effects jaja

  //Instructions (Cosas que se le ordena al computador que haga)

  //básicamente lo que se hacen en lenguajes imperativos como python y java


  // vs Expressions (cosas que tienen un valor o un tipo)


  //Expression IF
  val aCondition = true
  val aConditionedValue = if (aCondition) 5 else 3

  //en el condicional se dice si aCondition verdadero

  //entonces el valor de aConditionedValue es 5

  //sino  el valor de aConditionedValue es 3
  println(aConditionedValue)

  println(if (aCondition) 5 else 3)

  // IF en Scala es una EXPRESSION

  //Ciclos?

  var i = 0
  while (i < 10) {
    println(i)
    i += 1
  }
  //La expresión While retorna UN UNIT

  //EVITAR LOS CICLOS A TODA COSTA

  //To_do EN Scala es una Expression

  val aWeirdValue = (aVariable = 3) //Esto aparece como Unit

  //Unit es equivalente a === Void

  //El único valor de Unit es ()

  //Ejemplos de Side effects:

  //println(), whiles, reassigning

  //Los side effects son cosas que hacen reminiscencia a las instrucciones
  //de los lenguajes imperativos como python y java
  //pero en realidad son Expressions que retornan Unit (void)

  //Code Blocks

  //esto es un bloque de código; aquí se escribe código, se definen vals

  // Los CodeBlocks son expresiones

  //El val de un CodeBlock es el val de su última expresión
  val aCodeBlock = {
    val y = 2
    val z = y + 1

    if (z > 2) "hello" else "goodbye"
  }
  //Las variables declaradas dentro de un CodeBlock no se pueden
  //acceder desde afuera del CodeBlock

  //Una instruction se ejecuta, una expression se evalua


  //Mini quiz

  //1. Diferencia entre el string "hello world" vs println("hello world")?

  //el String hello world es un value de tipo String
  //println es un sideEffect y como ya sabemos los sideffects retornan Unit

  //2. el Value de

  val someValue = {
    2 < 3
  }
  //el Value de someValue es true pq es la ùltima expresiòn evaluada

  //3. el Value de

  val someOtherValue = {
    if (someValue) 239 else 986
    42

  }
  //el Value sería 42 porque nuevamente es la última expresion dada

}