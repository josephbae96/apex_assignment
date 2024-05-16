# apex_assignment

Joseph Bae's take home assignment.

Notes and thought process:

Task 1- JWS Generation
Many APIs use an access token of some sort to control who can call given endpoints; some use a Json Web Token, as described here https://jwt.io/introduction . For Task 1, imagine you have been presented with the following key:

{
‘username’: jws-test,
‘entity’: apex,
‘sharedSecret’: 1234567890
}

Using these credentials, write a script that generates a SHA-512 encoded JWS, with a payload that contains the username, entity, and datetime. Provide this JWS and be ready to explain the script you wrote to generate this.

Notes:
JSON Web Token definition: open standard (RFC 7519) that can be verified and trusted because it is digitally signed. Can be signed by using a secret (with HMAC algo) or public/private key pair using RSA or ECDSA.

SHA-512 encoded: cryptographic hash that produced a 512 bit hash value. meaning that it'll take an input and return a fixed-length string of 512 bits. It's deterministic which means same input produces same output.

Payload should contain username, entity, and datetime. 
Sharedsecret is provided and can be used as the encryption key used by both parties.

jwt is a library that has an encode function. Can encode using payload, key, and algorithm. Algorithm depends on type, in this case we want HS512 for the SHA-512 encoding.

In general: I used python as the language to create the script because python has many libraries and is great for scripting. Specifically the jwt library is most useful as well as the datetime library.

Since this task has no limitations on the language or the libraries that can be used, I opted to go for the quickest and easiest route which would be to use Python and the jwt library to create a script that generates a SHA-512 encoded JWS.



