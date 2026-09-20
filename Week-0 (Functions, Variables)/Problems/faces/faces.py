# Create a function convert that accepts a str.
def convert(t):
	return t.replace(":)", "🙂").replace(":(", "🙁")

# Create a function main.
def main():
	text = convert(input())
	print(text)

if __name__ == "__main__":
	main()