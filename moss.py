import Levenshtein
import os
import random
import string
import shutil

def prepare(province, level):
    directory = '{}-{}'.format(province, level)
    contestants = os.listdir(directory)
    contestants = [contestant for contestant in contestants if not contestant.startswith('.')]
    n = len(contestants)
    problems = [os.listdir(os.path.join(directory, contestant)) for contestant in contestants]
    problems = [temporary for problem in problems for temporary in problem]
    problems = [problem for problem in list(set(problems)) if problems.count(problem) > n / 2]
    return sorted(contestants), sorted(problems)

def calculate(province, level, contestants, problem):
    directory = '{}-{}'.format(province, level)
    auxiliary = ''
    while len([name for name in os.listdir() if name.startswith(auxiliary)]) > 0:
        auxiliary += random.choice(string.ascii_lowercase)
    os.mkdir(auxiliary)
    os.mkdir(os.path.join(auxiliary, auxiliary))
    for contestant in contestants:
        dir = os.path.join(os.path.join(directory, contestant), problem)
        if os.path.exists(dir):
            names = [name for name in os.listdir(dir) if not name.startswith('.')]
            if len(names) > 0:
                name = max(names, key = lambda x: os.path.getsize(os.path.join(dir, x)))
                with open(os.path.join(dir, name), 'r', encoding = 'UTF-8', errors = 'ignore') as file:
                    code = file.read()
                    with open(os.path.join(os.path.join(auxiliary, auxiliary), '{}.cpp'.format(contestant)), 'w') as f:
                        f.write(code)
    os.chdir(auxiliary)
    os.system('java -jar ../{} {} -l cpp --normalize --csv-export --cluster-skip -M=RUN'.format('jplag.jar', auxiliary))
    os.chdir('..')
    with open(os.path.join(auxiliary, os.path.join('results', 'results.csv')), 'r') as file:
        with open('{}_{}.csv'.format(province, problem), 'w') as f:
            lines = file.readlines()
            for line in lines[1 : ]:
                submissionName1, submissionName2, averageSimilarity, maxSimilarity = line.strip().split(',')
                submissionName1 = submissionName1.replace('.cpp', '')
                submissionName2 = submissionName2.replace('.cpp', '')
                f.write('{},{},{},{},{}\n'.format(province, problem, submissionName1, submissionName2, averageSimilarity))
    shutil.rmtree(auxiliary)

province = 'SD'
level = 'Junior'
contestants, problems = prepare(province, level)
for problem in problems:
    if problem == 'chain':
        calculate(province, level, contestants, problem)
    elif problem == 'explore':
        calculate(province, level, contestants, problem)
    elif problem == 'poker':
        calculate(province, level, contestants, problem)