

def newton(x, eps=0.01):
    err = 1
    cur_guess = x
    new_guess = 0
    
    while err>eps:
        new_guess = (cur_guess + x/cur_guess) / 2
        err = abs(cur_guess - new_guess)
        cur_guess = new_guess
    return cur_guess


def gradient(a, lr=0.01, eps=0.00001):
    x = 2
    err = 1
    while err > eps:
        
        dx = 4*x*(x**2 - a)
        new_x = x - dx*lr
        err = abs(new_x - x)
        x = new_x
    return x
    
    

if __name__ == "__main__":
    print(newton(2))
    print(gradient(2))
    
        