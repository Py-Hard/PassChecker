# Scoring Function
def scorepass(inp):
	score = 0.0
	symbols = "!@#$%^&*()+-_.,?"
	common_patterns = ["123", "1234", "abc", "abcd", "qwerty", "password"]
	bad_endings = ["!", "_", ".", "0", "1", "12", "123", "1234"]
	length = len(inp)
	lower = inp.lower()

	# praise system
	if length >= 20:
		score += 0.4
	elif length >= 10:
		score += 0.2
	elif length <= 5:
		# too short, too easy to crack.
		return 0.0
	else:
		score += 0.1

	if any(c.islower() for c in inp):
		score += 0.1
	if any(c.isupper() for c in inp):
		score += 0.1
	if any(c.isdigit() for c in inp):
		score += 0.1
	if " " in inp:
		score += 0.1
	if any(c in symbols for c in inp):
		score += 0.1
	
	# punishing system
	if inp.islower() or inp.isupper() or inp.isdigit():
		score -= 0.2

	for p in common_patterns:
		if p in lower:
			score -= 0.3
	
	for end in bad_endings:
		if inp.endswith(end):
			score -= 0.2

	return score

while True:
	inp = input("input text: ")
	print(inp)

	if inp == "exit" or inp == "EXIT" or inp == "Exit":
		break

	score = scorepass(inp)
	print("score:", round(score, 1))