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


JSON Web Token definition: open standard (RFC 7519) that can be verified and trusted because it is digitally signed. Can be signed by using a secret (with HMAC algo) or public/private key pair using RSA or ECDSA.


SHA-512 encoded

payload contains username, entity, and datetime. 



