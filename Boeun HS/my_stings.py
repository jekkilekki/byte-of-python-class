iron_man = 'He said, "Let\'s fight!"'
capt_amr = "I said,'No!'"

story = '\t' + iron_man + '\n\t' + capt_amr
print(story)

# Capitalization = 대글자로 변경하기 
me = "john wick"
you = "barbie"

# f-string = Python 3.6+
print(f"{me.upper()} fights {you.title()}")

# Python 3.5- (.format())
print("{} kills {}".format(me.title(), you.title()))

# Strip
print(story.strip())

# "          Help!".lstrip() = "Help!"
# "Help!          ".rstrip() = "Help!"
# "      Help!    ".strip() = "Help!"
# "  Help      Help  ".strip() = "Help     Help"