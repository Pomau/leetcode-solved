class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image[i])//2):
                image[i][j], image[i][len(image[i]) - j - 1] = image[i][len(image[i]) - j - 1], image[i][j]
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]
        return image