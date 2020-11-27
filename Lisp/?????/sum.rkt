#lang sicp
(define (sqrt x)
  (define tolerance 0.000001)
  (define (good - enuf? y)
    (< (abs (- (* y y) x)) tolerance))
  (define (improve y)
    (average (/ x y) y))
  (define (try y)
    (if (good - enuf? y)
        y
        (try (improve y ))))
  (try !))
