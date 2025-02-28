class LZString:
    @staticmethod
    def compress(uncompressed: str | None) -> str: ...
    @staticmethod
    def compressToUTF16(uncompressed: str | None) -> str: ...
    @staticmethod
    def compressToBase64(uncompressed: str | None) -> str: ...
    @staticmethod
    def compressToEncodedURIComponent(uncompressed: str | None) -> str: ...
    @staticmethod
    def decompress(compressed: str | None) -> str | None: ...
    @staticmethod
    def decompressFromUTF16(compressed: str | None) -> str | None: ...
    @staticmethod
    def decompressFromBase64(compressed: str | None) -> str | None: ...
    @staticmethod
    def decompressFromEncodedURIComponent(compressed: str | None) -> str | None: ...
