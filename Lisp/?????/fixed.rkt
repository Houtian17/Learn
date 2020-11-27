#lang sicp
(define (fixed-point f start)
  (define tolerance o.00001)
  (define (close-enuf? u v)
    (< (abs (- u v)) tolerance))
  (define (iter old new)
    (if (close-enuf? old new)
        new
        (iter new (f new ))))
  (iter start (f start)))