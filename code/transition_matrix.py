# TO DO

# transition matrix

def get_stationary_dist(strategy1, strategy2):
    
    ## constants
    
   
    # player 1's strategy
    p1=strategy1[:4];
    p2=strategy1[:8];
    x =strategy1[:12];

    # player 2's strategy
    q1=strategy2[:4];
    q2=strategy2[:8];
    y =strategy2[:12];

   
    # f = underlying environment dynamics of transitioning given both agree
    f = @(a, b) a*b;
     
    # decompose strategy vectors into individual probabilities CC, CD, DC, and DD
    p1cc = p1(1);
    p1cd = p1(2);
    p1dc = p1(3);
    p1dd = p1(4);

    p2cc = p2(1);
    p2cd = p2(2);
    p2dc = p2(3);
    p2dd = p2(4);

    q1cc = q1(1);
    q1cd = q1(2);
    q1dc = q1(3);
    q1dd = q1(4);

    q2cc = q2(1);
    q2cd = q2(2);
    q2dc = q2(3);
    q2dd = q2(4);

    xcc = x(1);
    xcd = x(2);
    xdc = x(3);
    xdd = x(4);

    ycc = y(1);
    ycd = y(2);
    ydc = y(3);
    ydd = y(4);
       
    # define Q = transition matrix
    Q = [
          f(xcc, ycc)*p1cc*q1cc, \
          f(xcc, ycc)*p1cc*(1 - q1cc), \
          f(xcc, ycc)*(1 - p1cc)*q1cc, \
          f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
          (1 - f(xcc, ycc))*p2cc* q2cc, \
          (1 - f(xcc, ycc))*p2cc * (1 - q2cc), \
          (1 - f(xcc, ycc)) * (1 - p2cc)*q2cc, \
          (1 - f(xcc, ycc))* (1 - p2cc) * (1 - q2cc) \
         ;
          f(xcd, ydc)*p1cd*q1dc, \
          f(xcd, ydc)*p1cd*(1 - q1dc), \
          f(xcd, ydc)*(1 - p1cd)*q1dc, \
          f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
          (1 - f(xcd, ydc))*p2cd*q2dc, \
          (1 - f(xcd, ydc))*p2cd*(1 - q2dc), \
          (1 - f(xcd, ydc))*(1 - p2cd)*q2dc, \
          (1 - f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
         ;
          f(xdc, ycd)*p1dc*q1cd, \
          f(xdc, ycd)*p1dc*(1 - q1cd), \
          f(xdc, ycd)* (1 - p1dc)*q1cd, \
          f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
          (1 - f(xdc, ycd))*p2dc*q2cd, \
          (1 - f(xdc, ycd))*p2dc*(1 - q2cd), \
          (1 - f(xdc, ycd))*(1 - p2dc)* q2cd, \
          (1 - f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
         ;
          f(xdd, ydd)*p1dd*q1dd, \
          f(xdd, ydd)*p1dd*(1 - q1dd), \
          f(xdd, ydd)*(1 - p1dd)*q1dd, \
          f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
          (1 - f(xdd, ydd))*p2dd*q2dd, \
          (1 - f(xdd, ydd))*p2dd*(1 - q2dd), \
          (1 - f(xdd, ydd))*(1 - p2dd)*q2dd, \
          (1 - f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
         ;
          f(xcc, ycc)*p1cc*q1cc, \
          f(xcc, ycc)*p1cc*(1 - q1cc), \
          f(xcc, ycc)*(1 - p1cc)*q1cc, \
          f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
          (1 - f(xcc, ycc))*p2cc* q2cc, \
          (1 - f(xcc, ycc))*p2cc * (1 - q2cc), \
          (1 - f(xcc, ycc)) * (1 - p2cc)*q2cc, \
          (1 - f(xcc, ycc))* (1 - p2cc) * (1 - q2cc), \
         ; 
          f(xcd, ydc)*p1cd*q1dc, \
          f(xcd, ydc)*p1cd*(1 - q1dc), \
          f(xcd, ydc)*(1 - p1cd)*q1dc, \
          f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
          (1 - f(xcd, ydc))*p2cd*q2dc, \
          (1 - f(xcd, ydc))*p2cd*(1 - q2dc), \
          (1 - f(xcd, ydc))*(1 - p2cd)*q2dc, \
          (1 - f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
         ;
          f(xdc, ycd)*p1dc*q1cd, \
          f(xdc, ycd)*p1dc*(1 - q1cd), \
          f(xdc, ycd)* (1 - p1dc)*q1cd, \
          f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
          (1 - f(xdc, ycd))*p2dc*q2cd, \
          (1 - f(xdc, ycd))*p2dc*(1 - q2cd), \
          (1 - f(xdc, ycd))*(1 - p2dc)* q2cd, \
          (1 - f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
         ;
          f(xdd, ydd)*p1dd*q1dd, \
          f(xdd, ydd)*p1dd*(1 - q1dd), \
          f(xdd, ydd)*(1 - p1dd)*q1dd, \
          f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
          (1 - f(xdd, ydd))*p2dd*q2dd, \
          (1 - f(xdd, ydd))*p2dd*(1 - q2dd), \
          (1 - f(xdd, ydd))*(1 - p2dd)*q2dd, \
          (1 - f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
        ];
