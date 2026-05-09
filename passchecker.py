# colors!!!
class Color:
	RESET = "\033[0m"
	BOLD = "\033[1m"
	RED = "\033[31m"
	YELLOW = "\033[33m"
	BLUE = "\033[34m"
	GREEN = "\033[32m"
	CYAN = "\033[36m"

# Scoring Function
def scorepass(inp):
	symbol_count = 0
	repeat_count = 1
	last_char = None
	score = 0.0
	length = len(inp)
	lower = inp.lower()
	bad_end = ["!", "_", ".", "0", "1", "12", "123", "1234", "69", "420", "67", "#", "_"]
	symbols = "!@#$%^&*()+-_.,?[]{}="
	leet = {"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t"} # example: 1337 = LEET
	common = ["123", "1234", "abc", "abcd", "qwerty", "password", "admin", "qwertyuiop", "1234567890"]

	# Too short = instant fail
	if length <= 5:
		return -1.0

	complexity = {
		"lower": 0.02,
		"upper": 0.03,
		"digit": 0.01,
		"symbol": 0.03
	}

	symbol_count = 0

	for c in inp:
		# repeating character punishment
		if c == last_char:
			repeat_count += 1
			if repeat_count > 3:
				score -= 0.02 * (repeat_count - 3)
		else:
			repeat_count = 1

		last_char = c

		if c.islower():
			ctype = "lower"
		elif c.isupper():
			ctype = "upper"
		elif c.isdigit():
			ctype = "digit"
		elif c in symbols:
			ctype = "symbol"
			symbol_count += 1
		else:
			ctype = "other"

		if ctype in complexity:
			score += complexity[ctype]

		if c in leet:
			score -= 0.05

	# praise more symbol use
	if symbol_count >= 3:
		score += 0.10
	elif symbol_count == 2:
		score += 0.05
	elif symbol_count == 1:
		score += 0.02

	# Common pattern punishments
	for p in common:
		if p in lower:
			score -= 0.5

	# Bad endings
	for end in bad_end:
		if lower.endswith(end):
			score -= 0.05
	# Bad starts
	for end in bad_end:
		if lower.startswith(end):
			score -= 0.025

	# Length bonus
	score += min(0.25, length * 0.01)

	if score > 1.0:
		score = 1.0
	elif score < -1.0:
		score = -1.0

	return score

# Grading Function
def grade(score):
	if score < 0.0:
		return f"{Color.BOLD}{Color.RED}Critical Risk!{Color.RESET}\a"
	elif score < 0.3:
		return f"{Color.RED}Weak{Color.RESET}"
	elif score < 0.7:
		return f"{Color.YELLOW}Moderate{Color.RESET}"
	elif score < 0.9:
		return f"{Color.GREEN}Strong{Color.RESET}"
	else:
		return f"{Color.CYAN}Very Strong{Color.RESET}"

while True:
	inp = input("input text: ")
	print(inp)

	if inp == "exit" or inp == "EXIT" or inp == "Exit":
		break

	score = scorepass(inp)
	rounded = round(score, 1)
	print("Score:", rounded)
	print("Grade: ", grade(rounded))