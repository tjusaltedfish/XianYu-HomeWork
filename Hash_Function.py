import base64
import hashlib

def main():     #调用了hashlib，对字符串进行了两次转码加密
    BeforeHash = input('请输入想要加密的字符串\n')
    Mymd5 = hashlib.md5()
    Mymd5.update(BeforeHash.encode('utf-8'))
    hash_in_bytes = Mymd5.digest()
    result = base64.b32encode(hash_in_bytes)
    result = result.strip(b'=')
    print(result)

if __name__ == "__main__":
    main()