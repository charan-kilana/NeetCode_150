class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # BFM
        for i in strs:
            encoded_str = encoded_str + i + "ram"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_lis = s.split("ram")
        return decoded_lis[0:len(decoded_lis)-1]

