let split = Str.split (Str.regexp_string " ");;

let gammaln_of_int ( z : int ) =
    let cof =[|76.18009172947146;-86.50532032941677;
              24.01409824083091;-1.231739572450155;
              0.1208650973866179e-2;-0.5395239384953e-5|]
    and z = float_of_int z in 
    let y = ref z in
    let x = z in
    let tmp=x +. 5.5 in
    let tmp = tmp -. (x +. 0.5)*.log(tmp) in
    let ser= ref 1.000000000190015 in
    for j= 0 to 5  do 
        y:=!y +. 1.0;
        ser := !ser +. cof.(j) /. !y 
    done;
    -. tmp +. log( 2.5066282746310005 *. !ser /. x )

let beta_function (alpha:int) (beta:int) =
    exp (gammaln_of_int(alpha) 
    +. gammaln_of_int(beta) 
    -. gammaln_of_int(alpha + beta))
;;

let power (x:float) (n:int) =
    x ** (float_of_int n)
;;

let beta_pdf (alpha:int) (beta:int) (x:float) =
    let num =
    (power x (alpha -1 )) *. ( power (1. -. x)  (beta -1))
    in num /. (beta_function alpha beta)
;;

let h a1 b1 a2 b2 =
    (beta_function (a1+a2) (b1+b2)) /. 
    (( beta_function a1 b1 ) *. (beta_function a2 b2))
;;

let rec g a1 b1 a2 b2  =
    if  a1 = b1 && b1 = a2 && a2 = b2  then 0.5 
    else  if  a1 > 1  then 
        (g (a1-1) b1 a2 b2 ) +. 
            ( h (a1 - 1) b1 a2 b2) /. ( float_of_int  ( a1 - 1 ) ) 
    else
    if  b1 > 1  then
        ( g a1 (b1-1) a2 b2 ) -. 
            (h a1 (b1-1) a2 b2) /. ( float_of_int ( b1 - 1 ) )
    else 
    if  a2 > 1  then 
        ( g a1 b1 (a2-1) b2 ) -. 
            ( h a1 b1 (a2-1) b2 ) /. ( float_of_int ( a2 - 1 ) )
    else
    if  b2 > 1  then
        ( g a1 b1 a2 ( b2 - 1 ) ) +. 
            ( h a1 b1 a2 ( b2 - 1 ) ) /. ( float_of_int ( b2 - 1 ) )
    else -1.0 
;;

let rec range start stop acc =
    match start with 
    |start when ( start > stop ) -> ( List.rev acc )
    |_ -> range (start + 1 ) stop ( start::acc )
;;

let _ =
    try
 while true do
   let line = input_line stdin in
    let fields = split line in
 let params = List.map (fun e->int_of_string e ) fields
 in 
 let a1 = List.nth params 0
    and b1 = List.nth params 1
    and a2 = List.nth params 2
    and b2 = List.nth params 3
    in
    Printf.fprintf stdout "%g\n" ( g a1 b1 a2 b2 )
 done;
 None
with
 End_of_file -> None
