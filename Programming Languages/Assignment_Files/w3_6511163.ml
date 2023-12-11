

(*Lut Lat Aung, 6511163, CSX3004(541)*)


(* No.1 *)


fun iseven(n: int): bool =
    if n mod 2 = 0 then true
    else false;

(* No.2 *)

fun cube(n: int): int =
    n*n*n;

    
(* No.3 *)

fun cuber(n: real): real =
    n*n*n;

    
(* No.4 *)

fun third(n: 'a list): 'a =
    hd(tl(tl n));


(* No.5 *)

fun max3(a: int, b: int, c: int): int =
    if a >= b andalso a >= c then a
    else if b >= a andalso b >= c then b
    else c;



(* No.6 *)

fun remove2(tuple: 'a * 'b * 'c): 'a * 'c =
    let
        val (first, _, third) = tuple
    in
        (first, third)
    end;

remove2("tin", 7, 1.2);


(* No.7 *)

fun fourthch(str: string): char =
    String.sub(str, 3);


(* No.8 *)

fun rotate(lst: 'a list, n: int): 'a list =
    let
        val len = length lst
        val rotateBy = n mod len
    in
        if rotateBy < 0 then rotate(lst, len + rotateBy)
        else
            let
                val (front, back) = chop rotateBy lst
            in
                back @ front
            end
    end;


(* No.9 *)

fun minhelper(x: int, nil: int list): int = x
  | minhelper(x, y::ys) = if x <= y then minhelper(x, ys) else minhelper(y, ys);

fun min(lst: int list): int =
    case lst of
        [] => raise Empty
      | x::xs => minhelper(x, xs);


(* No.10 *)

fun select(lst: 'a list, f: 'a -> bool): 'a list =
    filter f lst;

    