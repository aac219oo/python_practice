import random

lottoNumbers = random.sample(range(1,50),6)
lottoNumbers.sort()

specialNumbers = [n for n in range(1,50) if n not in lottoNumbers]
specialNumber = random.choice(specialNumbers)
print(lottoNumbers, specialNumber)