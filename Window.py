import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        // **Target** frequency map
        target_map = collections.Counter(t)
        
        start = 0
        min_len = float('inf')
        left = 0
        count = 0
        needed = len(t)
        
        // Use the target_map for both tracking need and current availability
        for right in range(len(s)):
            char_right = s[right]
            
            if char_right in target_map:
                if target_map[char_right] > 0:
                    count += 1
                target_map[char_right] -= 1

            // **Shrink** the window while it is valid
            while count == needed:
                current_len = right - left + 1
                // Update result
                if current_len < min_len:
                    min_len = current_len
                    start = left
                
                char_left = s[left]
                if char_left in target_map:
                    target_map[char_left] += 1
                    if target_map[char_left] > 0:
                        count -= 1

                left += 1

        return s[start:start+min_len] if min_len != float('inf') else ""
