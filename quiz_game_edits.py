import json
import requests
import pprint
import time
import random
import html

# Easy fix!
#ok

def category(cat_choice):
    category_picked = True
    
    while category_picked:
        if cat_choice == 1:
            triv_api = "https://opentdb.com/api.php?amount=10&category=15&type=multiple"
            category_picked = False
        elif cat_choice == 2:
            triv_api = "https://opentdb.com/api.php?amount=10&category=12&type=multiple"
            category_picked = False
        elif cat_choice == 3:
            triv_api = "https://opentdb.com/api.php?amount=10&category=9&type=multiple"
            category_picked = False
        elif cat_choice == 4:
            triv_api = "https://opentdb.com/api.php?amount=10&category=24&type=multiple"
            category_picked = False
        elif cat_choice == 5:
            triv_api = "https://opentdb.com/api.php?amount=10&category=11&type=multiple"
            category_picked = False
        else:
            cat_choice = int(input("Please select a valid category: "))
            continue


        return triv_api

def category_choice_redo():
    data_valid = False
    while data_valid == False:
        category_choice = input("Please select a category: \n 1: Video Games \n 2: Music \n 3: General Knowledge \n 4: Politics \n 5: Film \n Choice: ")
        try:
            category_choice = int(category_choice)
        except:
            print("\nPlease enter a valid number corresponding to the category: \n")
            continue

        if category_choice >= 6 or category_choice <= 0:
            print("\nPlease enter a valid number corresponding to the category: \n")
            continue
        else:
            data_valid = True

    return category_choice



question_count = [] #10 questions per quiz
right_answer = 0    #will keep track of right answers
wrong_answer = 0    #will keep track of wrong answers
print("Welcome to Vanni's Quiz Game!")
print("This is a 10 question quiz, your results will be displayed at the end.")
play_confirm = input("Press enter to play.")
play_again = True
print('---------------------------')
print('---------------------------')

####
new_cat = True
while play_again:  # default set to True
    quiz_answers = []   #empty list to store quiz answers
    answer_number_list = [] #empty list to store question numbers (1, 2, 3, 4)
    i = 0
    
    while new_cat:
        category_choice = category_choice_redo()
        new_cat = False
        
    x = category(category_choice)
    r = requests.get(x)
    question = json.loads(r.text)

    #pprint.pprint(question)
    #print(type(question))
    quiz_answers.append(html.unescape(question['results'][i]['incorrect_answers'][0])) ##appends answers to quiz_answers
    quiz_answers.append(html.unescape(question['results'][i]['incorrect_answers'][1]))
    quiz_answers.append(html.unescape(question['results'][i]['incorrect_answers'][2]))
    quiz_answers.append(html.unescape(question['results'][i]['correct_answer']))
    random.shuffle(quiz_answers)  #shuffles all items inside list

    print(html.unescape(question['results'][i]['category']))
    print(html.unescape(question['results'][i]['question']))
    answer_number = 1 # sets answer # to 1 everytime a new question is asked

    for answer in quiz_answers:  #easy to iterate numbers, thats why a-d didn't work
        print(answer_number, ": ", answer)
        answer_number += 1
        answer_number_list.append(answer_number-1)
        #print(answer_number_list)

    answer_dict = dict(zip(answer_number_list, quiz_answers))   #combines the list containing 1: 2: 3: 4: with the randomized quiz answers into a dictionary

    try:
        user_choice = int(input("Answer: "))
    except:
        print("You have entered an invalid answer.")

    if user_choice == 1:
        for key, value in answer_dict.items():
            if value == question['results'][i]['correct_answer'] and user_choice == key:
                print("You got it!")
                right_answer += 1
            elif (value !=question['results'][i]['correct_answer'] and user_choice == key):
                print("Wrong answer. The correct answer is " + question['results'][i]['correct_answer'] + ".")
                wrong_answer += 1
    elif user_choice == 2:
        for key, value in answer_dict.items():
            if value == question['results'][i]['correct_answer'] and user_choice == key:
                print("You got it!")
                right_answer += 1
            elif (value !=question['results'][i]['correct_answer'] and user_choice == key):
                print("Wrong answer. The correct answer is " + question['results'][i]['correct_answer'] + ".")
                wrong_answer += 1
    elif user_choice == 3:
        for key, value in answer_dict.items():
            if value == question['results'][i]['correct_answer'] and user_choice == key:
                print("You got it!")
                right_answer += 1
            elif (value !=question['results'][i]['correct_answer'] and user_choice == key):
                print("Wrong answer. The correct answer is " + question['results'][i]['correct_answer'] + ".")
                wrong_answer += 1
    elif user_choice == 4:
        for key, value in answer_dict.items():
            if value == question['results'][i]['correct_answer'] and user_choice == key:
                print("You got it!")
                right_answer += 1
            elif (value !=question['results'][i]['correct_answer'] and user_choice == key):
                print("Wrong answer. The correct answer is " + question['results'][i]['correct_answer'] + ".")
                wrong_answer += 1
    else:
        print("Wrong input. This question will now be marked incorrect.")
        continue
    
    question_count.append("") ## appends until 10 things have been added, thus the loop will end
    print() 
    #what u dchange
    total_score = right_answer / len(question_count) * 100
    i += 1 

    while len(question_count) == 10:
        print("Thank you for playing! Calculating your score...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("###############################")
        print("Your final score was ", int(total_score), "%.")
        print("You answered " + str(right_answer) + " question(s) correctly.")
        print("You answered " + str(wrong_answer) + " question(s) incorrectly.")
        print("################################")

        user_play_again = input("Would you like to play again? (y/n): ").lower()

        if (user_play_again == 'y'):  #continues to play game
            question_count = [] #10 questions per quiz
            new_cat = True
            right_answer = 0
            wrong_answer = 0
            break
        else:                      #ends game
            print("Thank you for playing my game.")
            play_again = False
            break
