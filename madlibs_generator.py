word_user_ip = {}
start_idx = -1
target_start = "["
target_end = "]"

with open("madlibs_generator_story.txt", "r") as story_file:
    story = story_file.read()

    for i, char in enumerate(story):
        if char == target_start:
            start_idx = i

        if char == target_end and start_idx != -1:
            word = story[start_idx: i+1]
            word_user_ip[word] = None

for key in word_user_ip.keys():
    val = input(f"Enter a word for {key}: ")
    word_user_ip[key] = val
    story = story.replace(key, val)

print(story)