class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l = sentence.split(" ")

        for i, v in enumerate(l):
            if len(v) > 1 and v[0] == "$" and v[1:].isdigit():
                price = int(v[1:])
                l[i] = f"${price * (100 - discount) / 100:.2f}"

        return " ".join(l)