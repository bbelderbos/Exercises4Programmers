quotes = [
("Tell me, what is it you plan to do / with your one wild and precious life?", "Mary Oliver"),
("You cannot overestimate the unimportance of practically everything.", "John Maxwell"),
("A non-Essentialist thinks almost everything is essential. An Essentialist thinks almost everything is non-essential.", "Greg Mckeown"),
("I do believe in simplicity. It is astonishing as well as sad, how many trivial affairs even the wisest thinks he must attend to in a day; how singular an affair he thinks he must omit. When the mathematician would solve a difficult problem, he first frees the equation of all incumbrances, and reduces it to its simplest terms. So simplify the problem of life, distinguish the necessary and the real. Probe the earth to see where your main roots run.", "Henry David Thoreau"),
("People are effective because they say 'no,' because they say, 'this isn't for me'.", "Peter Drucker"),
("If one's life is simple, contentment has to come. Simplicity is extremely important for happiness. Having few desires, feeling satisfied with what you have, is very vital: satisfaction with just enough food, clothing, and shelter to protect yourself from the elements. And finally, there is an intense delight in abandoning faulty states of mind and in cultivating helpful ones in meditation.","Dalai Lama"),
]

def print_quotes():
  out = []
  for q in quotes:
    (quote, author) = q
    out.append(author + ' says, "' + quote + '"')
  return "\n".join(out)

if __name__ == "__main__":
  print print_quotes()
