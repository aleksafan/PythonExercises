#https://leetcode.com/problems/encode-and-decode-tinyurl/

"""TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL."""

class Codec:
    def __init__(self):
        self.code2url = {}
        self.url2code = {}
        
    def encode(self, longUrl: str) -> str:
        codebase = string.ascii_letters + string.digits
        while longUrl not in self.url2code:
            code = ''.join([random.choice(codebase) for _ in range(6)])
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        
        return "http://tinyurl.com/"+code

    def decode(self, shortUrl: str) -> str:
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))