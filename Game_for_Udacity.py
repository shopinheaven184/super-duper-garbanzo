import textwrap

first_question = "We are surrounded by colors. Colors can be broken down into red, " \
                "yellow, and blue called {1} colors. Orange, green, and violet are known as {2} colors. " \
                "When making {3}, an expression of creativity, colors allow a person to express themselves. " \
                "Lots of children use {4}, colored wax sticks, to create their {3}."

first_answers = ["primary", "secondary", "art", "crayons"]

first_question_answer = "We are surrounded by colors. Colors can be broken down into red, " \
                "yellow, and blue called primary colors. Orange, green, and violet are known as secondary colors. " \
                "When making art, an expression of creativity, colors allow a person to express themselves. " \
                "Lots of children use crayons, colored wax sticks, to create their art."


print "Type 'quit' at any time to leave the game."


def get_user_level():
    user_level = raw_input("Please choose a level by typing one of the following: easy, medium, or hard")
    return user_level


def get_user_word():
    resp = raw_input("Please provide an answer. (Note: You do not have to answer in the order given): ")
    return resp


def init_answers(answers):
    user_answers = {}
    for answer in answers:
        user_answers[answer] = False
    return user_answers


def check_user_level(us_lev,level):
    pass
    # for lev in level:
    #     if us_lev == "easy":
    #         return easy_para
    #     if us_lev == "medium":
    #         return med_para
    #     else:
    #         return hard_para


def check_user_word(user_word, answers):
    for position, answer in enumerate(answers):
        if user_word == answer:
            return position + 1
    return -1


def replace_user_answer(question, answer, position):
    token = "{" + str(position) + "}"
    question = question.replace(token, answer)
    return question


def all_questions_answered(answers):
    all_answered = True
    for answer in answers:
        all_answered &= answers[answer]
        if not all_answered:
            break
    return all_answered


# Initialize the game
user_answers = init_answers(first_answers)

# Let's display a puzzled paragraph
print "\n".join(textwrap.wrap(first_question, 80))
print "\n"


while True:
    user_response = get_user_word()
    if user_response == "quit":
        quit()
    print "Your guess was " + user_response + "."
    ans_pos = check_user_word(user_response, first_answers)

    if ans_pos >= 0:
        user_answers[user_response] = True
        print "Great Job! Here's your updated question"
        first_question = replace_user_answer(first_question, user_response, ans_pos)
        print "\n".join(textwrap.wrap(first_question, 80))
        if all_questions_answered(user_answers):
            break
    else:
        print "Your answer is not correct. You got this! Try again or enter 'quit' to exit."
    print "\n"

print "\n"
print "-" * 50
print "Let's keep on going! Now here is the next one.\n" + "\n".join(textwrap.wrap(first_question, 80))


    # todo: ask for next answer
    # todo: how many are remaining
    # todo: has the answer already been used

