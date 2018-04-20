const True = t => f => t
const False = t => f => f
const If = b => t => f => b(t)(f)
const Not = x => If(x)(False)(True)
const And = x => y => If(x)(y)(False)
const Or = x => y => If(x)(True)(y)

const Pair = x => y => (f => f(x)(y))
const Fst = p => p(True)
const Snd = p => p(False)
const List = x => y => If(Not(y))

const IsZero = n => n(_ => False)(True) // Если аргумент можно вызвать - то Тру, если нет, то Фалс
const Lte = n => m => IsZero(Sub(n)(m))
const Lt = n => m => Lte(Succ(n))(m)
const Eq = n => m => And(Lte(n)(m))(Lte(m)(n))



const func1 = x => x
const func2 = x => 2 * x
const check = x => y => comp => comp(x)(y)
const comparator = x => y => x
const min = x => y => x - y
const x = 1
const y = 1

console.log(If(check(x)(y)(comparator))(func1(1))(func2(1)))
