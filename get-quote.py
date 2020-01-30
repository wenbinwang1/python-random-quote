import random

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(quotes)
  #print(quotes[13])
  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd], end ='' )
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print("hello")

if __name__== "__main__":
  main()
