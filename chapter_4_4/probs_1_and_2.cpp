template<class A> class optional { 
    bool _isValid;
    A _value;
public:
    optional() : _isValid(false) {} 
    optional(A v) : _isValid(true), _value(v) {} 
    bool isValid() const { return _isValid; }
    A value() const { return _value; }
};


/* PROBLEM 1 */
/* composition rule for partial function category */

/* template beginning option 1 */
template<class A, class B, class C>
function<optional<C>(A)> compose(
        function<optional<B>>(A) m1,
        function<optional<C>>(B) m2)
/* template beginning option 2 */
template<class A>
auto const compose = [](auto m1, auto m2)
/* rest of composition fn */
{
	[m1, m2](auto x){
		auto p1 = m1(x);
        if p1.isValid() {
            auto p2 = m2(p1.value())
            return p2;
       } else return p1; 
    }
}

/* category identity */
template<class A> optional<A> identity(A x) {
    return optional<A>{x};
}


/* UNIT FOR PARTIAL FUNCTION CATEGORY */
template<class A>


/* QUESTION 2: implement safe_reciprocal */
optional<double> safe_reciprocal(double x) {
    if x != 0. return optional<double>{ 1. / x };
    else return optional<double>{};
}
/* QUESTION 3: implement safe_root_reciprocal via composition */
optional<double>safe_root_reciprocal(double x) {
    return compose(safe_root, safe_reciprocal)
}
