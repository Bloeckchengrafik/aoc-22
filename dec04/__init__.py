class Pair:
    def __init__(self, input_string: str):
        self.lower = int(input_string.split("-")[0])
        self.upper = int(input_string.split("-")[1])

    def __str__(self):
        return f"{self.lower}-{self.upper}"

    def __contains__(self, pair) -> bool:
        return self.lower <= pair.lower and self.upper >= pair.upper

    def overlaps(self, pair) -> bool:
        """
        Check if one pair overlaps with another pair,
        i.e. if the lower or upper bound of one pair is between the bounds of the other pair
        """
        return self.lower <= pair.lower <= self.upper or self.lower <= pair.upper <= self.upper
