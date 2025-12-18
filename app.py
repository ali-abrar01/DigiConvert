from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Serve static files from templates directory as per frontend structure
@app.route('/style.css')
def serve_css():
    return send_from_directory('templates', 'style.css')

@app.route('/script.js')
def serve_js():
    return send_from_directory('templates', 'script.js')

# Core Logic Functions

def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return None

def decimal_to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except ValueError:
        return None

def binary_to_gray(binary_str):
    """
    Gray = Binary XOR (Binary >> 1)
    """
    try:
        n = int(binary_str, 2)
        gray_val = n ^ (n >> 1)
        return bin(gray_val)[2:]
    except ValueError:
        return None

def gray_to_binary(gray_str):
    """
    To convert Gray to Binary:
    1. The MSB of the Binary code is the same as the MSB of the Gray code.
    2. The subsequent bits are obtained by XORing the previous binary bit with the current gray bit.
    Example: Gray 1010
    B0 = G0 = 1
    B1 = B0 ^ G1 = 1 ^ 0 = 1
    B2 = B1 ^ G2 = 1 ^ 1 = 0
    B3 = B2 ^ G3 = 0 ^ 0 = 0
    Result: 1100
    """
    try:
        # Check input validity (only 0 and 1)
        if not all(c in '01' for c in gray_str):
            raise ValueError("Invalid Gray Code")
        
        binary_code = ""
        binary_code += gray_str[0] # MSB is the same
        
        for i in range(1, len(gray_str)):
            prev_binary_bit = int(binary_code[i-1])
            current_gray_bit = int(gray_str[i])
            next_binary_bit = prev_binary_bit ^ current_gray_bit
            binary_code += str(next_binary_bit)
            
        return binary_code
    except (ValueError, IndexError):
        return None

def generate_steps(conversion_type, inp, res):
    steps = []
    if conversion_type == 'bin2dec':
        steps.append(f"Received Binary Input: {inp}")
        steps.append("Formula: Sum of (digit × 2^position)")
        rev_inp = inp[::-1]
        calculation = []
        val = 0
        for i, char in enumerate(rev_inp):
            bit = int(char)
            if bit == 1:
                term = 2**i
                calculation.append(f"2^{i} = {term}")
                val += term
        steps.append(f"Summing active bits: {' + '.join(calculation)} = {val}")
        steps.append(f"Result: {val}")

    elif conversion_type == 'dec2bin':
        steps.append(f"Received Decimal Input: {inp}")
        steps.append("Method: Successive Division by 2")
        n = int(inp)
        if n == 0:
             steps.append("0 / 2 = 0, Remainder = 0")
        else:
            temp_n = n
            calc_steps = []
            while temp_n > 0:
                rem = temp_n % 2
                div = temp_n // 2
                calc_steps.append(f"{temp_n} ÷ 2 = {div}, Remainder = {rem}")
                temp_n = div
            steps.extend(calc_steps)
            steps.append("Read remainders from bottom to top.")
        steps.append(f"Result: {res}")

    elif conversion_type == 'bin2gray':
        steps.append(f"Received Binary Input: {inp}")
        steps.append("Formula: Gray = Binary ⊕ (Binary >> 1) (Right shift and XOR)")
        steps.append(f"Original:   {inp}")
        shifted = '0' + inp[:-1]
        steps.append(f"Shifted:    {shifted} (Shift right by 1)")
        steps.append("Perform XOR bit by bit:")
        xor_steps = []
        for i in range(len(inp)):
            b = int(inp[i])
            s = int(shifted[i])
            xor_steps.append(f"{b} ⊕ {s} = {b^s}")
        steps.append(" | ".join(xor_steps))
        steps.append(f"Result: {res}")

    elif conversion_type == 'gray2bin':
        steps.append(f"Received Gray Code Input: {inp}")
        steps.append("Method: Iterative XOR")
        steps.append(f"MSB stays same: {inp[0]} -> {inp[0]}")
        prev = int(inp[0])
        trace = [f"B0 = {prev}"]
        for i in range(1, len(inp)):
             curr_gray = int(inp[i])
             new_bin = prev ^ curr_gray
             trace.append(f"B{i} = B{i-1}({prev}) ⊕ G{i}({curr_gray}) = {new_bin}")
             prev = new_bin
        steps.extend(trace)
        steps.append(f"Result: {res}")

    return steps


# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    conversion_type = data.get('type')
    value = data.get('value')
    
    if not value:
        return jsonify({'error': 'Input cannot be empty'}), 400
    
    result = None
    error = None
    
    if conversion_type == 'bin2dec':
        # Validate Binary
        if not all(c in '01' for c in value):
             return jsonify({'error': 'Invalid Binary Input'}), 400
        result = binary_to_decimal(value)
        
    elif conversion_type == 'dec2bin':
        # Validate Decimal
        if not value.isdigit():
             return jsonify({'error': 'Invalid Decimal Input'}), 400
        result = decimal_to_binary(value)
        
    elif conversion_type == 'bin2gray':
        if not all(c in '01' for c in value):
             return jsonify({'error': 'Invalid Binary Input'}), 400
        result = binary_to_gray(value)
        
    elif conversion_type == 'gray2bin':
        if not all(c in '01' for c in value):
             return jsonify({'error': 'Invalid Gray Code Input'}), 400
        result = gray_to_binary(value)
        
    else:
        return jsonify({'error': 'Invalid conversion type'}), 400
        
    steps = generate_steps(conversion_type, value, result)
    
    return jsonify({
        'result': str(result),
        'steps': steps
    })

if __name__ == '__main__':
    app.run(debug=True)
