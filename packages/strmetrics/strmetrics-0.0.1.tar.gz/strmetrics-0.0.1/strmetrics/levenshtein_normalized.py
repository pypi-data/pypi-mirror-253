from strmetrics.levenshtein import Levenshtein


class LevenshteinNormalized:

    def __init__(self) -> None:
        self.levenshtein = Levenshtein()

    def distance(self, s0, s1):
        max_len = max(len(s0), len(s1))
        return 1.0 - (self.levenshtein.distance(s0, s1) / max_len)
    

if __name__ == "__main__":
    d = LevenshteinNormalized()
    print(d.distance("Hi", "Hello"))
