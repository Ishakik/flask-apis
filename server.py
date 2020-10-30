from flask import Flask, request
app = Flask(__name__)
API_PREFIX = '/api'


# A Api to encrypt the input string passed in the payload
@app.route(API_PREFIX + '/encrypt', methods=['POST'])
def encrypt():
    # Extract the json field with ame Input from request
    input_string = request.json['Input']
    # check is input string is empty or not. return 400 response if input is empty
    if input_string:
        encrypted_string = encrypt_string(input_string)
        return build_response(input_string, encrypted_string, 'success', 'encryption successful'), 200
    else:
        return build_response(input_string, '', 'failure', 'input should not be empty'), 400


# a decryption api to decrypt the provided string input.
@app.route(API_PREFIX + '/decrypt', methods=['POST'])
def decrypt():
    # Extract the json field with ame Input from request
    input_string = request.json['Input']
    # check is input string is empty or not. return 400 response if input is empty
    if input_string:
        decrypted_string = decrypt_string(input_string)
        return build_response(input_string, decrypted_string, 'success', 'decryption successful'), 200
    else:
        return build_response(input_string, '', 'failure', 'input should not be empty'), 400


# Health check endpoint to verify if the server is up and running.
@app.route(API_PREFIX + '/health', methods=['GET'])
def health():
    return {'server health': 'GREEN'}, 200


# An encryption function to encrypt the given string
def encrypt_string(input_string):
    return 'Encrypted_' + input_string + '_String'


# A decryption function to decrypt the provided string
def decrypt_string(input_string):
    return input_string.replace('Encrypted_', '').replace('_String', '')


# An utility function to build the response when required. Returns a response object
def build_response(input_string, output_string, status, message):
    response = {
        'Input': input_string,
        'Output': output_string,
        'Status': status,
        'Message': message
    }
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)

