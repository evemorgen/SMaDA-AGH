# Cryptography and Security

## Project - DNA Cryptography
For the sake of this project we developed a Python script enabling for encryption and decryption of DNA sequence data and given OTP key.  
This script can be found [here](project/dna_encryption.py)

## Usage example:
To encrypt a message one must provide a OTP key and a message, script will output the DNA sequence corresponding to given input
```bash
python3 dna_encrypt.py --encrypt --text 'some secret message' --key 'super secret key' 
AATCAACCAATTAAAAATCGACTCGCGTACCCACCTGGGGACAG
```

To decrypt a message one must provide same OTP key as used in encryption process as well as DNA sequence to decrypt. Decrypted message should correspond to plain text given in encryption process
```bash
python3 dna_encrypt2.py --decrypt --text 'AATCAACCAATTAAAAATCGACTCGCGTACCCACCTGGGGACAG' --key 'super secret key'
some secret message
```
