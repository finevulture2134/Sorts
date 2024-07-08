
(struct n (v l r))
(define a (n 4 #F #F))
(define b (n 6 #F #F))
(define c (n 8 #F #F))
(define d (n 11 #F #F))
(define lt (n 5 a b))
(define rt (n 9 c d))
(define root (n 7 lt rt))



(define (preorder tree)
  (when (n? tree) 
    (displayln (n-v tree))
  (preorder (n-l tree))
  (preorder (n-r tree))))
(preorder root)
