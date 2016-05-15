## aeswinpy

This project replicates an AES encryption/decryption routine from a Windows .NET project that was being migrated to another server.  I used these methods to verify that the key and initialization vector were correct.  This was a little tricky because of the PKCS7 padding.  Thanfully, there was an existing implementation of the padding that I was able to pull from another project on Github.

This code includes a dummy key and IV that are left in the code so it will run correctly as-is.  
