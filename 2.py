# Author : ./R15K1 | V4N654T
import zlib, base64
exec(zlib.decompress(base64.b64decode("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")))