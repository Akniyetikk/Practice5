#*	Zero or more occurrences	a*b	"b", "ab", "aab", etc.
#+	One or more occurrences	a+b	"ab", "aab", "aaab", etc., but not "b"
#?	Zero or one occurrence (optional)	colou?r	"color", "colour"
#{n}	Exactly n occurrences	\d{3}	"123" but not "12", "1234"
#{n,}	n or more occurrences	a{2,}	"aa", "aaa", "aaaa", etc.
#{n,m}	Between n and m occurrences	\d{2,4}	"12", "123", "1234" but not "1" or "12345"
