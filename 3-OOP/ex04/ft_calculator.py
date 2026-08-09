class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = []
        for i in range(len(V1)):
            result.append(V1[i] + V2[i])
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = []
        for i in range(len(V1)):
            result.append(V1[i] - V2[i])
        print("Sous Vector is:", result)