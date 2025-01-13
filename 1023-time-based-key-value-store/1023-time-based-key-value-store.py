from collections import defaultdict


class TimeMap:
    """
    Time-based key-value store that allows storing and retrieving values based on timestamps
    Uses binary search for efficient retrieval of values
    """

    def __init__(self):
        # Initialize dictionary with list as default value for each key
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key-value pair along with timestamp
        Values are stored in sorted order by timestamp
        """
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieve value for key at or before given timestamp
        Returns empty string if no value exists before timestamp
        Uses binary search for O(log n) time complexity
        """
        values = self.m[key]
        if not values: return ''

        # Binary search boundaries
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Exact timestamp match found
            if values[mid][0] == timestamp:
                return values[mid][1]

            # Search right half if current timestamp is too small
            elif values[mid][0] <= timestamp:
                left = mid + 1

            # Search left half if current timestamp is too large
            else:
                right = mid - 1

        # Return value with largest timestamp <= target
        if right >= 0:
            return values[right][1]     # Valid earlier timestamp exists

        return ''   # No valid timestamp exists before target
