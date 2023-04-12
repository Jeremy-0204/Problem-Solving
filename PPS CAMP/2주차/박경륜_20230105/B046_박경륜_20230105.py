class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # remember the first color
        init_color = image[sr][sc]

        # do the flood fill
        def flood_fill(x, y):
            if x < 0 or x >= len(image): return None
            if y < 0 or y >= len(image[0]): return None

            if image[x][y] == color: return None
            if image[x][y] != init_color: return None

            image[x][y] = color

            flood_fill(x-1, y)  # top
            flood_fill(x+1, y)  # bottom
            flood_fill(x, y+1)  # right
            flood_fill(x, y-1)  # left

        flood_fill(sr, sc)
        return image