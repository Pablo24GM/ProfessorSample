from random import randint, choice

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f'Your score is {score} / 10')
    print(final_score(score))


def get_level():
    while True:
        level = input('Select a level between 1 to 3: ')
        if level in ['1', '2', '3']:
            return int(level)

def generate_integer(level):
    if level == 1:
        return randint(1, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)

def generate_problems(level):
    problems = []
    while len(problems) < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        z = str(choice(['+', '-', '-' ,'*', '/', '/']))
        problem = f'{x} {z} {y} = '
        if z == '+' or z == '*':
            problems.append((x, y, z, problem))
        elif z == '-' and x - y >= 0:
            problems.append((x, y, z, problem))
        elif z == '/' and x % y == 0:
            problems.append((x, y, z, problem))
    return problems
        
def solve_problems(problems):
    score = 0
    for x, y, z, problem in problems:
        tries = 0
        while True:
            answer = input(problem)
            try:
                answer = int(answer)
                if z == '+' and answer == x + y:
                    score += 1
                    break
                elif z == '-' and answer == x - y:
                    score += 1
                    break
                elif z == '*' and answer == x * y:
                    score += 1
                    break
                elif z == '/' and answer == x / y:
                    score += 1
                    break
                else:
                    tries += 1
                    if tries < 3:
                        print('Try again')
                    elif tries == 3:
                        print('Sorry, the correct answer is:')
                        if z == '+':
                            print(problem, x + y)
                            break
                        elif z == '-':
                            print(problem, x - y)
                            break
                        elif z == '*':
                            print(problem, x * y)
                            break
                        elif z == '/':
                            print(problem, round(x / y))
                            break
            except ValueError:
                print('This is not a valid answer, try again')
                tries += 1 
                if tries == 3:
                    if z == '+':
                        print(problem, x + y)
                        break
                    elif z == '-':
                        print(problem, x - y)
                        break
                    elif x == '*':
                        print(problem, x * y)
                        break
                    elif z == '/':
                        print(problem, x / y)
                        break
    return score

def final_score(score):
    if 0 <= score <= 3:
        fm = 'You need to work harder! Come on, lets try again!'
    elif 4 <= score <= 6:
        fm = 'Keep up the good work! You are getting better!'
    elif 7 <= score <= 9:
        fm = "You're doing great! Come on, you're almost there!"
    elif score == 10:
        fm = 'Excelent job! you are ready for the next level!'
    return fm

if __name__=='__main__':
    main()