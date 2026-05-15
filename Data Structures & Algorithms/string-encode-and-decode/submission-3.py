class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "`"
        join_string = "~".join(strs)
        return join_string

    def decode(self, s: str) -> List[str]:
        if s == "`":
            return []
        return s.split("~")