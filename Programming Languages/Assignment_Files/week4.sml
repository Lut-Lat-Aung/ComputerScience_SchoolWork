(* Week4 *)
(* No.1 *)

fun exist (_,nil) = false 
|   exist (element, x::xs) = 
        (element = x)
        orelse exist(element, xs)

(* x is the first element of the list and xs is the rest *)

(* No.2 *)

fun lessthan(_, nil) = nil
|   lessthan(element, x::xs) = 
        if x < element then
            x::lessthan(element, xs)
        else lessthan(element, xs)


(* No.3 *)


fun repeats nil = false
|   repeats ([a]) = false
|   repeats (x::x1::rest) = 
        (x = x1)
        orelse repeats (x1::rest)

(* No.4 *)

fun partition (pivot, nil) = (nil, nil)
|   partition (pivot, target::rest) = 
        let 
            val (small, big) = partition(pivot,rest)
        in
            if target < pivot
                then (target::small, big)
            else (small, target::big)
        end;

fun quicksort nil = nil
|   quicksort [a] = [a]
|   quicksort (first::rest) = 
        let
            val (lessthan, greater) = partition(first,rest)
        in
            quicksort(lessthan) @ [first] @ quicksort(greater)
        end;

(* No.5 *)

fun isMember ([], _) = false
|   isMember (x::xs, element) = 
        if x = element then 
            true
        else isMember (xs, element)

(* No.6 *)

fun unionConstructor (nil, setB) = setB
|   unionConstructor (setA, nil) = setA
|   unionConstructor (setA, setB) = 
        let
            fun unionHelper ([], [], union) = union
            |   unionHelper (_, first::rest, union) = 
                    if isMember(union, first) then 
                        unionHelper([], rest, union)
                    else unionHelper([], rest, first::union)
            |   unionHelper (setA, setB, _) = unionHelper([], setB, setA)
        in
            unionHelper (setA, setB, [])
        end;


(* No.7 *)


fun intersectConstructor (nil, setB) = nil
|   intersectConstructor (setA, nil) = nil
|   intersectConstructor (setA, setB) = 
        let
            fun intersectHelper ([], _, intersect) = intersect
            |   intersectHelper (first::rest, setB, intersect) = 
                    if isMember(setB, first) then 
                        intersectHelper(rest, setB, first::intersect)
                    else intersectHelper(rest, setB, intersect)
        in
            intersectHelper (setA, setB, [])
        end;

(* No.8 *)


fun powerset([] : 'a list) : 'a list list = [[]]
  | powerset(x :: xs) : 'a list list =
      let
        val withoutX = powerset(xs)
        val withX = List.map (fn set => x :: set) withoutX
        

      in
        withoutX @ withX
      end;
      