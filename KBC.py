ques = [
    [
        "What is the capital of India?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "A"
    ],
    [
        "What is the capital of Maharashtra?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "B"
    ], 
    [
        "What is the capital of West Bengal?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "C"
    ], 
    [
        "What is the capital of Tamil Nadu?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "D"
    ],
    [
        "What is the capital of Uttar Pradesh?", "A. Kanpur", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "A"
    ],
    [
        "What is the capital of India?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "A"
    ],
    [
        "What is the capital of Maharashtra?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "B"
    ], 
    [
        "What is the capital of West Bengal?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "C"
    ], 
    [
        "What is the capital of Tamil Nadu?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "D"
    ],
    [
        "What is the capital of Uttar Pradesh?", "A. Kanpur", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "A"
    ],
    [
        "What is the capital of India?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "A"
    ],
    [
        "What is the capital of Maharashtra?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "B"
    ], 
    [
        "What is the capital of West Bengal?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "C"
    ], 
    [
        "What is the capital of Tamil Nadu?", "A. Delhi", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "D"
    ],
    [
        "What is the capital of Uttar Pradesh?", "A. Kanpur", "B. Mumbai",
         "C. Kolkata", "D. Chennai", "A"
    ]
]
print("Welcome to KBC")
levels = [1000,2000,5000,10000,25000,50000,100000,500000,1000000,2500000,5000000,10000000,20000000,40000000,70000000]
wonmoney = 0
for index,question in enumerate(ques):
    print(f"The question for Rs{levels[index]} is on your screen \n\n{question[0]}" )
    print(f"{question[1]}\t\t{question[2]}")
    print(f"{question[3]}\t\t{question[4]}")
    answer = input(f"Enter the correct option to win Rs{levels[index]}\n")
    print(answer)
    if answer == question[-1]:
        print(f"Aap jeet chuke hai {levels[index]} rupees ")
        if index == 4:
            wonmoney = 25000
        elif index == 9:
            wonmoney = 2500000
        elif index == 14:
            wonmoney = 70000000
    else:
        print("Bade shok ke saath batana pad rha hai aap haar chuke hai")
        print(f"kul raashi jo aap jeete hai vo hai {wonmoney}")
        break
else:
    print("Aap jeet chuke hai 7 crore ")
    

    