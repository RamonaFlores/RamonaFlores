package lectures.basicspt1

//Extends app es el equivalente a crear una función Main
//Esto es lo que hace que una aplicación / clase pueda ser ejecutada

//Una alternativa para skipearse el "extends App" es:

// En el cuerpo del objeto dentro de los {}, escribir "main"
// y presionar ctrl-space para auto generar la función
object ValuesVariablesTypes  extends App {
//ejemplo de una variable

//si se declara una variable con "val" su valor NO puede ser reasignado.

//VALS ARE INMUTABLE

val x: Int = 42
//La declaración de tipo de una val es opcional

//La máquina infiere el tipo a partir del valor que hay a la derecha

//val x = 42 es una forma correcta de declarar una variable.
println(x)

//Ejemplos de declaración de Val
val aString: String = "hello"

val anotherString = "goodbye"

val aBoolean: Boolean= false

val aChar: Char = 'a'

val anInt: Int= x

val aShort: Short = 4613

val aLong: Long = 52739854324234243L

val aFloat: Float= 2.0f

val aDouble: Double = 3.14

//Variables

var aVariable: Int = 4

//las variables pueden ser reasignadas

//Ejemplo de Reasignación

// Se dice que las variables son mutables

aVariable = 5

aVariable+=1
}
