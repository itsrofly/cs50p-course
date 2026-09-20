import re

def main():
  print(parse(input("HTML: ")))

def parse(s):
  if m := re.search("^.+https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).+$", s):
    return f"https://youtu.be/{m.group(1)}"

if __name__ == "__main__":
  main()